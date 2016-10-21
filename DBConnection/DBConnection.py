'''
@ Establishihg the database conection
@ To create a conetion
@ To close the conection
'''
import mysql.connector

from config.config import  *

class DBConnection(object):

    #Establishing the connection
    def getConnection(self):
        con = mysql.connector.connect(user=username,password=pswrd,host=hostname,database=dbname)
        return con

    #closing the conection
    def closeConnection(self,con):
        con.commit()
        con.close()
        
 
