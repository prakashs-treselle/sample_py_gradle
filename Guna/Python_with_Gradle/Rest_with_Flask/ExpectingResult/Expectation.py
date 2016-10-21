from DBConnection.DBConnection import *
from Calculation.Calculate import *
from Validation.Validating import *
from flask import json
from flask import jsonify
db=DBConnection()
evaluate=Evaluate()
validate=Validating()
class ExpectedResult:
    def expectedResult(self,dict1,url_studid,url_studname):
            con=db.getConnection()
            cursor=con.cursor()
            cursor.execute("select * from studreport5 where studid='{0}' and studname='{1}'".format(url_studid,url_studname))
            output=cursor.fetchall()
            
            for row in output:
                    studid=row[0]
                    studname=row[1]
                    maths=row[2]
                    physics=row[3]
                    chemistry=row[4]
                    computer=row[5]
                    total=row[6]
                    average=row[7]
                    cutoff=row[8]

            for key,value in dict1.items():
                if dict1['maths']==None:
                    dict1['maths']=maths
                if dict1['physics']==None:
                    dict1['physics']=physics
                if dict1['chemistry']==None:
                    dict1['chemistry']=chemistry
                if dict1['computer']==None:
                    dict1['computer']=computer
                    
            marks_status=validate.validateMarks(dict1['maths'],dict1['physics'],dict1['chemistry'],dict1['computer'])
            studid_status=validate.validateId(dict1['studid'])
            studname_status=validate.validateName(dict1['studname'])
            if studid_status==True and studname_status==True and marks_status==False:
                return validate.invalidMarks()
            elif studid_status==True and studname_status==False and marks_status==True:
                return validate.invalidName()
            elif studid_status==True and studname_status==False and marks_status==False:
                return validate.invalidError()
            elif studid_status==False and studname_status==False and marks_status==False:
                return validate.invalidError()
            elif studid_status==True and studname_status==True and marks_status==True:
                 
                exptotal=evaluate.totalmarks(dict1['maths'],dict1['physics'],dict1['chemistry'],dict1['computer'])
                expaverage=exptotal/8
                expcutoff=evaluate.cutoff(dict1['maths'],dict1['physics'],dict1['chemistry'])
                expgradevalue=evaluate.findgrade(expaverage)
                
                response={
                        'database':
                        {
                                   'studid':studid,
                                   'studname':studname,
                                    'maths':maths,
                                    'physics':physics,
                                    'chemistry':chemistry,
                                    'computer':computer,
                                    'total':total,
                                   'average':average,
                                   'cutoff':cutoff
                        },
                        'expected':
                        {
                                 'studid':studid,
                                 'studname':studname,
                                'maths':dict1['maths'],
                                  'physics':dict1['physics'],
                                 'chemistry':dict1['chemistry'],
                                'computer':dict1['computer'],
                                'total':exptotal,
                                'average':expaverage,           
                                'grade':expgradevalue,
                                'cutoff':expcutoff
                        }
                        }
                res=jsonify(response)
            
            
            return res
