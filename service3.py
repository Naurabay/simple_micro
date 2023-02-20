import time
from sql_queries import create_table, delay

create_table()

if __name__ == '__main__':
    while True:
        delay()
        print("We're sorry for the delay")
        time.sleep(20)
