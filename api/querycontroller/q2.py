from database.dbcon import PostgresConnection
import pandas as pd
class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        query2 = " select t.trans_type, sum(cast(fact.total_price as double precision)) " \
                 " from ecomdb_star_schema.fact_data fact " \
                 "join ecomdb_star_schema.trans_dim t on t.payment_key = fact.payment_key " \
                 "GROUP BY t.trans_type "
        cur.execute(query2)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['transaction-type', 'sales'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)