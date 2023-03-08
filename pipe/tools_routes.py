import os.path, os
import shutil
from math import ceil
from flask import render_template, request, \
    redirect, session, send_file, Blueprint
from pipe.models import History, Position, Tools
from pipe import db, redirect_tools_link
from pipe.utils import access_required, add_to_magazine, add_to_magazine_new
from werkzeug.utils import secure_filename
from pipe.utils import tools_dead_count, tools_sent_count, tools_all_count, tools_waiting_room


tools_routes = Blueprint("tools_routes", __name__, static_folder="static", template_folder="templates")

def name_of_id_position(id):
    id = int(id)
    position = Position.query.filter_by(id=id).first()
    print(position)
    return position.pretty_name


@tools_routes.route('/tools/magazyn/', methods=['POST', 'GET'])
@access_required("technolog")
def tools():
    title = 'MAGAZYN'
    session['title'] = title
    print(f'title: {session.get("title")}')
    positions = Position.query.all()
    # cnc = CNC.query.all()
    tools = Tools.query.filter_by(id_position=1).all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count,
                           waiting_room_tools=waiting_room_tools )


@tools_routes.route('/tools/magazyn-done/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_done():
    link = redirect_tools_link
    title = 'MAGAZYN'
    session['title'] = title
    print(f'title: {session.get("title")}')
    positions = Position.query.all()
    tools = Tools.query.filter_by(id_position=1).all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-post-done.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count,
                           waiting_room_tools=waiting_room_tools, link=link)


@tools_routes.route('/tools/szyba/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_szyba():
    title = 'SZYBA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=2).all()
    positions = Position.query.all()
    # cnc = CNC.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead,
                           send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/stanowisko-6/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_stanowisko_6():
    title='Sttanowisko 6'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=3).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/stanowisko-4/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_stanowisko_4():
    title='stan 4'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=4).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/plat-tytan/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_plat_tytan():
    title='plat-tytan'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=5).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/stanowisko-7/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_stanowisko_7():
    title='stan-7'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=6).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/stanowisko-13/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_stanowisko_13():
    title='stan13'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=7).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/zlom/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_zlom():
    tools = Tools.query.filter_by(id_position=8).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    title = 'ZŁOM'
    session['title'] = title
    print(f'title: {session.get("title")}')
    if request.method == "POST":
        tools_to_change = request.form.getlist('tool')
        for tool in tools:
            if str(tool.id) in tools_to_change:

                history_to_delete = History.query.filter_by(tool_id=tool.id).delete()
                Tools.query.filter(Tools.id == str(tool.id)).delete()
        tools = Tools.query.filter_by(id_position=8).all()
        try:
            path_to_tool_folder = f'./files/{tool.id_dup}'
            # check if there are duplicates
            tools_dup = Tools.query.filter_by(id_dup=tool.id).all()
            if len(tools_dup) == len(tools_to_change):
                shutil.rmtree(path_to_tool_folder)
            db.session.commit()
            return redirect('/tools/zlom/')
        except:
            return 'wystapil blad'
    else:
        return render_template('tools/tools-zlom.html', positions=positions, tools=tools, title=title,
                               all_tools_count=all_tools_count, tools_dead=tools_dead,
                               send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/do-ostrzenia/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_do_ostrzenia():
    title='DO OSTRZENIA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=9).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/w-ostrzeniu/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_w_ostrzeniu():
    title = 'W OSTRZENIU'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools_sharpen = Tools.query.filter_by(id_position=10).all()
    tools = Tools.query.all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    if request.method == "POST":
        if request.form['magazine'] == 'wyslij na magazyn':
            position_id = 1
            position_name = name_of_id_position(position_id)
            tools_to_change = request.form.getlist('tool')
            dict_with_new_tools = {}
            for tool in tools_to_change:
                tool_from_class_db = Tools.query.filter_by(id=tool).first()
                dict_with_new_tools[tool] = tool_from_class_db.shelf_type
            shelves = add_to_magazine(dict_with_new_tools)
            tool_shelf = {}
            tools_shelves = []
            for id, shelf in shelves.items():
                tool_to_change = Tools.query.filter_by(id=id).first()
                tool_to_change.id_position = 1
                new_shelf = shelf[0]
                type_of_shelf = shelf[1]
                tool_to_change.shelf = new_shelf
                tool_shelf[f'id'] = tool_to_change.id
                tool_shelf[f'name'] = tool_to_change.name
                tool_shelf[f'description'] = tool_to_change.description
                tool_shelf[f'shelf'] = new_shelf, type_of_shelf
                dict_copy = tool_shelf.copy()
                tools_shelves.append(dict_copy)
                new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})',
                                      tool_id=tool_to_change.id,
                                      position_id=position_id)
                db.session.add(new_history)
            try:
                db.session.commit()
                return render_template('tools/shelf-number-all-tools.html', tools_shelves=tools_shelves)
            except:
                return 'wystapil problem'
            return render_template('tools/tools-all.html', tools=tools, positions=positions)
        return render_template('tools/tools-all.html', positions=positions, tools=tools)
    else:
        return render_template('tools/tools-w-ostrzeniu.html', positions=positions, tools=tools,
                               send_tools_count=send_tools_count,
                               tools_dead=tools_dead,
                               all_tools_count=all_tools_count,
                               waiting_room_tools=waiting_room_tools,
                               tools_sharpen=tools_sharpen)
@tools_routes.route('/tools/gofuture/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_gofuture():
    title='GOFUTURE'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=11).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/goring-rura/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_goring_rura():
    title='GORING RURA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=12).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/rnd/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_rnd():
    title='RND'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=13).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/goring-rnd/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_goring_rnd():
    title='GORING RND'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=14).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/5-at-work-nowa/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_5atworknowa():
    title='5@WORK NOWA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=15).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/5-at-work-stara/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_5atworkstara():
    title='5@WORK STARA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=16).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/chiron/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_chiron():
    title='CHIRON'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.filter_by(id_position=17).all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    return render_template('tools/tools-list-base.html', positions=positions, tools=tools, title=title,
                           all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)

@tools_routes.route('/tools/szukaj/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_all():
    title = 'SZUKAJ'
    session['title'] = title
    print(f'title: {session.get("title")}')
    tools = Tools.query.all()
    positions = Position.query.all()
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    if request.method == "POST":
        if request.form['magazine'] == 'wyslij na magazyn':
            position_id = 1
            position_name = name_of_id_position(position_id)
            tools_to_change = request.form.getlist('tool')
            dict_with_new_tools = {}
            for tool in tools_to_change:
                tool_from_class_db = Tools.query.filter_by(id=tool).first()
                dict_with_new_tools[tool] = tool_from_class_db.shelf_type
            shelves = add_to_magazine(dict_with_new_tools)
            tool_shelf = {}
            tools_shelves = []
            for id, shelf in shelves.items():
                tool_to_change = Tools.query.filter_by(id=id).first()
                tool_to_change.id_position = 1
                new_shelf = shelf[0]
                type_of_shelf = shelf[1]
                tool_to_change.shelf = new_shelf
                tool_shelf[f'id'] = tool_to_change.id
                tool_shelf[f'name'] = tool_to_change.name
                tool_shelf[f'description'] = tool_to_change.description
                tool_shelf[f'shelf'] = new_shelf, type_of_shelf
                dict_copy = tool_shelf.copy()
                tools_shelves.append(dict_copy)
                new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})', tool_id=tool_to_change.id,
                                      position_id=position_id)
                db.session.add(new_history)
            try:
                db.session.commit()
                return render_template('tools/shelf-number-all-tools.html', tools_shelves=tools_shelves)
            except:
                return 'wystapil problem'
            return render_template('tools/tools-all.html', tools=tools, positions=positions)
        return render_template('tools/tools-all.html', positions=positions, tools=tools)
    else:
        tools_list = {}
        tools_duplicates = []

        for tool in tools:
            if tool.id_dup not in tools_duplicates:
                tools_list[tool.id] = {
                    'name': tool.name,
                    'description': tool.description,
                    'width': tool.width,
                    'angle': tool.angle,
                    'radius': tool.radius,
                    'company': tool.company,
                    'id_position': tool.id_position,
                    'shelf': tool.shelf,
                    'shelf_type': tool.shelf_type,
                    'quantity': len(Tools.query.filter_by(id_dup=tool.id_dup).all())
                }
                tools_duplicates.append(tool.id_dup)
        print(tools_list)


        return render_template('tools/tools-all.html', positions=positions, tools=tools,
                               send_tools_count=send_tools_count,
                               tools_dead=tools_dead,
                               all_tools_count=all_tools_count,
                               waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/wyslij-zlom/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_wyslij_zlom():
    title = 'WYŚLIJ ZŁOM'
    session['title'] = title
    print(f'title: {session.get("title")}')
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    tools = Tools.query.filter(Tools.id_position!=8).all()
    positions = Position.query.all()
    if request.method == "POST":
        reason = request.form.get('reason')
        tool_id = request.form.getlist('tool')
        position_id = 8
        tools_to_change = request.form.getlist('tool')
        tools_from_db_to_change = []
        print(tools_to_change)
        position_name = name_of_id_position(position_id)
        for tool in tools:
            if str(tool.id) in tools_to_change:
                tool.id_position = 8
                tool.shelf = '0'
                tools_from_db_to_change.append(tool)
                new_history = History(what_happened=f'przeniesiono na ({position_name}), powód: {reason}', tool_id=tool.id,
                                      position_id=position_id)
                db.session.add(new_history)
        print(tools_from_db_to_change)
        try:
            db.session.commit()
            return redirect('/tools/magazyn-done/')
        except:
            return 'wystapil problem'
    else:
        return render_template('tools/tools-send-zlom.html', positions=positions, tools=tools,
                               send_tools_count=send_tools_count, all_tools_count=all_tools_count, tools_dead=tools_dead, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/wyslij-ostrzenie/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_wyslij_ostrzenie():
    title = 'WYŚLIJ DO OSTRZENIA'
    session['title'] = title
    print(f'title: {session.get("title")}')
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    waiting_room_tools = tools_waiting_room()
    tools = Tools.query.filter(Tools.id_position == 9).all()
    positions = Position.query.all()
    if request.method == "POST":
        tool_id = request.form.getlist('tool')
        position_id = 10
        tools_to_change = request.form.getlist('tool')
        tools_from_db_to_change = []
        print(tools_to_change)
        position_name = name_of_id_position(position_id)
        for tool in tools:
            if str(tool.id) in tools_to_change:
                tool.id_position = 10
                tool.shelf = '0'
                new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})', tool_id=tool.id,
                                      position_id=position_id)
                db.session.add(new_history)
                tools_from_db_to_change.append(tool)
        print(tools_from_db_to_change)
        try:
            db.session.commit()
            return redirect('/tools/magazyn-done/')
        except:
            return 'wystapil problem'
    else:
        return render_template('tools/tools-w-ostrzeniu-wyslane.html', positions=positions, tools=tools, title=title,
                               all_tools_count=all_tools_count, tools_dead=tools_dead, send_tools_count=send_tools_count, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/czekaj-ostrzenie/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_czekaj_ostrzenie():
    title = 'DODAJ DO POCZEKALNI'
    session['title'] = title
    print(f'title: {session.get("title")}')
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    tools = Tools.query.filter(Tools.id_position != 9, Tools.id_position != 8, Tools.id_position != 10).all()
    positions = Position.query.all()
    if request.method == "POST":
        tool_id = request.form.getlist('tool')
        position_id = 9
        tools_to_change = request.form.getlist('tool')
        tools_from_db_to_change = []
        print(tools_to_change)
        position_name = name_of_id_position(position_id)
        for tool in tools:
            if str(tool.id) in tools_to_change:
                tool.id_position = 9
                tool.shelf = '0'
                tools_from_db_to_change.append(tool)
                new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})', tool_id=tool.id,
                                      position_id=position_id)
                db.session.add(new_history)
        print(tools_from_db_to_change)
        try:
            db.session.commit()
            return redirect('/tools/magazyn-done/')
        except:
            return 'wystapil problem'
    else:
        return render_template('tools/tools-send-waiting-room.html', positions=positions,
                               tools=tools, waiting_room_tools=waiting_room_tools, all_tools_count=all_tools_count,
                               tools_dead=tools_dead, send_tools_count=send_tools_count)


@tools_routes.route('/tools/ostrzenie-mag/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_action_one():
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    tools = Tools.query.filter(Tools.id_position != 9, Tools.id_position != 8, Tools.id_position != 10).all()
    positions = Position.query.all()
    if request.method == "POST":
        tool_id = request.form.getlist('tool')
        position_id = 9
        tools_to_change = request.form.getlist('tool')
        tools_from_db_to_change = []
        print(tools_to_change)
        position_name = name_of_id_position(position_id)
        for tool in tools:
            if str(tool.id) in tools_to_change:
                tool.id_position = 9
                tool.shelf = '0'
                tools_from_db_to_change.append(tool)
                new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})', tool_id=tool.id,
                                      position_id=position_id)
                db.session.add(new_history)
        print(tools_from_db_to_change)
        try:
            db.session.commit()
        except:
            return 'wystapil problem'
        return redirect('/tools/przekaz-stanowisko/')
    else:
        return render_template('tools/tools-send-waiting-room.html', positions=positions, tools=tools, waiting_room_tools=waiting_room_tools)


@tools_routes.route('/tools/przekaz-stanowisko/', methods=['POST', 'GET'])
@access_required("technolog")
def choose_position():
    title='PRZEKAŻ NA STANOWISKO'
    session['title'] = title
    print(f'title: {session.get("title")}')
    send_tools_count = tools_sent_count()
    tools_dead = tools_dead_count()
    all_tools_count = tools_all_count()
    waiting_room_tools = tools_waiting_room()
    tools = Tools.query.filter_by(id_position = 1).all()
    positions = Position.query.all()
    if request.method == "POST":

        tool_id = request.form.getlist('tool')
        position_id = request.form.getlist('position')[0]
        print(tool_id)
        print(position_id)
        position_name = name_of_id_position(position_id)
        for tool in tools:
            for tool_i_id in tool_id:
                if str(tool.id) == tool_i_id:
                    print('weszlo')
                    tool.id_position = position_id
                    tool.shelf = '0'
                    new_history = History(what_happened=f'przeniesiono na stanowisko({position_name})', tool_id=tool_i_id, position_id=position_id)
                    db.session.add(new_history)

        try:
            db.session.commit()
            return redirect('/tools/magazyn-done/')
        except:
            return 'wystapil problem'
    else:
        return render_template('tools/tools-przekaz-stanowisko.html/', tools=tools, positions=positions, title=title,
                               waiting_room_tools=waiting_room_tools, tools_dead=tools_dead, send_tools_count=send_tools_count, all_tools_count=all_tools_count)


@tools_routes.route('/tools/add-tool/', methods=['POST', 'GET'])
@access_required("technolog")
def tools_form():
    # UPLOAD_FOLDER = './files/'

    if request.method == "POST":
        tools = Tools.query.filter_by(id_position=1).all()
        name = request.form['name'] if not request.form['name'] is None else '-'
        description = request.form['description'] if not request.form['description'] is None else '-'
        width = request.form['width'] + 'mm' if not request.form['width'] is None else '-'
        angle = request.form['angle'] + '°' if not request.form['angle'] is None else '-'
        radius = request.form['radius'] + 'r' if not request.form['radius'] is None else '-'
        company = request.form['company'] if not request.form['company'] is None else '-'
        shelf_type = request.form['shelf-type']
        quantity = int(request.form['quantity'])

        new_tool = Tools(name=name, description=description + " ",
                         width=width, angle=angle, radius=radius,
                         company=company, id_position=1, shelf=0,
                         shelf_type=shelf_type, id_dup=0)
        files = request.files.getlist('file')

        # try:
        db.session.add(new_tool)
        db.session.flush()
        db.session.refresh(new_tool)

        new_tool.id_dup = new_tool.id
        new_tool_dict = {new_tool.id: shelf_type}

        print(new_tool_dict)
        shelves = add_to_magazine_new(new_tool_dict)
        print(shelves)
        shelf = shelves.get(new_tool.id)
        new_tool.shelf = shelf[0]

        new_history = History(what_happened='dodano narzędzie do bazy',
                              tool_id=new_tool.id, position_id=1)

        db.session.add(new_history)

        # db.session.commit()

        for tool in range(quantity-1):
            new_tool_dup = Tools(name=name, description=description + " ",
                     width=width, angle=angle, radius=radius,
                     company=company, id_position=1, shelf=new_tool.shelf,
                     shelf_type=shelf_type, id_dup=new_tool.id)

            db.session.add(new_tool_dup)
            db.session.flush()
            db.session.refresh(new_tool_dup)

            new_history = History(what_happened='dodano narzędzie do bazy',
                                tool_id=new_tool_dup.id, position_id=1)

            db.session.add(new_history)

        db.session.commit()

        directory = f'./files/{new_tool.id_dup}/'
        is_exist = os.path.exists(directory)
        if not is_exist:
            os.makedirs(directory)
        if files[0].filename != '':
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join(directory, filename))

        # except:
        #     return "there was an issue with your orders"

        return render_template('tools/shelf_number.html', shelf_for_new_tool=shelf[0], shelf_type=shelf_type)
    else:
        return render_template('tools/tools-add-tool.html')


@tools_routes.route('/tools/<int:id>', methods=['POST', 'GET'])
@access_required("technolog")
def browse_history(id):
    positions = Position.query.all()
    all_tools = Tools.query.all()
    tool = Tools.query.filter_by(id=id).one()
    tool_dup = tool.id_dup
    tool_dup = Tools.query.filter_by(id_dup=tool_dup, id_position=1).all()
    all_tools_one_company = Tools.query.filter_by(company=tool.company).all()
    percentage = ceil((len(all_tools_one_company)/ len(all_tools))*100)
    history = History.query.filter_by(tool_id=id).all()
    history_count = len(history)-1
    history_added = history[0]
    history_last = history[-1]
    delta = history_last.date - history_added.date
    difference = delta.days
    quantity = len(tool_dup)
    if history_count == 0:
        changes_time = 0
    else:
        changes_time = ceil(difference / history_count)
    route = f'./files/{tool.id_dup}/'
    files = os.listdir(f'./files/{tool.id_dup}/')

    if request.method == 'POST':
        if request.method == 'POST':
            files = request.files.getlist('file')
            directory = f'./files/{tool.id_dup}/'
            is_exist = os.path.exists(directory)
            if not is_exist:
                os.makedirs(directory)
            if files[0].filename != '':
                for file in files:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(directory, filename))
            return redirect(f'/tools/{tool.id}')

    return render_template('tools/tools-tool-history.html', difference=difference, changes_time=changes_time, positions=positions, percentage=percentage, history_added=history_added,
                           history_last=history_last,history_count=history_count,
                           route=route, quantity=quantity, files=files, tool=tool, history=history)


@tools_routes.route('/tools/download/<int:id>/<path:filename>', methods=['GET', 'POST'])
def download(filename, id):
    tool = Tools.query.filter_by(id=id).one()
    abspath = os.path.abspath(f'./files/{tool.id_dup}/{filename}')
    return send_file(abspath, as_attachment=True)

@tools_routes.route('/tools/file/delete/<int:id>/<path:filename>', methods=['GET', 'POST'])
def delete(filename, id):
    tool = Tools.query.filter_by(id=id).one()
    # tool_to_redirect = Tools.query.filter_by(id_dup=id).one()
    abspath = os.path.abspath(f'./files/{tool.id_dup}/{filename}')
    os.remove(abspath)
    return redirect(f'/tools/{tool.id}')

@tools_routes.route('/tools/change/<int:id>', methods=['GET', 'POST'])
def change(id):
    tool = Tools.query.filter_by(id=id).one()
    tools_dup = Tools.query.filter_by(id_dup=id).all()
    count_tools_dup = len(tools_dup)
    if request.method == 'POST':
        name = request.form['name'] if not request.form['name'] is None else '-'
        description = request.form['description'] if not request.form['description'] is None else '-'
        width = request.form['width'] + 'mm' if not request.form['width'] is None else '-'
        angle = request.form['angle'] + '°' if not request.form['angle'] is None else '-'
        radius = request.form['radius'] + 'r' if not request.form['radius'] is None else '-'
        company = request.form['company'] if not request.form['company'] is None else '-'

        for tool_x in tools_dup:
            tool_x.name = name
            tool_x.description = description
            tool_x.width = width
            tool_x.angle = angle
            tool_x.radius = radius
            tool_x.company = company
            db.session.commit()
        return redirect('/tools/magazyn-done')
    else:
        return render_template('tools/tools-change.html', tool=tool, count_tools_dup=count_tools_dup)

@tools_routes.route('/tools/add-quantity/<int:id>', methods=['GET', 'POST'])
def change_quantity(id):
    tool = Tools.query.filter_by(id=id).one()
    tools_dup = Tools.query.filter_by(id_dup=id).all()
    count_tools_dup = len(tools_dup)
    if request.method == 'POST':
        quantity = int(request.form['quantity'])
        name = tool.name
        description = tool.description
        width = tool.width
        angle = tool.angle
        radius = tool.radius
        company = tool.company
        shelf_type = tool.shelf_type

        if tool.shelf == 0:
            for tool_dup in tools_dup:
                if tool_dup.shelf != 0:
                    shelf = tool_dup.shelf
        else:
            shelf = tool.shelf

        id_dup = tool.id_dup

        for x in range(quantity):
            new_tool = Tools(name=name, description=description + " ",
                             width=width, angle=angle, radius=radius,
                             company=company, id_position=1, shelf=shelf,
                             shelf_type=shelf_type, id_dup=id_dup)

            db.session.add(new_tool)
            db.session.flush()
            db.session.refresh(new_tool)

            new_history = History(what_happened='dodano narzędzie do bazy',
                                  tool_id=new_tool.id, position_id=1)

            db.session.add(new_history)

        db.session.commit()

        return render_template('tools/shelf_number.html', shelf_for_new_tool=shelf, shelf_type=shelf_type)
    else:
        return render_template('tools/tools-add-quantity.html', tool=tool, count_tools_dup=count_tools_dup)