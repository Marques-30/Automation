import sys
import cx_Oracle
import csv
import subprocess
from xlrd import open_workbook
import xlrd
import getpass
import time

header = ['Database', 'Schema', 'Password', 'Validation']

class Arm(object):
    def __init__(self, SCHEMA, PASSWORD, DB):
        self.SCHEMA = SCHEMA
        self.PASSWORD = PASSWORD
        self.DB = DB

    def __iter__(self):
       return self

    def __str__(self):
        return("\n"
               "  SCHEMA = {0}\n"
               "  PASSWORD = {1}\n"
               "  Database = {2}\n"
               .format(self.SCHEMA, self.PASSWORD, self.DB))

wb = open_workbook('Schema excel.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    items = []
    rows = []
    with open("Schema Report.csv", 'w') as out_file:
	        writer=csv.writer(out_file, lineterminator='\n')
	        writer.writerow((header))
	        count = 0
		while count < number_of_rows:
			    for row in range(1, number_of_rows):
			        values = []
			        for col in range(number_of_columns):
			            value  = (sheet.cell(row,col).value)
			            try:
			                value = str(int(value))
			            except ValueError:
			                pass
			            finally:
			                values.append(value)
			        item = Arm(*values)
			        items.append(item)
				print item
				print count
				ID=item.SCHEMA
				Database=item.DB
				password=item.PASSWORD
				try :
					connection = cx_Oracle.connect(ID+'/'+password+'@'+Database.upper())
					cursor = connection.cursor()
					field = "Pass"
					cursor.close()
				except IOError:
				 	field = "Fail"
				 	cursor.close()
				except cx_Oracle.DatabaseError:
					field = "Fail"
				body = [Database, ID, password, field]
				if ID is not None:
		        		writer.writerow((body))
				count += 1
		print "\n\n    All Schemas have been successful tested "
		time.sleep(10)