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

@app.route('/range',methods=['GET'])
def viewRange():
        url_start=request.args.get('start')
        url_end=request.args.get('end')
        res=dbutil.viewRange(url_start,url_end)
        return res
@app.route('/limit',methods=['GET'])
def recordLimit():
        url_rows=request.args.get('rows')
        url_start=request.args.get('start')
        res=dbutil.recordLimit(url_rows,url_start)
        return res
@app.route('/field',methods=['GET'])        
def particularField():
        
        url_field=request.args.get('field')
        res=dbutil.particularField(url_field)
        return res

@app.route('/fieldlist',methods=['GET'])        
def fieldList():
        fieldlist=[]
        fielddict={'maths_marks':None,'physics_marks':None,'chemistry_marks':None,'computer_marks':None}
        maths_marks=request.args.get('maths')
        physics_marks=request.args.get('physics')
        chemistry_marks=request.args.get('chemistry')
        computer_marks=request.args.get('computer')
        
        fielddict={'maths_marks':maths_marks,'physics_marks':physics_marks,'chemistry_marks':chemistry_marks,'computer_marks':computer_marks}
        if fielddict['maths_marks']is not None:
                fieldlist.append(maths_marks)
        elif fielddict['physics_marks']is not None:
                fieldlist.append(physics_marks)
        elif fielddict['chemistry_marks']is not None:
                fieldlist.append(chemistry_marks)
        elif fielddict['computer_marks']is not None:
                fieldlist.append(computer_marks)
        
        res=dbutil.fieldList(fieldlist)       
        
        return res
'''
    # Execution begins here
'''
if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0',port=7010)
