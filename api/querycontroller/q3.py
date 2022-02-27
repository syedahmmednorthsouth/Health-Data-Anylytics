from database.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):


        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query3 = "select sum(cast(fact.total_price as double PRECISION)) " \
                 "from ecomdb_star_schema.fact_data fact " \
                 "join ecomdb_star_schema.store_dim s on s.store_key = fact.store_key " \
                 "where s.division = 'BARISAL' "
        cur.execute(query3)
        result = cur.fetchall()[0][0]

        return { "total_sales": result}

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)