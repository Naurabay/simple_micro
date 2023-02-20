import time
from sql_queries import create_table, delete_arrived

create_table()

if __name__ == '__main__':
    while True:
        delete_arrived()
        print("Deleted")
        time.sleep(37)
