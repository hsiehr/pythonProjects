# Rebecca Hsieh
# Goal: Find frequency of words from given texts

import sys

def grabfiles():
    
    filelist = []
    
    if len(sys.argv) < 3:
        print("Usage: python3 WnnnnnnnnAssg3.py number file1 file2 . . .filen")
        quit()

    if sys.argv[1].isnumeric():
        filelist = sys.argv[1:]
        return(filelist)

    else:
        print("Usage: python3 WnnnnnnnnAssg3.py number file1 file2 . . .filen")
        quit()

#---------------------------------------------------------------------------------------------------

punctuation = ('!', '"', '#', '$', '%', '^', '&', '*', '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '_', '`', '{', '|', '}', '~')

def runthrough(filelist):
    
    previousletter = ""
    cleanlist = ""

    for filename in filelist[1:]:

        files = open(filename, 'r')

        for line in files:

            templine = ""
    
            for char in punctuation:
                line = line.replace(char, " ") # if character, replace with space
                line = line.replace("'", " ") # if apostrophe, replace with space
                line = line.lower()
                line = line.replace("\n", " ") # if new line, replace with space

            for char in line:
                if char == " ":
                    # if previousletter is not a space then it adds onto previousletter as a char
                    if previousletter != " ":
                        templine = templine + char # adds onto a new line string organiziation
                else:
                    templine = templine + char # adds onto a new line string organization
                previousletter = char # check to make sure previous letter is a character
            line = templine # puts all back into a line
            cleanlist = cleanlist + line # puts all filing together line by line that is cleaned
    return cleanlist

# sorts the item by key
def sortkey(item):
    return item[1]

# putting the number given in the command line and creating it into a integer 
def tointeger(filelist):
    number = int(filelist[0])
    return number

# MAIN ------------------------------------------------------------------------------------

filelist = grabfiles()
cleanlist = runthrough(filelist)
wordlist = {
cleanlist = cleanlist.split(' ')

for word in cleanlist:
    
    # that length of word is bigger than one or the other separated alphabetic letters
    # loops through to add how many times the word shows up in the files
    if len(word) > 1 or word == "i" or word == "a": 
        if word in wordlist:
            wordlist[word] = wordlist[word] + 1
        else:
            wordlist[word] = 1

wordylist = list(wordlist.items())

# sort wordylist by the key and make sure it's in numeric order
wordylist = sorted(wordylist, key = sortkey, reverse = True)

# putting the number given in the codfsdfl
# finds the maximum number a letter gives
maximum = 0
for integere in range(0, integer):
    if len(wordylist[integere][0]) > maximum:
        maximum = len(wordylist[integere][0])

# prints out the numeric order, the given number of words that appears the most times
# ljust, rjust are adjusted to print cleanly by adjusting to the right and left
for integere in range(0, integer):
    print((str(integere + 1) + ".").ljust(4), (wordylist[integere][0]).ljust(maximum), (str(wordylist[integere][1])).rjust(4))




