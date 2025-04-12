from TextProcessor import TextProcessor
import os
import string
import json

def main():
    '''
    Iterate over all saved webpages and extract statistics to read later
    '''
    processor = TextProcessor()
    dataDir = "RawTextContents"
    allLetters = string.ascii_lowercase
    allDigits = [0,1,2,3,4,5,6,7,8,9]
    files = os.listdir(dataDir)

    fileStats = {"stats": []}
    for file in files:
        filePath = dataDir + '/' + file
        with open(filePath, 'r') as f:
            print(f"+++ Processing file {filePath}")

            # Read contents
            contents = f.read()

            # Word distributions
            words = processor.findWords(contents)
            words = [x.lower() for x in words]
            wordSet = set(words)
            wordCounts = [words.count(x) for x in wordSet]

            # Letter distributions
            firstLetters = [x[0] for x in words]
            letterCounts = [firstLetters.count(x) for x in allLetters]

            # Number distributions
            nums = processor.findNumbers(contents)
            numSet = set(nums)
            numCounts = [nums.count(x) for x in numSet]

            # Digit distributions
            firstDigits = [processor.firstDigit(x) for x in nums]
            digitCounts = [firstDigits.count(x) for x in allDigits]

            # Pack statistics into JSON format
            fileStats["stats"].append(packIntoFormat(file.replace(".txt", ""), wordSet, wordCounts, letterCounts, numSet, numCounts, digitCounts))

    # Save file stats to JSON
    jsonString = json.dumps(fileStats)
    with open("fileStats.json", "w") as f:
        f.write(jsonString)

def packIntoFormat(fileName, wordSet, wordCounts, letterCounts, numSet, numCounts, digitCounts):
    return {
        "file": fileName,
        "allWords": list(wordSet),
        "wordCounts": wordCounts,
        "letterCounts": letterCounts,
        "allNumbers": list(numSet),
        "numCounts": numCounts,
        "digitCounts": digitCounts
    }

if __name__ == "__main__":
    main()