# Author: Oran Avivi
# Written: April 2021

from os import path # to cheack if directories exist
from operator import itemgetter # to sort the list
import numpy as np # numerical operation library
from collections import deque # import double ended queues
import json # json library
import csv # import a csv file

# output file check
if path.exists("data2.json"): # check if data2.json exists
    jsondata = open('data2.json', 'w') #if it does, write to it
else:
    jsondata = open('data2.json', 'x') # if it doesnt, create it

# row calculator - total/valid row calculator
with open('data.csv') as datafile: # with the file name 'data.csv', new line delimiter is ''
    datareader = csv.reader(datafile, delimiter=',') # create a data reader for data.csv. variables delimitted by ',' 
    datawriter = csv.writer(datafile, delimiter=',') # create a data wirter for data.csv
    
    validrows = 0 # declare initial number of rows with valid profits
    totalrows = 0 # declare initial number of valid and invalid rows
    validrowvalues = [] # declare array to store invalid profit values
    columnnames = [] # declare empy array to store column names
    columns = 0 # declare initial known number or columns
    rowdataobj = {} # initialize data dictionary to be exported to json

    jsondata.write('{\n "validprofitdata": [\n  ') # format start of data2.json file where we export data
    for row in datareader: # for loop to count number of valid profit lines
        if totalrows == 0: # read titles
            columns = np.size(row) # get size of row (number of titles/columns)
            columnnames = row # get column titles
            totalrows += 1
        elif totalrows == 1: # 1st row of data
            try: # try converting string to float
                float(row[columns - 1])
                # convert 
                validrowvalues.append(row) # save valid row
                validrows += 1 # increment valid rows
                totalrows += 1 # increment total rows
                rowdict = {columnnames[i]:row[i] for i in range(len(columnnames))} # create dictionary from row data
                # first line has no leading comma
                json.dump(rowdict, jsondata) # export data to data2.json file
                jsondata.write('\n')
            except ValueError: # if cant convert, profit is invalid format
                totalrows += 1 # increment only total rows
                # could make an "invalidrows" variable but would be redundant
        else: # all other rows
            try: # try converting string to float
                float(row[columns - 1])
                # convert 
                validrowvalues.append(row) # save valid row
                validrows += 1 # increment valid rows
                totalrows += 1 # increment total rows
                rowdict = {columnnames[i]:row[i] for i in range(len(columnnames))} # create dictionary from row data
                jsondata.write('  ,') # leading comma
                json.dump(rowdict, jsondata) # export data to data2.json file
                jsondata.write('\n')
            except ValueError: # if cant convert, profit is invalid format
                totalrows += 1 # increment only total rows
                # could make an "invalidrows" variable but would be redundant
    jsondata.write(']\n}') # format end of data2.json file

print("There are " + str(totalrows) + " rows of data in the data.csv file.\nThis includes the first line containing column titles.") # println command to display number of rows
print(f"There are {validrows} rows with valid profit values (Either integer or decimal values)") # print number of valid lines

sortedprofits = sorted(validrowvalues, key=lambda x: float(x[columns - 1]), reverse=True) # use pythons built in sorting methods along with a lambda function. then sort in descending order
print("The 20 Highest Profiting Companies are:") 
for l in range(20): # for loop iterates over first (top) 20 values
    print(f"{l + 1}. {sortedprofits[l]}\n") # score and print each company

