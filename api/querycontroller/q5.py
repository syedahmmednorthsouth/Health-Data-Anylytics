from database.dbcon import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query5 = "select sum(cast(fact.total_price as double precision)) " \
                 "from ecomdb_star_schema.fact_data fact " \
                 "join ecomdb_star_schema.store_dim s on s.store_key = fact.store_key " \
                 "join ecomdb_star_schema.time_dim time on time.time_key=fact.time_key " \
                 "where  s.division = 'BARISAL' and (cast(time.year as integer))=2015 "
        cur.execute(query5)
        result = cur.fetchall()[0][0]

        return {"total_sales": result}


if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)