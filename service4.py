import time
from sql_queries import create_table, get_arrivals

create_table()

if __name__ == '__main__':
    while True:
        arrivals = get_arrivals()
        print("-------------------- >>")
        for arrival in arrivals:
            print(arrival)
        print("-------------------- <<")
        time.sleep(5)
