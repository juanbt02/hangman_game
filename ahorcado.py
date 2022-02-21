#Reglas: incoporar comprehensions, manejar archivo data.txt
# Investigar funcion enumerate, el método get, os.system("clear")

import random
import os
from xml.etree.ElementTree import tostring

def getWord():
    
    i = 0
    word = str
    num_random = int(random.uniform(1,170))
    final_word = []

    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]
        word = list(words[num_random])
    f.close()

    while i < len(word) -1:
        final_word.append(word[i])
        i+=1

    return final_word
        

def run():
    

    handed_picture = [
        """--------------||
                 |
           ||             
           ||   
           ||   
           ||___________
        """,
        """--------------||
                 |
           ||    O         
           ||   
           ||   
           ||___________
        """,
        """--------------||
                 |
           ||    O         
           ||   {
           ||   
           ||___________
        """,
        """--------------||
                 |
           ||    O         
           ||   {|
           ||   
           ||___________
        """,
        """--------------||
                 |
           ||    O         
           ||   {|}
           ||   
           ||___________
        """,
        """--------------||
                 |
           ||    O         
           ||   {|}
                /
           ||   
           ||___________
        """,
        """--------------||

           ||             
           ||     O
           ||    /|\ 
           ||___ / \  ___
                iiiii
        """,
    ]

    attemps = 6
    fails = 0
    word = getWord()
    underscore_word = []
    for i in word:
        underscore_word.append("_")


    while True:
        os.system("clear")
        print("!ADIVINA LA PALABRA!\n")
        print(handed_picture[fallos])
        print(str(underscore_word), "\n")
        index = 0
        validator = 0
        n = input("Introduce una letra: ")
        if fails < attemps:
            while index < len(word):
                if word[index] == n:
                    underscore_word[index] = n
                    validator+=1 
                index+=1
            if validator == 0:
                fails+=1
            
        if fails == attemps:
            os.system("clear")
            print(handed_picture[6])
            print("Has sido ahorcado, la palabra era: ", "".join(word))
            break

        if underscore_word == word:
            os.system("clear")
            print("!ENHORABUENA, LO HAS ADIVINADO¡")
            break
    

        
            
    

    


if __name__ == '__main__':
    run()
