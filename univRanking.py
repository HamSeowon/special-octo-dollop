#capitals
#CAPITAL_FILE = "capitals.csv"
COUNTRY_NAME = 0
CAPITAL = 1
CONTINENT = 5

#TopUni
#TOPUNI_FILE = "TopUni.csv"
WORLD_RANK = 0
INSTITUTION = 1
COUNTRY = 2
NATIONAL_RANK = 3
SCORE = 8

COMMA = ","

#File to List
def FileToList(filename):
    newList = []
    filename = open(filename,"r")
    for line in filename:
        line = line.strip()
        line = line.split(COMMA)
        newList.append(line)
    newList.pop(0)
    filename.close()
    return newList



#1
def universityCount(topuniFile):
    file = FileToList(topuniFile)
    count = len(file)
    text = "Total number of universities => " + str(count)
    return text

#2
def availableCountries(topuniFile):
    file = FileToList(topuniFile)
    newSet = set()
    countries = ""
    for i in range(len(file)):
        country = file[i][COUNTRY]
        newSet.add(country.upper())
    
    for i in newSet:
        countries += i + ", "
    
    str = countries[:-2]
    text = "Available countries => {0}".format(str)
    return text

#3
def availableContinent(capitalsFile):
    file = FileToList(capitalsFile)
    newSet = set()
    continents = ""
    for i in range(len(file)):
        country = file[i][CONTINENT]
        newSet.add(country.upper())
    
    for i in newSet:
        continents += i + ", "
    
    str = continents[:-2]
    text = "Available continents => {0}".format(str)
    return text

#4
#select country and show top uni and its rank
def universityRanking(selected_Country,topuniFile):
    file = FileToList(topuniFile)
    internationalRanking = []
    name = []
    for info in file:
        infoCountry = info[COUNTRY].upper()
        selected_Country = selected_Country.upper()
        if infoCountry == selected_Country:
            internationalRanking.append(info[WORLD_RANK])
            name.append(info[INSTITUTION])
    
    text = "At international rank => {0} the university name is => {1}".format(internationalRanking[0],name[0].upper())
    return text

#5
def topNationalRank(selected_Country,topuniFile):
    file = FileToList(topuniFile)
    nationalRanking = []
    name = []
    for info in file:
        infoCountry = info[COUNTRY].upper()
        selected_Country = selected_Country.upper()
        if infoCountry == selected_Country:
            nationalRanking.append(info[WORLD_RANK])
            name.append(info[INSTITUTION])
    text = "At national rank => {0} the university name is => {1}".format(1,name[0].upper())
    return text

#6
#scores of all uni and number of uni
def averageScore(selected_Country,topuniFile):
    file = FileToList(topuniFile)
    scores = []
    for info in file:
        if selected_Country.upper() in info:
            scores.append(float(info[SCORE]))


    totalScore = sum(scores)
    totalNum = len(scores)

    average = round(totalScore/totalNum,2)
    return average


def printAverageScore(selected_Country,topuniFile):
    average = averageScore(selected_Country,topuniFile)
    text = "The average score => {0}%".format(average)
    return text

#7
#continent/country,
def continentRelativeScore(selected_Country,topuniFile,capitalsFile):
    continentsAndCountry = {}
    countriesInContinent = []
    file1 = FileToList(capitalsFile)
    file2 = FileToList(topuniFile)
    topScoreContinent = 0.0
    continent = ""

    for info1 in file1:
        country = str(info1[COUNTRY_NAME].upper())
        if country == selected_Country.upper():
            continent = str(info1[CONTINENT].upper())
    
    for i in file1:
        if i[CONTINENT].upper() == continent.upper():
            countriesInContinent.append(i[COUNTRY_NAME])
    
    continentsAndCountry[continent] = countriesInContinent

    for info2 in file2:
        country  = info2[COUNTRY].upper()
        for i in countriesInContinent:
            if country == i.upper():
                score = float(info2[SCORE])
                if score > topScoreContinent:
                    topScoreContinent = score

    average = averageScore(selected_Country,topuniFile)
    relativeScore = (average / topScoreContinent) *100

    text = "The relative score to the top university in {0} is => ({1} / {2}) x 100% = {3}%".format(continent,round(average,2),round(topScoreContinent,2),round(relativeScore,2))
    return text

#8 
#show capital of selected country

def capitalCity(selected_Country,capitalsFile):
    file = FileToList(capitalsFile)
    capital = ""
    for info in file:
        if info[COUNTRY_NAME].upper() == selected_Country.upper():
            capital = str(info[CAPITAL].upper())
    return capital

def printCapitalCity(selected_Country,capitalsFile):
    capital = capitalCity(selected_Country,capitalsFile)
    text = "The capital is => {0}".format(capital)
    return text

#9
#university containing "capital"
def uniWithCapital(selected_Country,topuniFile,capitalsFile):
    file = FileToList(topuniFile)
    capital = str(capitalCity(selected_Country,capitalsFile))
    lst = []
    university = ""
    for info in file:
        uni = str(info[INSTITUTION].upper())
        if capital in uni:
            lst.append(uni)
    
    for i in range(len(lst)):
        university += "\n%4s#%d%s" %("",i+1,lst[i])
    
    text = "The universities that contain the capital name => {0}".format(university)
    return text

def getInformation(selectedCountry,rankingFileName,capitalsFileName):
    # university = FileToList(rankingFileName)
    # capitals = FileToList(capitalsFileName)
    selectedCountry = selectedCountry.upper()
    with open('output.txt','w') as file:
        #1
        file.write(universityCount(rankingFileName)+"\n\n")
        #2
        file.write(availableCountries(rankingFileName)+"\n\n")
        #3
        file.write(availableContinent(capitalsFileName)+"\n\n")
        #4
        file.write(universityRanking(selectedCountry,rankingFileName)+"\n\n")
        #5
        file.write(topNationalRank(selectedCountry,rankingFileName)+"\n\n")
        #6
        file.write(printAverageScore(selectedCountry,rankingFileName)+"\n\n")
        #7
        file.write(continentRelativeScore(selectedCountry,rankingFileName,capitalsFileName)+"\n\n")
        #8
        file.write(printCapitalCity(selectedCountry,capitalsFileName)+"\n\n")
        #9
        file.write(uniWithCapital(selectedCountry,rankingFileName,capitalsFileName))


getInformation("usa","TopUni.csv","capitals.csv")
