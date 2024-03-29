import json

import qrcode
import qrcode.image.svg
from flask import render_template, request, \
    redirect, session, url_for
from pipe.models import User, GoFutureTable, Role
from pipe import app, bcrypt, db
from pipe.forms import RegisterForm, LoginForm
from pipe.utils import access_required, add_to_magazine, database_default_add
import asyncio
import random
from pipe import Base, engine
from pipe.file_opener_routes import MetrixOrder, Customers, Orders
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from sqlalchemy import select


db_stelmach_session = scoped_session(sessionmaker(bind=engine))



@app.route('/test-fetch', methods=["GET", "POST"])
def test_fetch():
    pattern = request.form.get('pattern')
    quantity = request.form.get('number-of-positions')
    no_ag = request.form.get('no-ag')
    print(no_ag)
    if no_ag == 'on':
        all_orders_with_pattern = db_stelmach_session.query(Orders.id, Orders.mat_color, Orders.d_shipment) \
            .filter(Orders.pattern_name == pattern, Orders.mat_color is not None, Orders.mat_color != '-')\
            .order_by(Orders.id.desc())\
            .limit(quantity).all()
    else:
        all_orders_with_pattern = db_stelmach_session.query(Orders.id, Orders.mat_color, Orders.d_shipment) \
            .filter(Orders.pattern_name == pattern).order_by(Orders.id.desc()).limit(quantity).all()

    print(pattern)
    if request.method == 'post':
        return render_template('test.html',)
    else:
        return render_template('test.html',)



@app.route('/test;no-ag=<no_ag>;ring=<int:pattern>;orders-quantity=<int:quantity>', methods=["GET", "POST"])
async def test(no_ag, pattern, quantity):
    print(no_ag)
    print(pattern)
    print(quantity)

    if no_ag == 'on':
        all_orders_with_pattern = db_stelmach_session.query(Orders.id, Orders.mat_color, Orders.d_shipment) \
            .filter(Orders.pattern_name == pattern, Orders.mat_color is not None, Orders.mat_color != '-')\
            .order_by(Orders.id.desc())\
            .limit(quantity).all()
    else:
        all_orders_with_pattern = db_stelmach_session.query(Orders.id, Orders.mat_color, Orders.d_shipment) \
            .filter(Orders.pattern_name == pattern).order_by(Orders.id.desc()).limit(quantity).all()




    json_string = json.dumps(all_orders_with_pattern, default=str)

    return {'data': json_string}
    # return {}

@app.route('/register', methods=['GET', 'POST'])
# @access_required('admin')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        role_id = 0
        role = form.access.data
        roles = Role.query.all()
        for r in roles:
            if r.name == role:
                role_id = r.id
        hashed_password = bcrypt.generate_password_hash(form.password.data)

        new_user = User(username=form.username.data,
                        password=hashed_password,
                        role=role)
        db.session.add(new_user)
        db.session.flush()
        db.session.refresh(new_user)

        # new_user_roles = UserRoles(user_id=new_user.id, role_id=role_id)
        # db.session.add(new_user_roles)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('username', 'logged out') != "logged out":
        print("username:", session.get("username", "logged out"))
        print("role:", session.get("role", "brak"))
        return render_template('no_access.html')
    else:
        print("username:", session.get("username", "logged out"))
        print("role:", session.get("role", "brak"))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            session["username"] = request.form.get('username')
            session["role"] = user.role

            if 'technolog' in session['role']:
                session['role'] = ['operator', 'technolog']
            if 'kierownik' in session['role']:
                session['role'] = ['kierownik', 'operator', 'technolog']
            if 'prezes' in session['role']:
                session['role'] = ['operator', 'technolog', 'kierownik', 'prezes']
            if 'admin' in session['role']:
                session['role'] = ['operator', 'kierownik', 'admin', 'technolog', 'prezes']

            if 'admin' in session["role"]:
                return redirect("/dashboard")
            if 'kierownik' in session["role"]:
                return redirect("/")
            if 'operator' in session['role']:
                return redirect("/")

            return redirect("/login")
        return render_template('login.html', form=form)


@app.route("/dashboard", methods=["GET", "POST"])
@access_required('admin')
def dashboard():
    return render_template("dashboard.html")


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('opened_details1', None)
    session.pop('opened_details2', None)
    return redirect(url_for('login'))


@app.route("/5atwork", methods=["GET", "POST"])
@access_required('operator')
def stan3_menu3():
    with open("\\\\10.0.0.5\\public\\MAGDA\\CELIK PDFY\\1494915.pdf") as f:
        file = f.readlines()
    return render_template("5atwork_celik_trend.html", file=file)


@app.route("/send-orders", methods=['GET', 'POST'])
def send_orders():
    if request.method == "POST":
        arkusz = request.get_json()
        type = arkusz['type']
        date = arkusz['date']
        gold_color_type = arkusz['gold_color_type']
        orders = arkusz['orders']
        for i, order in enumerate(orders):
            order_id = order[0]
            pipe = order[1]
            program = order[2]
            r50 = order[3]
            r51 = order[4]
            r52 = order[5]
            r60 = order[6]
            r40 = order[7]
            r61 = order[8]
            r41 = order[9]
            r20 = order[10]
            p1 = order[11]
            p2 = order[12]
            p3 = order[13]
            p5 = order[14]

            img = qrcode.make(f'{r50}\r{r51}\r{r52}\r{r60}\r{r40}\r{r61}\r{r41}\r{r20}\r{p1}\r{p2}\r{p3}\r\r{p5}',
                              image_factory=qrcode.image.svg.SvgImage)
            img.save("1.svg")
            with open('1.svg', encoding="utf8") as f:
                qrcode_data = f.read()
            code = qrcode_data

            new_order = GoFutureTable(date=date, type=type, gold_color_type=gold_color_type, order_id=order_id,
                                      pipe=pipe,
                                      program=program, r50=r50, r51=r51, r52=r52, r60=r60, r40=r40, r61=r61,
                                      r41=r41, r20=r20, p1=p1, p2=p2, p3=p3, p5=p5, code=code)

            # warunki dla zlecen
            if new_order.type == "na gotowo":
                new_order.place = "g"
            if new_order.type == "na surowo":
                new_order.place = "f"
            if new_order.pipe == "":
                new_order.place = "k"

            if new_order.program == "":
                if new_order.r50 != "":
                    new_order.program = "RING_AB_GR_1_SR"

            if new_order.program == "RING_AB_GR_1_SR":
                if new_order.r50 == "":
                    new_order.program = "RING_TUL"

            try:
                db.session.add(new_order)
                db.session.commit()
            except:
                return "there was an issue with your orders"

            # showmess("DODANO NOWE ZLECENIA")

        return "sukces"
    else:
        return "bladdddd"




@app.route('/', methods=['POST', 'GET'])
@access_required("operator")
def index():
     return render_template("index.html")



@app.route('/manage-orders-to-describe', methods=['POST', 'GET'])
@access_required("kierownik")
def manage_rings_to_describe():
    orders_to_describe = GoFutureTable.query.filter_by(place='k').order_by(GoFutureTable.type).all()
    return render_template('manage_rings_to_describe.html', orders_to_describe=orders_to_describe)


@app.route('/gofuture/color-pipe-order', methods=['POST', 'GET'])
@access_required("operator")
def color_pipe_order():
    current_order = ""
    if request.method == "POST":
        key = request.form.to_dict()
        key = list(key.keys())[0]
        print(key)
        order_ring_sr = GoFutureTable.query.filter_by(place='f', program='RING_AB_GR_1_SR').order_by(GoFutureTable.type).all()
        for order in order_ring_sr:
            # print(order.order_id)
            if int(order.id) == int(key):
                print("weszlo")
                date = order.date
                pipe = order.pipe
                gold_color_type = order.gold_color_type
                type = order.type
                first_detail = f'{date}_{gold_color_type}_{type}'
                second_detail = f'{date}_{gold_color_type}_{type}_{pipe}'
                opened_details = [first_detail, second_detail]
                session['opened_details1'] = opened_details[0]
                session['opened_details2'] = opened_details[1]

        return redirect(f'/gofuture/color-order/clicked_done/{key}', )

        # order_id = request.form["done"]
        # print(order_id)
    else:
        print(session.get('opened_details', 'brak'))
        orders_ring_sr = GoFutureTable.query.filter_by(place='f', program='RING_AB_GR_1_SR').order_by(GoFutureTable.type).all()
        # print(orders_ring_sr)

        kolory_proby = []
        count_list = []
        dict_with_pipes = {}

        for order in orders_ring_sr:
            kolor_proba = f'{order.gold_color_type} {order.type} >{order.date}'
            if kolor_proba not in kolory_proby:
                kolory_proby.append(kolor_proba)
                position_of_space = kolor_proba.index(" ")
                type_gold_color = kolor_proba[:position_of_space]
                index_of_greater = kolor_proba.index(">")
                type_of_arkusz = kolor_proba[position_of_space + 1:index_of_greater - 1]
                date = kolor_proba[index_of_greater + 1:]
                pipes = GoFutureTable.query.filter_by(place='f', program='RING_AB_GR_1_SR', type=type_of_arkusz, gold_color_type=type_gold_color, date=date).with_entities(GoFutureTable.pipe).distinct().all()
                dict_with_pipes[kolor_proba] = pipes
        # print(dict_with_pipes)
        # for x in dict_with_pipes.values():
            # print(x)

        for typ in kolory_proby:
            position_of_space = typ.index(" ")
            type_gold_color = typ[:position_of_space]
            index_of_greater = typ.index(">")
            type_of_arkusz = typ[position_of_space + 1:index_of_greater - 1]
            date = typ[index_of_greater + 1:]
            order1 = GoFutureTable.query.filter_by(place='f', gold_color_type=type_gold_color, type=type_of_arkusz,
                                                   date=date).count()
            count_list.append(order1)

        return render_template('gofuture-color-pipe-order.html', orders_ring_sr=orders_ring_sr, kolory_proby=kolory_proby, dict_with_pipes=dict_with_pipes)


@app.route('/gofuture/color-pipe-order/clicked_done/<int:id>', methods=['POST', 'GET'])
@access_required("operator")
def clicked_done(id):
    order = GoFutureTable.query.get_or_404(id)
    order.place = 'z'

    try:
        db.session.commit()
        return redirect('/gofuture/color-order')
    except:

        return 'There was an issue updating your task'


@app.route('/gofuture/color-width-orders/clicked_done/<int:id>', methods=['POST', 'GET'])
@access_required("operator")
def clicked_done_width(id):
    order = GoFutureTable.query.get_or_404(id)
    order.place = 'z'
    try:
        db.session.commit()
        return redirect('/gofuture/color-width-orders')
    except:
        return 'There was an issue updating your task'


@app.route('/gofuture/one-order-scan', methods=['POST', 'GET'])
@access_required("operator")
def one_order_scan():
    if request.method == "POST":
        order_id = request.form['order_id']
        return redirect(f'/gofuture/one-order-scan/{order_id}')
    else:
        return render_template('gofuture-one-order-scan.html')


@app.route('/gofuture/one-order-scan/<string:order_id>', methods=['POST', 'GET'])
@access_required("operator")
def show_order(order_id):
    orders = GoFutureTable.query.filter_by(place='f').order_by(GoFutureTable.type).all()
    showed_order = []
    if len(orders) == 0:
        return render_template('gofuture-one-order-scan.html')
    for order in orders:
        type_of_arkusz = order.type
        width = order.r51
        gold_color_type = order.gold_color_type
        pipe = order.pipe
        svg = order.code
        date = order.date
        if order.order_id == order_id:
            showed_order.append([order.id, gold_color_type, pipe, type_of_arkusz, order.order_id, svg, date, width])

    return render_template('gofuture-one-order-scan.html', date=date, showed_order=showed_order, pipe=pipe, width=width, type_of_arkusz=type_of_arkusz)


@app.route('/gofuture/color-width-orders', methods=['POST', 'GET'])
@access_required("operator")
def color_width_orders():
    if request.method == "POST":
        key = request.form.to_dict()
        key = list(key.keys())[0]
        orders_ring_sr = GoFutureTable.query.filter_by(place='f', program='ring_tul').order_by(
            GoFutureTable.type).all()
        for order in orders_ring_sr:
            # print(order.order_id)
            if int(order.id) == int(key):
                print("weszlo")
                date = order.date
                pipe = order.pipe
                gold_color_type = order.gold_color_type
                type = order.type
                first_detail = f'{date}_{gold_color_type}_{type}'
                second_detail = f'{date}_{gold_color_type}_{type}_{pipe}'
                opened_details = [first_detail, second_detail]
                session['opened_details1'] = opened_details[0]
                session['opened_details2'] = opened_details[1]
        return redirect(f'/gofuture/color-width-orders/clicked_done/{key}')
    else:
        orders_ring_sr = GoFutureTable.query.filter_by(place='f', program='ring_tul').order_by(
            GoFutureTable.type).all()
        print(orders_ring_sr)

        kolory_proby = []
        count_list = []
        dict_with_pipes = {}

        for order in orders_ring_sr:
            kolor_proba = f'{order.gold_color_type} {order.type} >{order.date}'
            if kolor_proba not in kolory_proby:
                kolory_proby.append(kolor_proba)
                position_of_space = kolor_proba.index(" ")
                type_gold_color = kolor_proba[:position_of_space]
                index_of_greater = kolor_proba.index(">")
                type_of_arkusz = kolor_proba[position_of_space + 1:index_of_greater - 1]
                date = kolor_proba[index_of_greater + 1:]
                filtered_orders = GoFutureTable.query.filter_by(place='f', program='ring_tul', type=type_of_arkusz,
                                                                gold_color_type=type_gold_color, date=date).order_by(GoFutureTable.r51).all()
                print(filtered_orders)
                pipes = GoFutureTable.query.filter_by(place='f', program='ring_tul', type=type_of_arkusz,
                                                      gold_color_type=type_gold_color, date=date).with_entities(
                    GoFutureTable.pipe).distinct().all()
                dict_with_pipes[kolor_proba] = pipes
        print(dict_with_pipes)
        for x in dict_with_pipes.values():
            print(x)

        for typ in kolory_proby:
            position_of_space = typ.index(" ")
            type_gold_color = typ[:position_of_space]
            index_of_greater = typ.index(">")
            type_of_arkusz = typ[position_of_space + 1:index_of_greater - 1]
            date = typ[index_of_greater + 1:]
            order1 = GoFutureTable.query.filter_by(place='f', gold_color_type=type_gold_color, type=type_of_arkusz,
                                                   date=date).count()
            count_list.append(order1)

        return render_template('gofuture-color-width-order.html', orders_ring_sr=orders_ring_sr, kolory_proby=kolory_proby,
                               dict_with_pipes=dict_with_pipes)


@app.route('/gofuture/done', methods=['POST', 'GET'])
@access_required("operator")
def done():
    if request.method == "POST":
        closed_orders = GoFutureTable.query.filter_by(place='z').all()
        checkbox_list = request.form.getlist('mycheckbox')
        print(checkbox_list)
        print(closed_orders)
        for order in closed_orders:
            if str(order.id) in checkbox_list:
                print(order.id)
                print("jest")
                order.place = 'f'
        try:
            db.session.commit()
            return redirect('/gofuture/done')
        except:
            return 'wystapil problem z przeniesieniem zlecen'

    else:
        orders = GoFutureTable.query.filter_by(place='z')
        return render_template('gofuture-done.html', orders=orders)


@app.route('/gofuture/move', methods=['POST', 'GET'])
@access_required("operator")
def move():
    if request.method == 'POST':
        orders_list_to_change_place = []
        orders = GoFutureTable.query.order_by(GoFutureTable.type).all()
        checkbox_list = request.form.getlist('mycheckbox')
        print(checkbox_list)
        if 'do-kierownika' in checkbox_list:
            checkbox_list.pop()
            for order in orders:
                if str(order.id) in checkbox_list:
                    print("do kierownika")
                    orders_list_to_change_place.append(order)
            print(orders_list_to_change_place)

            for order in orders_list_to_change_place:
                order.place = 'k'
            try:
                db.session.commit()
                return redirect('/gofuture/move')
            except:
                return 'wystapil problem z przeniesieniem zlecen'
        else:
            print("na goringa")
            if 'na-goringa' in checkbox_list:
                checkbox_list.pop()
                for order in orders:
                    if str(order.id) in checkbox_list:
                        orders_list_to_change_place.append(order)

                for order in orders_list_to_change_place:
                    order.place = 'g'
                try:
                    db.session.commit()
                    return redirect('/gofuture/move')
                except:
                    return 'wystapil problem z przeniesieniem zlecen'

        return redirect('/gofuture/move')

    else:
        kolory_proby = []
        count_list = []
        all_gofuture_orders = GoFutureTable.query.filter_by(place='f').all()
        all_gofuture_orders_length = GoFutureTable.query.filter_by(place='f').count()

        for order in all_gofuture_orders:
            kolor_proba = f'{order.gold_color_type} {order.type} >{order.date}'
            if kolor_proba not in kolory_proby:
                kolory_proby.append(kolor_proba)

        for typ in kolory_proby:
            position_of_space = typ.index(" ")
            type_gold_color = typ[:position_of_space]
            index_of_greater = typ.index(">")
            type_of_arkusz = typ[position_of_space + 1:index_of_greater - 1]
            date = typ[index_of_greater + 1:]
            order1 = GoFutureTable.query.filter_by(place='f', gold_color_type=type_gold_color, type=type_of_arkusz, date=date).count()
            count_list.append(order1)

        return render_template('gofuture-move.html', all_gofuture_orders=all_gofuture_orders, kolory_proby=kolory_proby, all_gofuture_orders_length=all_gofuture_orders_length)


@app.route('/description-required', methods=['POST', 'GET'])
@access_required("operator")
def description_required():
    kolory_proby = []
    count_list = []
    orders_to_describe = GoFutureTable.query.filter_by(place='k').order_by().all()

    for order in orders_to_describe:
        kolor_proba = f'{order.gold_color_type} {order.type} >{order.date}'
        if kolor_proba not in kolory_proby:
            kolory_proby.append(kolor_proba)

    for typ in kolory_proby:
        position_of_space = typ.index(" ")
        type_gold_color = typ[:position_of_space]
        index_of_greater = typ.index(">")
        type_of_arkusz = typ[position_of_space + 1:index_of_greater - 1]
        date = typ[index_of_greater + 1:]
        order1 = GoFutureTable.query.filter_by(place='k', gold_color_type=type_gold_color, type=type_of_arkusz, date=date).count()
        count_list.append(order1)
    return render_template('description-required.html', orders_to_describe=orders_to_describe, kolory_proby=kolory_proby, count_list=count_list)
