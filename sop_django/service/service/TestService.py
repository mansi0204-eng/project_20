
from service.models import Test
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection



class TestService(BaseService):

    def get_model(self):
        return Test

    def search(self, params):
        pageNo = (params['pageNo'] - 1) * self.pageSize
        sql = "select * from sos_test where 1=1"
        val = params.get("userName", None)
        if DataValidator.isNotNull(val):
            sql += " and userName like '" + val + "%%' "
        sql += " limit %s,%s"
        cursor = connection.cursor()
        print("----------", sql, pageNo, self.pageSize)
        params['index'] = ((params['pageNo'] - 1) * self.pageSize) + 1
        cursor.execute(sql, [pageNo, self.pageSize])
        result = cursor.fetchall()
        columnName = ('id', 'firstName', 'lastName', 'userName')
        res = {
            "data": [],
            "MaxId": 1,
        }
        count = 0
        res["index"] = params["index"]
        for x in result:
            params['MaxId'] = x[0]
            res['data'].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        print("MMMMMMMMMM", params.get("MaxId"))
        return res



