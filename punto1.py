def main(entry):

    asterisk = bool(0)
    firstCharacter =bool(0)
    characters = bool(1) 

    i=0
    
    for i in range(len(entry)):
        if entry[0] == '&' or entry[0] == entry[0].upper():
            firstCharacter = True
        if i>=2 and entry[i]=='*':
            asterisk = True
        if i>=1 and ord(entry[i])<97 and ord(entry[i])!=45 and ord(entry[i])!=95 and ord(entry[i])!=42:
            characters = False
        if i>=1 and ord(entry[i])>122:
            characters = False
            

    if asterisk == True and firstCharacter ==True and characters==True:
        print ("La cadena es ACEPTADA")
    else:
        print ("la cadena es RECHAZADA")  




if __name__ == "__main__":
    
    print ("Ingrese la entrada: ")
    entry = input()
    
    main(entry)

