import psycopg2

from arrivals import Arrivals

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS nurai_airport_arrivals (
        id SERIAL PRIMARY KEY,
        destination VARCHAR(20) NOT NULL,
        flight VARCHAR(20) NOT NULL,
        airline VARCHAR(50) NOT NULL,
        terminal INTEGER,
        std DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'On Time'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_flight(arrival: Arrivals):
    query = """
    INSERT INTO nurai_airport_arrivals (destination, flight, airline, terminal)
    VALUES (%s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (arrival.destination, arrival.flight, arrival.airline, arrival.terminal))
    conn.commit()


def start_boarding():
    query = "UPDATE nurai_airport_arrivals SET  status='Boarding...' WHERE terminal=2;"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def delay():
    query = "UPDATE nurai_airport_arrivals SET status='Delayed' WHERE destination='Dubai' or destination = 'Warsaw';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def delete_arrived():
    query = "DELETE FROM nurai_airport_arrivals WHERE status = 'On Time';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def get_arrivals() -> list[Arrivals]:
    query = "SELECT * FROM nurai_airport_arrivals;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [Arrivals(
        id=arrival[0],
        destination=arrival[1],
        flight=arrival[2],
        airline=arrival[3],
        terminal=arrival[4],
        std=arrival[5],
        status=arrival[6],
    ) for arrival in cursor.fetchall()]
