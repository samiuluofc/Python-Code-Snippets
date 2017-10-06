def createParagraphList(inf):
    inf.seek(0)
    allText = inf.read()
    pList = allText.split("\n\n")
    
    return pList

def sentenceCount(aParagraph):
    sc = aParagraph.count(".") + aParagraph.count("?") + aParagraph.count("!")
    
    return sc
    
def wordCount(aParagraph):
    wList = aParagraph.split()
    return len(wList)
    
# return a dictionary of max words
def getMaxWord(allWordList):
    countDic = {}
    maxWords = {}
    for i in allWordList:
        if i in countDic.keys():
            countDic[i] += 1
        else:
            countDic[i] = 1
            
    maxValue = max(countDic.values())
    for i in countDic.keys():
        if countDic[i] == maxValue:
            maxWords[i] = maxValue
            
    return maxWords
    
def main():
    # Open the file
    inFileName = input("Enter input file name (with .in extension): ")
    outFileName = inFileName[:inFileName.find(".")] + ".out"
    print(outFileName + " is the output file.")
    
    inf = open(inFileName, "r")
    outf = open(outFileName, "w")
    allText = inf.read()
    
    pList = createParagraphList(inf)
    outf.write("# of paragraphs: " + str(len(pList)) + "\n\n")

    paragraphNum = 0
    for i in pList:
        numOfSentences = sentenceCount(i)
        numOfWords = wordCount(i)
        paragraphNum += 1
        
        outf.write("Paragraph " + str(paragraphNum) + ":\n")
        outf.write("  # of sentences: " + str(numOfSentences) + "\n")
        outf.write("  # of words: " + str(numOfWords) + "\n\n")
    
    allWordList = allText.split()

    # remove all punctuations in a list of all words
    # change all words to lower case
    for i in range(0, len(allWordList)):
        aWord = allWordList[i]
        aWord = aWord.lower()
        
        if "." in aWord or "?" in aWord or "!" in aWord or "," in aWord or ";" in aWord:
            aWord = aWord[:len(aWord)-1]
        
        allWordList[i] = aWord
            
    outf.write("Total # of words: " + str(len(allWordList)) + "\n")
    
    # deal with max words
    maxWordDic = getMaxWord(allWordList)
    for i in maxWordDic.keys():
        if maxWordDic[i] == 1:
            outf.write("\"" + i + "\"" + " occurs " + str(maxWordDic[i]) + " time\n")
        else:
            outf.write("\"" + i + "\"" + " occurs " + str(maxWordDic[i]) + " times\n")
    
#    outf.write(allText)

    # Close the file
    inf.close()
    outf.close()
    
main()
