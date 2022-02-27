from database.dbcon import PostgresConnection
import pandas as pd


class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query4 = "select sum(cast(fact.total_price as double precision)) " \
                 "from ecomdb_star_schema.fact_data fact " \
                 "join ecomdb_star_schema.time_dim time on time.time_key=fact.time_key " \
                 "where (cast(time.year as integer))=2015 "
        cur.execute(query4)
        result = cur.fetchall()[0][0]

        return {"total_sales": result}


if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)