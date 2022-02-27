from flask import jsonify
from flask.views import MethodView
from querycontroller.q3 import Query3

class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        '''
        Get the data of querycontroller 1
        :return: [{
                  ‘division’: “Dhaka”,
                  'total_sales’: 1000
                  },
                 {
                  ‘division’: “Rangpur”,
                  ‘total_sales’: 1000
                 },....
                ]
        '''
        result = self.q3.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):

    # def delete(self):