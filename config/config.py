#Database Connection utilities
username='root'
pswrd='root'
hostname='localhost'
dbname='studentreport'

#insert query
insertrecord="insert into studreport values(%s,%s,%s,%s)"

#select Query
selectrecord="select * from studreport"
searchrecord="select * from studreport where studid='{0}'"


#delete query
deleterecord="delete from studreport where studid='{0}'"




