import sys

from order import Order
from user import Supervisor
from utils import check_credential, save_to_file, load_items
from saloon import Table
from constanst import ITEM_JSON_FILE_PATH, TABLE_JSON_FILE_PATH
from menu import Item
from ordering import intro

if __name__ == '__main__':
    if check_credential(sys.argv):
        _ = [Item(**d) for d in load_items(ITEM_JSON_FILE_PATH)]
        t = [Table(**d) for d in load_items(TABLE_JSON_FILE_PATH)]

        intro()
