import psycopg2

class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb1",
                                           user = "postgres",
                                           password = "12345",
                                           host = "127.0.0.1",
                                           port = "5432")
    def getConnection(self):
        print("successfully connected to database")
        return self.connection
# conn = PostgresConnection().getConnection()