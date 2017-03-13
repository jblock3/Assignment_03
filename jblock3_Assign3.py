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
    numPacificTweets = 0
    numMountainTweets = 0
    numCentralTweets = 0
    numEasternTweets = 0

    pacificScore = 0
    mountainScore = 0
    centralScore = 0
    easternScore = 0


    for line in infile2 :
        line = line.rstrip('\n')
        splitLine = line.split()

        latStrip1 = splitLine[0].rstrip(',')
        latStrip2 = latStrip1.lstrip('[')
        latitude = float(latStrip2)

        longStrip = splitLine[1].rstrip(']')
        longitude = float(longStrip)

        if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -67.4446574 and longitude >= -87.518395) :
            for element in splitLine :
                if element in unhappy :
                    numEasternTweets += 1
                    easternScore += 1
                if element in satisfied :
                    numEasternTweets += 1
                    easternScore += 5
                if element in happy :
                    numEasternTweets += 1
                    easternScore += 10


        if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -87.518395 and longitude >= -101.998892) :
            for element in splitLine :
                if element in unhappy :
                    numCentralTweets += 1
                    centralScore += 1
                if element in satisfied :
                    numCentralTweets += 1
                    centralScore += 5
                if element in happy :
                    numCentralTweets += 1
                    centralScore += 10

        if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -101.998892 and longitude >= -115.236428) :
            for element in splitLine :
                if element in unhappy :
                    numMountainTweets += 1
                    mountainScore += 1
                if element in satisfied :
                    numMountainTweets += 1
                    mountainScore += 5
                if element in happy :
                    numMountainTweets += 1
                    mountainScore += 10

        if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -115.236428 and longitude >= -125.242264) :
            for element in splitLine :
                if element in unhappy :
                    numPacificTweets += 1
                    pacificScore += 1
                if element in satisfied :
                    numPacificTweets += 1
                    pacificScore += 5
                if element in happy :
                    numPacificTweets += 1
                    pacificScore += 10

    print('The Eastern timezone has a happiness score of', easternScore / numEasternTweets, 'and has', numEasternTweets, 'tweets')
    print('The Central timezone has a happiness score of', centralScore / numCentralTweets, 'and has', numCentralTweets, 'tweets')
    print('The Mountain timezone has a happiness score of', mountainScore / numMountainTweets, 'and has', numMountainTweets, 'tweets')
    print('The Pacific timezone has a happiness score of', pacificScore / numPacificTweets, 'and has', numPacificTweets, 'tweets')

    infile2.close()

except IOError :
    print('Error: File', tweetsFile, 'does not exist.')
    quit()
