#Macarie Razvan Cristian 332CB
from string import ascii_uppercase
import sys

#return a list of patterns starting from the first pattern
#LFA -> ['', 'L', 'LF', 'LFA']
def makePrefixList(pattern):
    lista = []
    for i in range(0, len(pattern)+1):
        lista.append(pattern[0:i])
    return lista

#make the delta matrix used for searching
def makeMatrix(pattern):
    matrix = []
    prefixList = makePrefixList(pattern)
    #loop trough pattern
    for i in range(len(pattern)+1):
        toAdd = []
        #loop trough ascii_uppercase
        for letter in ascii_uppercase:
            #join the current letter to the current prefix
            current = prefixList[i]
            current += letter

            #strip the first letters if the word is too big
            if len(current) > len(pattern):
                current = current[len(current)-len(pattern)::]

            #while we have no match with any prefix in the prefix list
            #we keep removing lettern from the current word and decrease
            #the counter
            counter = len(current)
            while counter > 0:
                if current == prefixList[counter]:
                    break
                else:
                    current = current[len(current)-counter+1::]
                    counter -= 1

            toAdd.append(counter)
        matrix.append(toAdd)
    return matrix

#search function that works like a DFA
def search(pattern, text):
    state = 0
    list = []
    matrix = makeMatrix(pattern)
    for caracter in range(len(text)):
        state = (matrix[state])[ord(text[caracter])-ord('A')]
        if state == len(pattern):
            list.append(caracter-len(pattern)+1)
    return list

#file print function
def print_list(list, file):
    for x in list:
        print(x," ", sep="", end="", file=file)
    print("\n", sep="", end="", file=file)

def main(argv):
    #files
    fileToRead = open(argv[1], "r")
    fileToPrint = open(argv[2], "w")
    
    pattern = fileToRead.readline().strip("\n")
    text = fileToRead.readline().strip("\n")
    
    list = search(pattern, text)
    print_list(list, fileToPrint)

if __name__ == "__main__":
    main(sys.argv)