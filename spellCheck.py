# Rebecca Hsieh
# Goal: Utilizing a given dictionary list, we find the closest words to it given a distane (like spell check)
# Note: wording is user input word, word is from the dictionary

import sys

def readfile():

    dictionarylist = [] 
    
    if len(sys.argv) <= 1:
        filename = input("Input a file name: ") 
    else:
        filename = sys.argv[1]

    inputfile = open(filename, "r") 
    
    for word in inputfile:
        word = word.strip() # Strips the white space
        word = word.lower() # Double checks that everything is lower case
        dictionarylist.append(word) # Adds every word in the file name into an array for my function to go through

    inputfile.close() 

    return dictionarylist # Return the dictionary words that I have put/made

# This function gives the integer of the minimum hamming distance i.e. 1,2,3 away from the user inputted word
def hammingdistance(wording, word): # wording is user input word, word is from the dictionary
    
    count = 0
    for indexing in range(0, len(word)):
        if word[indexing] != wording[indexing]:
            count = count + 1  
    return count

# This function returns the list of close words that have the minimum hamming distance
def minhamming(wording, dictionarylist):

    count = -1 #hamming distance
    returnlist = []

    for word in dictionarylist:

        if len(word) == len(wording): # Figure out if length is the same

            if count < 0: # Never found a word before that's the same length
                count = hammingdistance(wording, word) 
                returnlist.append(word)

            elif hammingdistance(wording, word) == count: # Find another one that's the same length and add to the list
                returnlist.append(word)

            elif hammingdistance(wording, word) < count:
                returnlist.clear() # Clears all of the olds words that have a higher hamming distance
                returnlist.append(word)
                count = hammingdistance(wording, word)
                  
    return returnlist # Gives list of all words that have the minimum hamming distance         
 
def main():

    wording = input("Word to spell-check: ") 

    if len(wording) == 0: 
        print("End of spell-check run")
    else:
        wording = wording.lower()
        check = False

        for word in dictionarylist:
            if word == wording:
                check = True

        if check == True:
            print(wording + " found in dictionarylist")

        if check == False:
            spellchecklist = minhamming(wording, dictionarylist) # Set spellchecklist to the list that is returnlist
 
            if len(spellchecklist) == 1:    
                print("The nearest word to '" + wording + "' is " + "'" + spellchecklist[0] + "'")
            if len(spellchecklist) > 1:
                print("The nearest word to '" + wording + "' are", spellchecklist)           
        main()

# ---------------------------------------------------------------------------------------------------------------------

dictionarylist = readfile() # Sets the returned variable equal to the variable that the function returns - puts everything into a list

main() 



    











