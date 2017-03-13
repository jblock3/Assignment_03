

##
# This program was coded by Jamie Block (Student #: 250777666)
# This program is designed to analyze Twitter information using textual analysis
# using functions, complex data structures, nested loops
#



def main() :    # Defines main function for first part of program
    try :
        # Prompts user for name of file containing keywords; checks if file exists (if not, program quits)

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
                happinessScore()


            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -87.518395 and longitude >= -101.998892) :
                happinessScore()

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -101.998892 and longitude >= -115.236428) :
                happinessScore()

        print(numEasternTweets, easternScore)
        print(numCentralTweets, centralScore)
        print(numMountainTweets, mountainScore)
    except IOError :
        print('Error: File', tweetsFile, 'does not exist.')
        quit()


def happinessScore() :
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

main()
