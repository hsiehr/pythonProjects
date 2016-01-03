# Rebecca Hsieh
# Goal: Given a certain number, we print out the digital formatting of it
# Info: Sorting  the given numbers with how they look printed out digitally, we go through the top/middle/bottom 
# functions to see how the numbers formatted.

userinput = input ("Type a number here ")

toplist = ["0", "2", "3", "5", "6", "7", "8", "9"]
toplist1 = ["1", "4"]
middlelist1 = ["4", "8", "9"]
middlelist2 = ["1", "7"]
middlelist3 = ["2", "3"]
middlelist4 = ["5", "6"]
bottomlist1 = ["0", "6", "8"]
bottomlist2 = ["1", "4", "7"]
bottomlist3 = ["3", "5", "9"]


def top():

    for topzone in userinput :

        if topzone == "-":
            print("   ", end = "")	
        if topzone in toplist:
            print(" _ ", end = "")
        elif topzone in toplist1:
            print("   ", end = "")

    print("", end = "\n")

def middle():

    for middlezone in userinput :

    	if middlezone == "-":
        	print(" __", end = "")
    	if middlezone == "0":
        	print ("| |", end = "")   
    	elif middlezone in middlelist2:
        	print ("  |", end = "")
    	elif middlezone in middlelist3:
        	print (" _|", end = "")
    	elif middlezone in middlelist1:
        	print ("|_|", end = "")
    	elif middlezone in middlelist4:
        	print ("|_ ", end = "")

    print("", end = "\n")

def bottom():

    for bottomzone in userinput :
    	if bottomzone == "-":
        	print("   ", end = "")
    	if bottomzone in bottomlist1:
        	print ("|_|", end = "")
    	elif bottomzone in bottomlist2:
        	print ("  |", end = "")
    	elif bottomzone == "2":
        	print ("|_ ", end = "")
    	elif bottomzone in bottomlist3:
        	print(" _|", end = "")

    print("", end = "\n")

top()
middle()
bottom()
