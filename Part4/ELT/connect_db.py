import psycopg2


def connect_db():
	return psycopg2.connect(host='localhost', port='8731',
                            database='sfo', user='sfo', password='sfo')