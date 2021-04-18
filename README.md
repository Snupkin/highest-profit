# Oran-Avivi-SADA-Tech-Challenge-2021
 SADA Technical Skill Assessment Challenge 2021

 github link: https://github.com/Snupkin/highest-profit

 **To execute code, run "run.bat"**
 *make sure you have python 3.8 or higher installed*

The code should run in terminal and produce the following result
![Sample Output Image](https://github.com/Snupkin/highest-profit/tree/main/images/sample_output.PNG)

## The main code: **max-profit.py**
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

## Intro
The code __*wasn't*__ too complicated with perhaps the exception of a lamda function. After revising the code to output proper JSON syntax, I had to fix a trailing comma issue as there was a syntax issue when appending dividing commas between data entries on every line.

In essence: this code starts by opening the data.csv file, creating a reader to peruse the file, and creating a for loop to index over each row. 
On the first iteration of the loop, it determines the number of columns by counting the number of titles.
it also stores the names of the column titles

## Code Breakdown
### Intro *1-31*
*1-4* start with comment section about author, date written, and general purpose of script.
this helps the reader know what the file is supposed to accomplish 
#### Imports
*6-11* import all of the necessary dependencies used in the code
### Output file check
*14-17* determine whether to write to the output file or create oneif it does not exist
#### Set-Up
*20* opens the data file 'data.csv'
*21* creates a reader for the csv file so it can be iterated over
*23-29* variable declarations
*31* a little hard-codey, but this essentially initializes the data2.json document to contain an array that will contain json objects
### Body *32-65*
#### FOR
*32-65* multi purpose for loop - The heart and body of the functionality of the code. iterates over the entire csv file
*33-64* if loop splits into 3 main sections
#### IF
*33* if on titles of csv (index 0 of csv.reader file)
*34-36* 1st line of data. since data is .csv, 1st line tends to be titles. csv.reader knows this and accounts for it. determines number of columns dynamically - i check the first line in case there are missing column fields down the road which could produce an invalid profit field. gets the column names. increments total rows
#### ELSE IF
*37* else if 1st line of data
*38-49* tries to convert profit value of data (5th column/4th index of each row) into a float. 
*39-47* on success this confirms all characters in the field have proper numerical format, do not contain numbers, and exists. 
*41* saves valid rows locally for future analysis. 
*42-43* increments valid row count and total row count
*44* converts python data structure from iterated list to dictionary allowing the use of pythons built in json dependencies/libraries to convert to a json object and output it to the file
*46-47* almost literally dumps formatted valid row data into the json file with nice formatting.
*48-49* event exception it does not output invalid data to data2.json file but still increments total row counter
#### ELSE
*52-64* pretty much exactly like the else if, but preceeds each json output line with a comma to separate the objects in the json array
iterates over entire data set trys to convert the last index of each row (the profit values) to a float value.
only main difference is the preceeding comma in front of every line. I tried implementing simply and if and else method, but i ended up with trailing commas which caused a format error in the data2.json file. Were I to re-write the code, I would change the slmost copy-pasted elif/else try/except methods and implement them as a function, which would make the script more efficient, and easier to generalize. 
*65* the closing syntax for a json list of objects

*67-68*The first 2 print lines: 
1. the total number of rows 
2. the number of rows with valid profit lines
believed to be:
![Total company rows && Total valid profit rows](https://github.com/Snupkin/highest-profit/tree/main/images/first_two_outputs.PNG)

### Sort
__*71*__ One of the main advantages of python is the plethora of libraries and methods it aleady has implemented. While I could have coded a multi-line sorting algorithm, I decided to implement pythons built in sorting system. Using this with an in-line lamda function sorts the entire valid data set in 1 line. This was very useful as the data is essentially a list of lists (matrix), so hardcoding a sorting algorithm such as bucket sort/quick sort would be more time intensive on the developer with minor performance gains on a data size of ~25k^2 = ~625 million computations. On a standard 2ghz cpu this is done in a fraction of a second.
sorts the data based on the 4th index of each row (the profit) in descending order from highest to lowest. 
*72-74* prints the first 20 results of line 71, satisfying the 3rd and final part of the challenge
3. outputs valid data to a json file named "data2.json"


Were the data different, a more omptimized sorting algorithm could be implemented, depending on data size and format. 
The valid profit conditional only accounts for non-integer characters. were the data formatted differently (hexadecimal, complex, exponents, etc...) this code may not be suitable, however, this would presumably be made known to us, and would still filter all profits not in integer/decimal notation

I managed to fix the .json file output. It now produces a json object containing a list of objects. 
Along the way I had some fun and made some minor functional changes.


I'm still thinking about how to implement this solution with SQL... it keeps me up at night
