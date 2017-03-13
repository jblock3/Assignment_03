##
# This program was coded by Jamie Block (Student #: 250777666)
# This program is designed to analyze Twitter information using textual analysis
# using functions, complex data structures, nested loops
#


# Prompts user for name of file containing keywords; checks if file exists

try :
    keywordsFile = input('Enter the filename that contains the keywords: ')
    infile = open(keywordsFile, 'r')

    unhappy = []    # For keywords with sentiment value of 1
    satisfied = []  # For keywords with sentiment value of 5
    happy = []      # For keywords with sentiment value of 10

    for keywordLine in infile :
        keywordLine = keywordLine.rstrip('\n')
        splitKeywordLine = keywordLine.split(',')
        if splitKeywordLine[1] == '1' :
            unhappy.append(splitKeywordLine[0])
        elif splitKeywordLine[1] == '5' :
            satisfied.append(splitKeywordLine[0])
        else :
            happy.append(splitKeywordLine[0])

    infile.close()
except IOError :
    print('Error: File', keywordsFile, "does not exist")
    quit()

# Prompts user for name of file containing Tweets text; checks if file exists
# If file exists, "happiness score" for tweet is calculated
try :
    tweetsFile = input('Enter the filename that contains the tweets: ')
    infile2 = open(tweetsFile, 'r')
    pacificTweets = []
    mountainTweets = []
    centralTweets = []
    easternTweets = []
    for line in infile2 :
        line = line.rstrip('\n')
        splitLine = line.split()

        latSplit1 = splitLine[0].rstrip(',')
        latSplit2 = latSplit1.lstrip('[')
        latitude = float(latSplit2)

        longSplit = splitLine[1].rstrip(']')
        longitude = float(longSplit)

        
finally:
    print()
