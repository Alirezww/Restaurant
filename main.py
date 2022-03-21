import sys
from user import Supervisor
from utils import check_credential, save_to_file
from constanst import ITEM_JSON_FILE_PATH

if __name__ == '__main__':
    if check_credential(sys.argv):
        item = Supervisor.create_item()
        save_to_file(ITEM_JSON_FILE_PATH, Supervisor.item_data())
