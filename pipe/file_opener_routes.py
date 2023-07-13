from flask import render_template, request, redirect, Blueprint
from pipe import Base, engine
from pipe.celik_list import celik_list


file_opener_routes = Blueprint("file_opener_routes", __name__, static_folder="static", template_folder="templates")




class MetrixOrder(Base):
    __table__ = Base.metadata.tables['metrix_order']


class Customers(Base):
    __table__ = Base.metadata.tables['customers']


class Orders(Base):
    __table__ = Base.metadata.tables['orders']


@file_opener_routes.route('/file-opener', methods=["GET", "POST"])
def openopen():
    history_link = '#'
    details_link = '#'
    pdf_link = ''
    client = '-'
    date = '-'
    if request.method == 'POST':
        id = request.form.get('id')
        return redirect(f'file-opener/{id}')
    else:
        return render_template('file-opener/file-opener.html',pdf_link=pdf_link,
                               history_link=history_link, details_link=details_link, client=client, date=date)

@file_opener_routes.route('/file-opener/<string:order_id>', methods=["GET", "POST"])
def open(order_id):
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    CELIK_ID = 1952
    TRENDSELLER_ID = 2802

    date = ""
    client = ""
    pdf_link = ""
    description = ''

    length = len(order_id)
    position_of_underscore = order_id.index('_')
    order_id_modified = order_id[:position_of_underscore - length]
    print(order_id)
    print(order_id_modified)
    db_stelmach_session = scoped_session(sessionmaker(bind=engine))

    history_link = f"http://10.0.0.2/move/zlecenie/{order_id_modified}/orders"
    details_link = f'http://10.0.0.2/orders/edit/{order_id_modified}/'

    celik_trendseller = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().pdf_name
    is_metrix = db_stelmach_session.query(MetrixOrder).filter(MetrixOrder.order_id == order_id_modified).first()
    print(f'wynik: {celik_trendseller}')

    if celik_trendseller is not None and celik_trendseller != "":
        if db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().customer_id == CELIK_ID:
            client = 'Celik'
            date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
            pdf_link = f"/static/public/MAGDA/CELIK PDFY/{celik_trendseller}.pdf"
            # pdf_link = f'http://10.0.0.5/public/MAGDA/TRENDSELLER/{celik_trendseller}.pdf'
            pattern = "spec"
        else:
            client = 'Trendseller'
            date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
            pdf_link = f"/static/public/MAGDA/TRENDSELLER/Trendseller{celik_trendseller}.pdf"
            # pdf_link = f'http://10.0.0.5/public/MAGDA/TRENDSELLER/Trendseller{celik_trendseller}.pdf'
            pattern = "spec"

    elif is_metrix is not None:
        date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
        client_id = db_stelmach_session.query(MetrixOrder).filter(MetrixOrder.order_id == order_id_modified).first().customer_id
        client = db_stelmach_session.query(Customers).filter(Customers.id == client_id).first().name
        pdf_link = f'http://10.0.0.2/metrix/order_data/{order_id_modified}/production.pdf'
        pattern = "spec"
        description = ''
    else:
        date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
        client_id = db_stelmach_session.query(Orders).filter(
            Orders.id == order_id_modified).first().customer_id
        client = db_stelmach_session.query(Customers).filter(Customers.id == client_id).first().name
        pdf_link = ""
        pattern = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().pattern_name
        if pattern == 'spec':
            for x in celik_list:
                print(x)
                if x in description:
                    print(f'znaleziono! {x}')
                    pdf_link = f'http://10.0.0.2/img/obraczki_katalog/zdjecia/{x.upper()}.jpg'
                    break
        else:
            if pattern.isdigit() and 1 <= int(pattern) <= 539:
                if len(pattern) < 3:
                    pdf_link = f'http://10.0.0.2/img/obraczki_katalog/zdjecia/0{pattern}.jpg'
                else:
                    pdf_link = f'http://10.0.0.2/img/obraczki_katalog/zdjecia/{pattern}.jpg'

            elif len(pattern) == 4 and pattern[0] == '4':
                print('kruk')
            elif 'PLZ' in pattern:
                pdf_link = "ausko"
                print("aukso ok")
            elif 'SV' in pattern:
                print('savcki ok')
            elif 'A' in pattern:
                print('arenart ok')
                pdf_link = f"/static/pattern_images/arenart/{pattern}.png"
            elif 'SL' in pattern:
                pdf_link = f"/static/pattern_images/jaracz/{pattern}.jpg"
                print('jaracz ok')
            elif len(pattern) == 4 and pattern[0] == 7:
                print('gessele ok')
            elif len(pattern) == 4 and pattern[0] == 9:
                print('alo ok')
            elif 'MD' in pattern:
                print('marry and me ok')
            # brakuje ravajeer
            elif 'SCH' in pattern:
                print('schubert ok')
            elif pattern[0] == 'S':
                print('skorpion ok')
            # brakuje eliasz zofia
            elif pattern[0] == 'L':
                pdf_link = f"/static/pattern_images/luva/{pattern}.png"
            elif 'AD' in pattern:
                print('adiamo')

    if request.method == 'POST':
        return redirect(f'/file-opener/{order_id}')
    else:
        db_stelmach_session.close()
        return render_template('file-opener/file-opener.html', pdf_link=pdf_link,
                               history_link=history_link, details_link=details_link, client=client, date=date,
                               pattern=pattern)

