# Rebecca Hsieh 
# Goal: Encode from ASCII to Base64
# Info: Taking in input, we shift the character and shift the numbers with correct spacing. We then translate them.


line = input ("Type something here ") 

number = 0
count = 0
base64 = ''

for character in (line):
    count +=1
    number = ord(character) + (number << 8)

total = count * 8 
othertotal = total / 6 

orange = int(othertotal)
   
while number > 0:

    orange -=1

    code = number >> (6 * orange) 
    number = number - (code << (6 * orange))
    
    if 0 <= code <= 25 :
        character = chr(code + ord('A') - 0)
    elif 26 <= code <= 51 :
	    character = chr(code + ord('a') - 26)
    elif 52 <= code <= 61 :
	    character = chr(code + ord('0') - 52)
    elif code == 62 : 
	    character = '+'
    elif code == 63 :
	    character = '/'
    base64 = base64 + character

print (base64)



