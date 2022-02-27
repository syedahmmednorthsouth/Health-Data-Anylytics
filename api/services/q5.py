from flask import jsonify
from flask.views import MethodView
from querycontroller.q5 import Query5

class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

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
        result = self.q5.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)

    # def post(self):

    # def delete(self):