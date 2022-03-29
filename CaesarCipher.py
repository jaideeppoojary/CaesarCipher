#python 3.9.6
# declaring variable that we use as constants

asciiOfBigA = 65
asciiOfBigZ = 90
asciiOfSmallA =97
asciiOfSmallZ =122


def start():
  # Getting Sting value from user
  while True:    
    
    print("\n *** Enter your choice:*** \n")

    # Manual decript we use enter skip character (how much charecter  + or -) 
    encriptedString = input(" [ + ] Enter String : ")
    choice = int( input(" [ 1 ] Manual Encript/Decript \n [ 2 ] Auto Decript\n [ 3 ] Exit \n [ >> ]  "))
    
    if ( choice == 1):
      skip = int(input(" [ + ] how much to skip count : "))
      print("\n [ >> ]  "  + cipherEncryptDecrypt(encriptedString, skip ) + "\n" )

    elif (choice == 2):
      flag = input(" [ + ] Enter flag(hint word): ")
      autoCipherDecript(encriptedString, flag )

    else:
      print("\n ++  ++")
      print("  \__/")
      print("         --Bye")
      exit(0)


def cipherEncryptDecrypt(encriptedString, skipCharecter ):
  skipCharecter %=27  
  decriptString = ""
  for singleCharecter in encriptedString:

    # For big latters
    if( ord(singleCharecter) in range(65, 91)):
      decriptString = processString(decriptString, singleCharecter, skipCharecter, asciiOfBigA,asciiOfBigZ)
    # For small letters
    elif( ord(singleCharecter) in range(97, 123) ):
      decriptString = processString(decriptString, singleCharecter, skipCharecter, asciiOfSmallA,asciiOfSmallZ) 
    # For other characters
    else:
      decriptString = decriptString + singleCharecter    

  return decriptString


def processString(decriptString, singleCharecter, skipCharecter, asciiOfA, asciiOfZ):
  # getting new charecter by adding skip charecter
  newChar = (ord(singleCharecter) + skipCharecter)
  
  # if skipped ascii value other than a-z or A-Z like 63 
  # This function keeps that cycle a-z A-Z

  if( (newChar > asciiOfZ ) or (newChar < asciiOfA)):
    newChar = directionChange(newChar, asciiOfA, asciiOfZ)
  
  decriptString = decriptString + chr( newChar )
  return decriptString


# if we get ascii value other than a-z or A-Z like 63. 
# This function keeps that cycle
 
def directionChange(newChar, aPosition, zPosition):
  # Direction 'Z' to 'A' 
  if(newChar > zPosition ):
    newChar = (newChar - zPosition) + (aPosition - 1 )
  # Direction 'A' to 'Z'
  if(newChar < aPosition):
    newChar = (zPosition + 1) - (aPosition- newChar)
  
  return newChar


def autoCipherDecript(encriptedString, flag ):
  # skip = 0
  for skip in range(26,-1,-1):
    decriptString = cipherEncryptDecrypt(encriptedString, skip)

    if(flag in decriptString):
      print("\n [ >> ]  "  + decriptString + "\n" )
      return decriptString
  print(" [ ! ] Entered flag not in Encrypted String...")
  if __name__ != "__main__":
    return " [ ! ] Entered flag not in Encrypted String..."
    

  
# starts from here

if __name__ == "__main__":
  start();
else:
  print(" [!] Run CaesarCipher.py")
    