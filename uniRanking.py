#   Assignment 3
#   Name: Seowon Ham

#Constant Index Numbers
###capitals.csv
COUNTRY_NAME = 0
CAPITAL = 1
CONTINENT = 5

###TopUni.csv
WORLD_RANK = 0
INSTITUTION = 1
COUNTRY = 2
NATIONAL_RANK = 3
SCORE = 8

COMMA = ","

###Making the excel file to a List for a further usage.  
def FileToList(filename):
    #a list for a sorted excel file. 
    newList = []
    filename = open(filename,"r")
    for line in filename:
        #delete empty space
        line = line.strip()
        #remove comma that is delimiting the value. 
        line = line.split(COMMA)
        #append the value into the list. 
        newList.append(line)
    #remove the first list that indicates the information about the values. 
    newList.pop(0)
    #close the file.
    filename.close()
    #return the List.
    return newList

### PART 1
#   Count the number of universities. 
def universityCount(topuniFile):
    try:
        #call the List of required excel file. 
        file = FileToList(topuniFile)
        #the length of the List is equal to the number of universities. 
        count = len(file)
        #final statement
        text = "Total number of universities => " + str(count)
        return text
    except:
        pass

### PART 2
#   List the available countries.
def availableCountries(topuniFile):
    try:
        #call the List of required excel file. 
        file = FileToList(topuniFile)
        #use the set to find the list of available countries as set() does not accept repeated values. 
        newSet = set()
        #initial value of countries
        countries = ""
        #use the for loop to add countries from the List.
        for i in range(len(file)):
            country = file[i][COUNTRY]
            newSet.add(country.upper())
        
        #use a for loop to display a list of available countries in a comma-separated sentence.
        for i in newSet:
            countries += i + ", "
        #Remove the comma at the end of the sentence.
        str = countries[:-2]
        text = "Available countries => {0}".format(str)
        return text
    except:
        pass

### PART 3
#   List the available countries.
def availableContinent(capitalsFile):
    try:
        #call the List of required excel file.
        file = FileToList(capitalsFile)
        #use the set to find the list of available continents as set() does not accept repeated values. 
        newSet = set()
        #initial value of continents
        continents = ""
        #use the for loop to add countries from the List.
        for i in range(len(file)):
            country = file[i][CONTINENT]
            newSet.add(country.upper())

        #use a for loop to display a list of available countries in a comma-separated sentence.
        for i in newSet:
            continents += i + ", "
        #Remove the comma at the end of the sentence.
        str = continents[:-2]
        text = "Available continents => {0}".format(str)
        return text
    except:
        pass

### PART 4
#   International Ranking of the selected country. 
def universityRanking(selected_Country,topuniFile):
    try:
        #call the List of required excel file.
        file = FileToList(topuniFile)
        #create a list to contain the ranks.
        internationalRanking = []
        #create a list to contain the names.
        name = []
        for info in file:
            infoCountry = info[COUNTRY].upper()
            selected_Country = selected_Country.upper()
            if infoCountry == selected_Country:
                internationalRanking.append(info[WORLD_RANK])
                name.append(info[INSTITUTION])
        
        #final statement. 
        text = "At international rank => {0} the university name is => {1}".format(internationalRanking[0],name[0].upper())
        return text
    except:
        pass

### PART 5
#   National Ranking of the selected country. 
def topNationalRank(selected_Country,topuniFile):
    try:
        #call the List of required excel file.
        file = FileToList(topuniFile)
        #create a list to contain the name.
        name = []
        for info in file:
            infoCountry = info[COUNTRY].upper()
            selected_Country = selected_Country.upper()
            if infoCountry == selected_Country:
                name.append(info[INSTITUTION])
        text = "At national rank => {0} the university name is => {1}".format(1,name[0].upper())
        return text
    except:
        pass

### PART 6
#   Average score of the selected country. 
def averageScore(selected_Country,topuniFile):
    try:
        #call the List of required excel file.
        file = FileToList(topuniFile)
        #create a list to contain the scores.
        scores = []
        for info in file:
            country = info[COUNTRY].upper()
            if selected_Country.upper() == country:
                scores.append(float(info[SCORE]))
        #Total score is sum of the scores contained in the List.
        totalScore = sum(scores)
        #Total number of universities is the length of the List. 
        totalNum = len(scores)

        #round it to 2 decimal place. 
        average = round(totalScore/totalNum,2)
        return average
    except:
        pass

#   Print the final statement. 
def printAverageScore(selected_Country,topuniFile):
    try:
        #recall the average score. 
        average = averageScore(selected_Country,topuniFile)

        #final statement
        text = "The average score => {0}%".format(average)
        return text
    except:
        pass

### PART 7
#   Relative score of the continent 
def continentRelativeScore(selected_Country,topuniFile,capitalsFile):
    try:
        #call the Lists of required excel files.
        file1 = FileToList(capitalsFile)
        file2 = FileToList(topuniFile)

        #create a dictionary to contain the continent and countries.
        continentsAndCountry = {}
        #create a list to contain all countries in the continent.
        countriesInContinent = []
        #initial value of the highest score within the continent.
        topScoreContinent = 0.0
        continent = ""

        for info1 in file1:
            country = str(info1[COUNTRY_NAME].upper())
            if country == selected_Country.upper():
                continent = str(info1[CONTINENT].upper())
        
        for i in file1:
            if i[CONTINENT].upper() == continent.upper():
                countriesInContinent.append(i[COUNTRY_NAME])
        
        #add to the previously created dictionary.
        continentsAndCountry[continent] = countriesInContinent

        for info2 in file2:
            country  = info2[COUNTRY].upper()
            for i in countriesInContinent:
                if country == i.upper():
                    score = float(info2[SCORE])
                    if score > topScoreContinent:
                        topScoreContinent = score

        average = averageScore(selected_Country,topuniFile)
        relativeScore = (average/topScoreContinent) * 100

        #final statement. 
        text = "The relative score to the top university in {0} is => ({1} / {2}) x 100% = {3}%".format(continent,round(average,2),round(topScoreContinent,2),round(relativeScore,2))
        return text
    except:
        pass

### PART 8
#   The capital city of the selected country. 
def capitalCity(selected_Country,capitalsFile):
    try:
        #call the List of required excel file.
        file = FileToList(capitalsFile)
        capital = ""
        for info in file:
            if info[COUNTRY_NAME].upper() == selected_Country.upper():
                capital = str(info[CAPITAL].upper())
        return capital
    except:
        pass

#   Print the capital city of the selected country. 
def printCapitalCity(selected_Country,capitalsFile):
    try:
        capital = capitalCity(selected_Country,capitalsFile)

        #final statement
        text = "The capital is => {0}".format(capital)
        return text
    except:
        pass

### PART 9
#   The list of universities that contains the capitial city name in thir name. 
def uniWithCapital(selected_Country,topuniFile,capitalsFile):
    try:    
        #call the List of required excel file.
        file = FileToList(topuniFile)
        capital = str(capitalCity(selected_Country,capitalsFile))
        #create a List to contain the university name(s).
        lst = []
        #initial value of university name(s)
        university = ""
        for info in file:
            uni = str(info[INSTITUTION].upper())
            if capital in uni:
                lst.append(uni)
        
        #use a for loop to display a list of university name(s) with the number.
        for i in range(len(lst)):
            university += "\n%4s#%d%s" %("",i+1,lst[i])
        
        #final statement.
        text = "The universities that contain the capital name => {0}".format(university)
        return text
    except:
        pass


### FINAL
#   Get all informations and write them on output.txt file.  
def getInformation(selectedCountry,rankingFileName,capitalsFileName):
    try:
        selectedCountry = selectedCountry.upper()
        with open('output.txt','w') as file:
            ### PART 1
            file.write(universityCount(rankingFileName)+"\n\n")
            ### PART 2
            file.write(availableCountries(rankingFileName)+"\n\n")
            ### PART 3
            file.write(availableContinent(capitalsFileName)+"\n\n")
            ### PART 4
            file.write(universityRanking(selectedCountry,rankingFileName)+"\n\n")
            ### PART 5
            file.write(topNationalRank(selectedCountry,rankingFileName)+"\n\n")
            ### PART 6
            file.write(printAverageScore(selectedCountry,rankingFileName)+"\n\n")
            ### PART 7
            file.write(continentRelativeScore(selectedCountry,rankingFileName,capitalsFileName)+"\n\n")
            ### PART 8
            file.write(printCapitalCity(selectedCountry,capitalsFileName)+"\n\n")
            ### PART 9
            file.write(uniWithCapital(selectedCountry,rankingFileName,capitalsFileName))
    except:
        pass
