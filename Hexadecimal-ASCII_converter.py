##ASCII to Hexadecimal##
def hex_ascii():
    ##Hexadecimal input from user##
    hex_input=input("Enter a hexadecimal value of a word/sentence: ")

    ###to check whether input starts with '0x', and removes it
    h=list(hex_input)
    if h[0]=='0' and h[1]=='x':
        h.pop(1)
        h.pop(0)
        hex_input=''.join(h)
    
    ##list to seperate the input string##
    hex_list=[]
    
    ##temporary list to help achieve desired result##
    temp_list=[]
    
    ##help count in even numbers##
    x=0

    ##loop to separate input string by 2 hex digits##
    for i in range(len(hex_input)//2):
        ##clear temporary list##
        temp_list=[]
        
        ##appending 2 hex digits into temporary list##
        temp_list.append(hex_input[x])
        temp_list.append(hex_input[x+1])
        
        ##join all the strings in temporary list (2 hex digits) into one string
        temp_var=''.join(temp_list)
        
        ##append into hex_list##
        hex_list.append(temp_var)
        
        ##x increases by 2##
        x+=2
        
    ##list for ASCII characters##
    asc=[]
    
    ##list to convert all strings from hex_list to ASCII characters##
    for i in hex_list:
        asc.append(chr(int(i,16)))

    ##join all strings from asc and show as output##
    print(''.join(asc))

##ASCII to Hexadecimal##
def ascii_hex():
    ##input from user##
    ascii_input=input("Enter a word/sentence: ")

    ##separate each character and put them in a list##
    ascii_list=list(ascii_input)

    ##storing hexadecimal values of each character (with 0x in each string) in a list##
    ascii_value=[]

    for i in ascii_list:
        ascii_value.append(hex(ord(i)))

    ##removing '0x' from each string##
    ascii_value=[l.replace('0x','') for l in ascii_value]
    
    ##joining all list into one string
    output=''.join(ascii_value)

    ##printing result starting with '0x' to show that it is hexadecimal
    print('0x'+output+'\n')

##Main loop##
while True:
    print("Choose one option:\n(1) Hexadecimal to ASCII\n(2) ASCII to Hexadecimal \n(quit)")
    a=input()
    if a=='1':
        hex_ascii()
    elif a=='2':
        ascii_hex()
    elif a=='quit':
        break
    else:
        print("Error: Please select 1 or 2")
