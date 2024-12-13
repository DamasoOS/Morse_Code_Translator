
CODE = {'A': '10111000',     'B': '111010101000',   'C': '11101011101000', 
        'D': '1110101000',    'E': '1000',      'F': '101011101000',
        'G': '111011101000',    'H': '1010101000',   'I': '101000',
        'J': '1011101110111000',   'K': '111010111000',    'L': '101110101000',
        'M': '1110111000',     'N': '11101000',     'O': '11101110111000',
        'P': '10111011101000',   'Q': '1110111010111000',   'R': '1011101000',
        'S': '10101000',    'T': '111000',      'U': '1010111000',
        'V': '101010111000',   'W': '101110111000',    'X': '11101010111000',
        'Y': '1110101110111000',   'Z': '11101110101000',

        '0': '1110111011101110111000',  '1': '10111011101110111000',  '2': '101011101110111000',
        '3': '1010101110111000',  '4': '10101010111000',  '5': '101010101000',
        '6': '11101010101000',  '7': '1110111010101000',  '8': '111011101110101000',
        '9': '11101110111011101000',

        ',':'1110111010101110111000',  '.':'10111010111010111000',
        '?':'101011101110101000',   '/':'1110101011101000',   '-':'111010101010111000',
        '(':'111010111011101000',    ')':'1110101110111010111000', ' ':'0000'
        
        
        }


CODE2 = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        ',':'--..--',  '.':'.-.-.-',
        '?':'..--..',   '/':'-..-.',   '-':'-....-',
        '(':'-.--.',    ')':'-.--.-',  ' ':'_'
        }


print("Welcome to Morse Code Translator!")
print("Created by Dámaso Matheus")
print("Compiled by Josh Grundmann")
print("There are four total services available:")
print("Translating English --> Morse Code Binary (1),")
print("translating English --> Morse Code (2) ,")
print("translating Morse Code Binary --> English (3),")
print("and translating Morse Code --> English (4).")
print("Alternatively, type (5) to get instructions on how to use this translator.")

service = (input("Type the corresponding number you want to translate:")).lower()

#This is if you want to translate English --> Morse Code Binary
if service == '1':      
    
#This loop is to make sure you're typing a letter correctly.
#For example, if someone puts a number it won't work because of the translate.isalpha() statement.

        
    while True:
        translate = input("Type what you want to translate:").upper()
        es = ''
        for i in translate:
            if len(i) > 0:
                es += (CODE[i])
                es += '-'
             
        
            else:
                print ("This format is invalid, try again.")
           
        print(es)

         
    

#This is if you want to translate English --> Morse Code
elif service == '2':

        while True:
            translate = input("Type what you want to translate:").upper()
            es = ''
            for i in translate:
                if len(i) > 0:
                    es += (CODE2[i])
                    es += '_'
             
        
                else:
                    print ("This format is invalid, try again.")
                    
            print(es)

#This is if you want to translate Morse Code Binary --> English
elif service == '3':

#This loop is to make sure you're typing a letter correctly.
#For example, if someone puts a number it won't work because of the translate.isalpha() statement.

    while True:
        translate = str(input("Type what you want to translate:")).upper()
        CODE_REVERSED = {value:key for key,value in CODE.items()}
        es = ''
        for i in translate.split('-'):

            if len(i) > 0:

                es += (CODE_REVERSED[i])
            
      
        
            else:
                print ("This format is invalid, try again.")
                
          
        print(es)
#This is if you want to translate Morse Code --> English
elif service == '4':

#This loop is to make sure you're typing a letter correctly.
#For example, if someone puts a number it won't work because of the translate.isalpha() statement.

    while True:
        translate = str(input("Type what you want to translate:")).upper()
        CODE_REVERSED2 = {value:key for key,value in CODE2.items()}
        es = ''
        for i in translate.split('_'):

            if len(i) > 0:

                es += (CODE_REVERSED2[i])
            
                
        
            else:
                print ("This format is invalid, try again.")
                
              
        print(es)

#Here are the instructions, available on request.   
elif service == '5':
    print("In order to use a service, type the number that corresponds with the sentence.")
    print("Once you have selected a service, type a message.")
    print("The translator will divide each character with a '-' or '_'.")
    print("In order to translate MCB or MC back to English, it would be ideal to remove the last '-'")
    print("(Though it will still work).")
    print("If you have typed an invalid service number, the translator will prompt you to run the program again.")
    print("Please run the program again to get started!")
    
else:
    print("Hmmm... try running the program again")
       


