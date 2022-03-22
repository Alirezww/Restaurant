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
        f.writelines(json.dumps(data, indent=5))
        print('it was successfully.')


def load_items(file_path):
    with open(file_path, 'r') as f:
        items = json.loads(f.read())
    return items


def calculate(order_dict):
    for element in order_dict:
        item = Item.search_by_id(uuid=element['item_id'])
        if item is not None:
            result = int(item.price) * int(element['item_count'])
            return result
        return item
