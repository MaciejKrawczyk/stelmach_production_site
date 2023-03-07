from flask import render_template, request, redirect, session, Blueprint
from pipe import Base, engine
import json


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

    length = len(order_id)
    position_of_underscore = order_id.index('_')
    order_id_modified = order_id[:position_of_underscore - length]
    print(order_id)
    print(order_id_modified)
    db_stelmach_session = scoped_session(sessionmaker(bind=engine))

    history_link = f"http://10.0.0.2/move/zlecenie/{order_id_modified}/orders"
    details_link = f'http://10.0.0.2/orders/edit/{order_id_modified}/'

    celik_trendseller = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().pdf_name
    if celik_trendseller is not None:
        if db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().customer_id == CELIK_ID:
            print('celik')
            client = 'Celik'
            date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
            pdf_link = f"/static/public/MAGDA/CELIK PDFY/{celik_trendseller}.pdf"
            # pdf_link = f'http://10.0.0.5/public/MAGDA/TRENDSELLER/{celik_trendseller}.pdf'

        else:
            client = 'Trendseller'
            date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
            print('trendseller')
            pdf_link = f"/static/public/MAGDA/TRENDSELLER/Trendseller{celik_trendseller}.pdf"
            # pdf_link = f'http://10.0.0.5/public/MAGDA/TRENDSELLER/Trendseller{celik_trendseller}.pdf'
    else:
        print('metrix')
        date = db_stelmach_session.query(Orders).filter(Orders.id == order_id_modified).first().d_shipment
        client_id = db_stelmach_session.query(MetrixOrder).filter(MetrixOrder.order_id == order_id_modified).first().customer_id
        client = db_stelmach_session.query(Customers).filter(Customers.id == client_id).first().name
        pdf_link = f'http://10.0.0.2/metrix/order_data/{order_id_modified}/production.pdf'
    if request.method == 'POST':
        return redirect(f'/file-opener/{order_id}')
    else:
        return render_template('file-opener/file-opener.html', pdf_link=pdf_link,
                               history_link=history_link, details_link=details_link, client=client, date=date)

