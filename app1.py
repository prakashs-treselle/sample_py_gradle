from flask import Flask, url_for, request, json,Response, jsonify, render_template
 
import re
import sys
import time
from DBUtilities.DBUtil import *
from ExpectingResult.Expectation import *
from DBConnection.DBConnection import *
from config.config import *

app = Flask(__name__)

 
 
dbutil=DBUtilities()
expect=ExpectedResult()
'''
        @ This service gee the details and return the expected result in json format
'''
@app.route('/studentdetails', methods=['GET'])
def getDetails():
        
        dict1={'studid':None,'studname':None,'maths':None,'physics':None,'chemistry':None,'computer':None}
        url_studid=request.args.get('studid')
        url_studname=request.args.get('studname')
        url_maths=request.args.get('maths')
        url_physics=request.args.get('physics')
        url_chemistry=request.args.get('chemistry')
        url_computer=request.args.get('computer')
        dict1={'studid':url_studid,'studname':url_studname,'maths':url_maths,'physics':url_physics,'chemistry':url_chemistry,'computer':url_computer}
        res=expect.expectedResult(dict1,url_studid,url_studname)
        return res


'''
        @ This servcice used to view the record for the partcular range of values according ot start and end limit
'''
@app.route('/range',methods=['GET'])
def viewRange():
        url_start=request.args.get('start')
        url_end=request.args.get('end')
        res=dbutil.viewRange(url_start,url_end)
        return res


'''
        @ This service return the number of rows from the given start row
'''
@app.route('/limit',methods=['GET'])
def recordLimit():
        url_rows=request.args.get('rows')
        url_start=request.args.get('start')
        res=dbutil.recordLimit(url_rows,url_start)
        return res

'''
        @ This service return the data for the particular field
'''
@app.route('/field',methods=['GET'])        
def particularField():
        
        url_field=request.args.get('field')
        res=dbutil.particularField(url_field)
        return res


'''
    # Execution begins here
'''
if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0',port=7010)
