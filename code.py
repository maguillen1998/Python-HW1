import zipfile

zipFile = zipfile.ZipFile("C:/Users/magui/PycharmProjects/stuff/Jan.zip")
fileNames = zipFile.namelist()

fileNameDictionary = {}
for fileName in fileNames:
    #create string to hold file contents
    openFile = zipFile.open(fileName, 'r')
    #ceates a list containing all strings and makes them lower-case
    fileContent = str(openFile.read()).lower().split()
    wordList = []#will contain all alphabet words in file
    #adds strings with only alphabet chars to list
    for string in fileContent:
        if string.isalpha():
            wordList.append(string)
    fileContentDictionary = {}#create dictionary to be nested
    for word in wordList:
        #key maps to num occurances
        if fileContentDictionary.get(word) == None:
            fileContentDictionary[word] = 1
        else:
            fileContentDictionary[word] += 1
        #fileContentDictionary.setdefault(word, []).append(word)
    #map fileName key to dictionary containing all words in the file
    fileNameDictionary[fileName] = fileContentDictionary
    #fileNameDictionary.setdefault(fileName, []).append(fileContentDictionary)

print("Now search begins:")
keyword = input("enter a search key=>")
while keyword != '': #loop continues until empty input
    foundFlag = False
    for fileName in fileNames:
        #if keyword is in the nested dictionary
        if fileNameDictionary[fileName].get(keyword) != None:
            foundFlag = True
            numOccurrences = fileNameDictionary[fileName].get(keyword)
            if numOccurrences == 1:
                print("found", numOccurrences, "match:", fileName)
            else:
                print("found", numOccurrences,"matches:", fileName)
    if foundFlag == False:
        print("no match found")
    keyword = input("enter a search key=>")