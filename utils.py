import json
from menu import Item
from constanst import SUPERVISOR_CREDENTIAL


def check_credential(user_credential):
    if len(user_credential) > 2:
        check_username = bool(SUPERVISOR_CREDENTIAL[0]['username'] == user_credential[1])
        check_password = bool(SUPERVISOR_CREDENTIAL[0]['password'] == user_credential[2])
        return check_password, check_username
    return False


def save_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.writelines(json.dumps(data))
        print('it was successfully.')


def calculate(order_dict):
    item = Item.search_by_id(uuid=order_dict['uuid'])
    if item is not None:
        result = item.price * order_dict['count']
        return result
    return item
