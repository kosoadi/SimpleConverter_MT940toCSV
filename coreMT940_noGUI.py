#!/usr/bin/env python3

from mt940 import MT940
import csv
import os
import argparse

"""
a simple MT940 converter without GUI
How to use:
	python coreMT940_noGUI.py [input file]

Result will be generated in the same folder [input file]+.CSV
"""

# define argparse for input
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input the MT940 to be converted", type=str)

args = parser.parse_args()
# get the input file
input_file = args.input_file
# define output filename, format: [input file name].csv
output_file = args.input_file + ".csv"

# parse the file to MT940 object
# reference https://pypi.org/project/mt940/
mt940 = MT940(input_file)
# get 1 MT940 statement
statement = mt940.statements[0]

# get the account no
account_no = statement.account
# get the account info
account_info = statement.information

# get the starting balance object
start_balance = statement.start_balance
# get the starting balance date
start_balance_date = start_balance.date
# get the starting balance amount
start_balance_amount = start_balance.amount
# get the starting balance currency
start_balance_currency = start_balance.currency

# get the ending balance object
end_balance = statement.end_balance
# get the ending balance date
end_balance_date = end_balance.date
# get the ending balance amount
end_balance_amount = end_balance.amount
# get the ending balance currency
end_balance_currency = end_balance.currency

"""
# print(s) for testing purpose
print account_no
print account_info
print start_balance
print start_balance_date
print start_balance_amount
print start_balance_currency
print end_balance
print end_balance_date
print end_balance_amount
print end_balance_currency
"""

# write the result into a CSV file
# reference https://realpython.com/python-csv/
with open(output_file, mode="w") as converted_MT940:
	# initiate writer
	writer = csv.writer(converted_MT940, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
	# write file headers
	writer.writerow(["account no", account_no])
	writer.writerow(["sequence no", account_info])
	writer.writerow(["currency", start_balance_currency])
	writer.writerow(["from date", start_balance_date])
	writer.writerow(["to date", end_balance_date])
	writer.writerow(["starting balance", start_balance_amount])
	writer.writerow(["ending balance", end_balance_amount])
	writer.writerow("")
	#writer.writerow(["TEST"])
	
	# write content headers
	writer.writerow(["no",
		"transaction id/type", 
		"effective date", 
		"booking date", 
		"amount", 
		"transaction reference",
		"additional data",
		"description"
		])
	
	# write transaction(s)
	row_no = 1 
	for txn in statement.transactions:
		writer.writerow([row_no,
			txn.id, 
			txn.date, 
			txn.booking, 
			txn.amount, 
			txn.reference,
			txn.additional_data,
			txn.description
			])
		row_no += 1
	
	
	
	
	
	
	
	
	
	
	
	
	