import pyodbc
connection_data=pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % 
	('SQL Server', '172.31.23.171', 'salesiq_IC_processing_DEV', 'salesiq_IC_processing_dev', 'salesiq@123' ) )
cursor_data = connection_data.cursor()
query='select top 1 * from  abcd'
cursor_data.execute(query)
print('s')

for i in cursor_data:
	print(i[5])