##
# This program was coded by Jamie Block (Student #: 250777666)
# This program is designed to analyze Twitter information using textual analysis
# using functions, complex data structures, nested loops
#

# Prompt user for name of file containing keywords; check if file exists

try :
    keywordsFile = input('Enter the filename that contains the keywords: ')
    infile = open(keywordsFile, 'r')

    unhappy = []    # For keywords with sentiment value of 1
    satisfied = []  # For keywords with sentiment value of 5
    happy = []      # For keywords with sentiment value of 10

    for line in infile :
        line = line.rstrip('\n')
        splitLine = line.split(',')
        if splitLine[1] == '1' :
            unhappy.append(splitLine[0])
        elif splitLine[1] == '5' :
            satisfied.append(splitLine[0])
        else :
            happy.append(splitLine[0])
finally:
    print()
