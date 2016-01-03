# Rebecca Hsieh 
# Goal: Decode from Base64 to ASCII
# Info: Find the order of the characters and numbers given and shift them


line = input ("Type something here ")

number = 0
count = 0


for character in line:
    
        if 'A' <= character <= 'Z' :
            code = ord(character) - ord("A") - 0
        elif 'a' <= character <= 'z' :
            code = (ord(character) - ord("a")) + 26
        elif '0' <= character <= '9' :
            code = (ord(character) - ord("0")) + 52
        elif character == "+" : 
            code = 62
        elif character == "/" :
            code = 63

        number = code + (number << 6)
        count = count + 1

        if count == 4:
            while count >= 0:
                ASCII  = number >> (8 * count)
                number = number - (ASCII << (8 * count))
                count = count - 1
                print(chr(ASCII), end = "")
            count = 0

print("")

      
  
