# Oran-Avivi-SADA-Tech-Challenge-2021
 SADA Technical Skill Assessment Challenge 2021

 github link: https://github.com/Snupkin/highest-profit

 **To execute code, run "run.bat"**
 *make sure you have python 3.8 or higher installed*

The code should run in terminal and prouce the following result
![Sample Output Image](https://github.com/Snupkin/highest-profit/tree/main/images/sample_output.PNG)

```python
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
```

The code isn't too complicated with perhaps the exception of a lamda function.
In essence: this code starts by opening the data.csv file, creating a reader to peruse the file, and creating a for loop to index over each row. 
On the first iteration of the loop, it determines the number of columns by counting the number of titles.
it also stores the names of the column titles

The for loop on line 28 trys to convert the last index of each row (the profit values) to a float value.
if successful, it increments the count for total # of rows and # of valid rows. 
string representations of integers and non-integer numbers (decimals) should be converted to a float value.
if unable to convert, it means theres a non-numerical value. thus, increment # of total rows by 1 
thus, totalrows increments every time and validrows only increments on successful string to float conversions, indicating no non-integer characters (excluding '.')

This produces the first 2 print lines (41/42) containing the total number of rows and the number of rows with valid profit lines, believed to be
![Total company rows && Total valid profit rows](https://github.com/Snupkin/highest-profit/tree/main/images/first_two_outputs.PNG)

Finally, checks if a data2.json file exists (code outputs it) and if so does a write to the file. Otherwise it creates a new file with the name 'data2.json'
It then dumps/converts the data from python objects to json file formats.

The companies profits are sorted based on the 4th index (starting from 0) of each row. thus need to compare values and sort.
Python has a built in sorting dependency that uses inline lambda functions. This was very useful as the data is essentially a list of lists (matrix), so hardcoding a sorting algorithm such as bucket sort/quick sort would be more time intensive on the developer with minor performance gains on a data size of ~25k^2 = ~625 million computations. On a standard 2ghz cpu this is done in a fraction of a second.

Were the data different, a more omptimized sorting algorithm can be used. 
The valid profit conditional only accounts for non-integer characters. were the data formatted differently (hexadecimal, complex, exponents, etc...) this code may not be suitable

I'm uncertain what the purpose of exporting to a .json file is, but I was unsure how to fix the formatting issues in data2.json. All of the information should be there, but the conversion from a python nested list to .json didnt seem to work as expected. I would definitely devise a more refined implementation given more time and a more specific description regarding the functionality of the .json file. (Currently, I have all of the data there, but unsure if the .json file is functional)

I'm still thinking about how to implement this solution with SQL... it keeps me up at night
