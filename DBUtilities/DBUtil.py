'''

    @ Dbutilities class to insert and retrive the data from Daatabase
    @ fetching the data from the given range of values
    @ fetching the data according to the start and the given values between the range
'''

from DBConnection.DBConnection import *
from flask import json,jsonify
from collections import OrderedDict

db=DBConnection()
class DBUtilities:

    #This method fetch the data according to the start and end value in the given range
    def viewRange(self,start,end):
        con=db.getConnection()
        cursor=con.cursor()
        cursor.execute("select * from studreport5 limit {0},{1}".format(start,end))
        output=cursor.fetchall()
        db.closeConnection(con)
        objects_list = []
        for row in output:
                details= {
                    'STUDID': row[0],
                    'STUDNAME': row[1],
                    'MATHS': row[2],
                    'PHYSICS': row[3],
                    'CHEMISTRY': row[4],
                    'COMPUTER': row[5],
                    'TOTAL': row[6],
                    'AVERAGE'  : row[7],                  
                    'CUTOFF': row[8],
                    'GRADE': row[9],
                     }
                objects_list.append(details)
                resp=jsonify(objects_list)
        return resp
    #This method fetch the data from the database according to the number of rows given and the start value
    def recordLimit(self,rows,start):
        con=db.getConnection()
        cursor=con.cursor()
        cursor.execute("select * from studreport5 limit {0} OFFSET {1}".format(rows,start))
        output=cursor.fetchall()
        db.closeConnection(con)
        objects_list = []
        for row in output:
                details= {
                    'STUDID': row[0],
                    'STUDNAME': row[1],
                    'MATHS': row[2],
                    'PHYSICS': row[3],
                    'CHEMISTRY': row[4],
                    'COMPUTER': row[5],
                    'TOTAL': row[6],
                    'AVERAGE'  : row[7],                  
                    'CUTOFF': row[8],
                    'GRADE': row[9],
                     }
                objects_list.append(details)
                resp=jsonify(objects_list)
        return resp
    #This method used to retrive tha data from the particular given field
    def particularField(self,field):
        con=db.getConnection()
        cursor=con.cursor()
         
        cursor.execute("select {0},{1} from studreport5".format("studid",field))
        output=cursor.fetchall()
        db.closeConnection(con)
        objects_list = []
        for row in output:
            studid=row[0]
            chemistry=row[1]
            details={
                 'studid':studid,
                 field:chemistry
                }
            objects_list.append(details)
            resp=jsonify(objects_list)
        return resp
     
