import time
from sql_queries import create_table, start_boarding

create_table()

if __name__ == '__main__':
    while True:
        start_boarding()
        print("Boarding has  started ")
        time.sleep(20)
