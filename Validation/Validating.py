'''
    #This class validate the Email id whether it is a valid email id or not
'''

import re
import logging
from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify
from DBConnection.DBConnection import *
 
db=DBConnection()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
class Validating:

    # method to check the whether the given input is a valid emailid or not
    def validateId(self,studid):
        match = re.match("^[0-9]*$", studid)
        if match==None:
             logger.warning( "studid is Invalid")
             logger.warning( "***Please enter the valid  Id***")
              
             return False
        else:
             logger.info( "studid is valid")
             return True

    def validateName(self,studname):
        match = re.match("^[A-Za-z]*$", studname)
        if match==None:
            logger.warning( "studname  is Invalid")
            logger.warning( "***Please enter the valid user name***")
            return False
        else:
            logger.info("stud name is valid")
            return True

    def validateMarks(self,maths,physics,chemistry,computer):
            mathsmatch = re.match("^[0-9]*$", str(maths))
            physicsmatch = re.match("^[0-9]*$", str(physics))
            chemistrymatch = re.match("^[0-9]*$", str(chemistry))
            computermatch = re.match("^[0-9]*$", str(computer))
            if mathsmatch==None or physicsmatch==None or chemistrymatch==None or computermatch==None:
                logger.warning( " maths marks is Invalid")
                logger.warning( "***Please enter the valid marks***")
                return False
        
            if mathsmatch and physicsmatch and chemistrymatch and computermatch:
                logger.warning( " maths marks is valid")
                logger.warning( "***valid***")
                return True

            else:
                logger.info("some of marks is invalid")
                return False
        
        
          
    def invalidName(self):
        invalidname = {
                'status': 'false',
                'message': 'plese give the username in Alphabets ',
                'error': 'Invalid User Name',
                'responce':'User name should not be in alphabeticcharacter'                
        
                }
        responce = jsonify(invalidname)
        return responce
        
    def invalidId(self):
        invalidemailid = {
                'status': 'false',
                'message': 'plese give the valid student id ',
                'error': 'Invalid studentid',
                'responce':'student id shound be in number  ',
                'sample':'eg. 101'
        
                }
        responce = jsonify(invalidemailid)
        return responce
    def invalidMarks(self):
        invalidemailid = {
                'status': 'false',
                'message': 'plese enter the valid marks ',
                'error': 'Invalid marks',
                'responce':'maximum mark is 200',
                'sample':'67,190,78'
        
                }
        responce = jsonify(invalidemailid)
        return responce
    def invalidError(self):
        invalidname = {
                'status': 'false',
                'message': 'plese give the Correct student name and student id ',
                'error': 'Invalid student name and student id',
                'responce':'student name should not be in alphabeticcharacter ',
                'sample':'maximum marks is 200'
        
                }
        responce = jsonify(invalidname)
        return responce


    
    

    
        
         
