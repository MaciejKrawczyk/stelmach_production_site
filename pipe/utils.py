from flask import session, redirect, url_for
from pipe.models import Tools, Role
from pipe import db


def access_required(role):
    """decorator for limiting access to specific routes"""
    def decorator_function(original_function):
        def wrapper(*args, **kwargs):
            if role in session.get('role', 'brak'):
                print("username:", session.get("username", "logged out"))
                print("role:", session.get("role", "brak"))
                return original_function(*args, **kwargs)
            else:
                return redirect(url_for('login'))
        wrapper.__name__ = original_function.__name__
        return wrapper
    return decorator_function


def add_to_magazine_new(tools_to_change: dict):
    """returns dictionary { tool_id: (shelf, shelf_type), },
    to change global number of shelf types,
    change first two variables
    Input is the dictionary { tool_id: shelf_type }"""
    AMOUNT_OF_SMALL_SHELVES = 180
    AMOUNT_OF_BIG_SHELVES = 100
    ALL_SMALL_SHELVES_AVAILABLE = [x for x in range(1, AMOUNT_OF_SMALL_SHELVES)]
    ALL_BIG_SHELVES_AVAILABLE = [x for x in range(1, AMOUNT_OF_BIG_SHELVES)]
    tools = Tools.query.filter_by(id_position=1).all()
    new_tools_small = []
    new_tools_big = []
    shelves_occupied_small = []
    shelves_occupied_big = []
    returned_dict = {}
    for tool in tools:
        if tool.shelf_type == 'big':
            shelves_occupied_big.append(tool.shelf)
        else:
            shelves_occupied_small.append(tool.shelf)
    for id, shelf_type in tools_to_change.items():
        if shelf_type == 'small':
            new_tools_small.append(id)
        else:
            new_tools_big.append(id)
    all_shelves_available_now_big = [x for x in ALL_BIG_SHELVES_AVAILABLE if x not in shelves_occupied_big]
    all_shelves_available_now_small = [x for x in ALL_SMALL_SHELVES_AVAILABLE if x not in shelves_occupied_small]
    i = 0
    for x in new_tools_small:
        returned_dict[x] = (all_shelves_available_now_small[i], 'small')
        i = i + 1
    i = 0
    for x in new_tools_big:
        returned_dict[x] = (all_shelves_available_now_big[i], 'big')
        i = i + 1
    return returned_dict


def add_to_magazine(tools_to_change: dict):
    """returns dictionary { tool_id: (shelf, shelf_type), },
    to change global number of shelf types,
    change first two variables
    Input is the dictionary { tool_id: shelf_type }"""
    AMOUNT_OF_SMALL_SHELVES = 580
    AMOUNT_OF_BIG_SHELVES = 500
    ALL_SMALL_SHELVES_AVAILABLE = [x for x in range(1, AMOUNT_OF_SMALL_SHELVES)]
    ALL_BIG_SHELVES_AVAILABLE = [x for x in range(1, AMOUNT_OF_BIG_SHELVES)]
    tools = Tools.query.filter_by(id_position=1).all()
    new_tools_small = []
    new_tools_big = []
    shelves_occupied_small = []
    shelves_occupied_big = []
    id_dup_small = []
    id_dup_big = []
    returned_dict = {}
    for tool in tools:
        if tool.shelf_type == 'big':
            shelves_occupied_big.append(tool.shelf)
        else:
            shelves_occupied_small.append(tool.shelf)
    for id, shelf_type in tools_to_change.items():
        if shelf_type == 'small':
            new_tools_small.append(id)
            id_dup_small.append(Tools.query.filter_by(id=id, shelf_type='small').one().id_dup)
        else:
            id_dup_big.append(Tools.query.filter_by(id=id, shelf_type='big').one().id_dup)
            new_tools_big.append(id)
    all_shelves_available_now_big = [x for x in ALL_BIG_SHELVES_AVAILABLE if x not in shelves_occupied_big]
    all_shelves_available_now_small = [x for x in ALL_SMALL_SHELVES_AVAILABLE if x not in shelves_occupied_small]

    inserted_tools_dup_id = {}
    i = 0
    for x in new_tools_small:
        # check if there are duplicates of tool
        tool_small = Tools.query.filter_by(id=x).one()
        id_dup_of_tool = tool_small.id_dup
        tools_dup = Tools.query.filter_by(id_dup=id_dup_of_tool, id_position=1).all()
        tools_dup_quantity = len(tools_dup)
        print(tools_dup_quantity)
        if tool_small.id_dup in inserted_tools_dup_id:
            returned_dict[x] = (inserted_tools_dup_id[tool_small.id_dup], 'small')
            continue
        if tools_dup_quantity >= 1:
            returned_dict[x] = (tools_dup[-1].shelf, 'small')
            inserted_tools_dup_id[tool_small.id_dup] = returned_dict[x][0]
            continue
        returned_dict[x] = (all_shelves_available_now_small[i], 'small')
        inserted_tools_dup_id[tool_small.id_dup] = returned_dict[x][0]
        print(inserted_tools_dup_id)
        i = i + 1
    i = 0
    inserted_tools_dup_id.clear()
    for x in new_tools_big:
        # check if there are duplicates of tool
        tool_big = Tools.query.filter_by(id=x).one()
        id_dup_of_tool = tool_big.id_dup
        tools_dup = Tools.query.filter_by(id_dup=id_dup_of_tool, id_position=1).all()
        tools_dup_quantity = len(tools_dup)
        # print(tools_dup_quantity)
        if tool_big.id_dup in inserted_tools_dup_id:
            print(tool_big.id_dup)
            # print(inserted_tools_dup_id)
            returned_dict[x] = (inserted_tools_dup_id[tool_big.id_dup], 'big')
            continue
        if tools_dup_quantity >= 1:
            returned_dict[x] = (tools_dup[-1].shelf, 'big')
            inserted_tools_dup_id[tool_big.id_dup] = returned_dict[x][0]
            continue
        returned_dict[x] = (all_shelves_available_now_big[i], 'big')
        inserted_tools_dup_id[tool_big.id_dup] = returned_dict[x][0]
        print(inserted_tools_dup_id)
        i = i + 1
    return returned_dict


def tools_sent_count():
    tools = Tools.query.filter_by(id_position=10).all()
    return len(tools)


def tools_all_count():
    tools = Tools.query.filter(Tools.id_position != 9, Tools.id_position != 8, Tools.id_position != 10).all()
    return len(tools)


def tools_dead_count():
    tools = Tools.query.filter_by(id_position=8).all()
    return len(tools)


def tools_waiting_room():
    tools = Tools.query.filter_by(id_position=9).all()
    return len(tools)


def database_default_add():
    # """ always after server start """
    #
    # roles = Role.query.all()
    # print(roles)
    # list_of_roles = [x.name for x in roles]
    # print(roles)
    #
    # roles_dict = {
    #     1: 'admin',
    #     2: 'technolog',
    #     3: 'pracownik',
    #     4: 'kierownik',
    # }
    #
    # for key, value in roles_dict:
    #     if value not in list_of_roles:
    #         new_role = Role(name=value, id=key)
    #         db.session.add(new_role)
    # db.session.commit
    pass