import random
def hang_man():
     
    wordslist = ['rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks']
    word=random.choice(wordslist)
    ourword=list("-"*len(word))
    turns=8
    while turns>0: 
        letter=input("guess the letter:")
        if letter in word:
            for i in range(len(word)):
                if word[i]==letter:
                    ourword[i]=letter
            myword=''.join(ourword)
            print(myword)
            if myword==word:
                print("Congrats "+name+" YOU WON")
                print("The word is",myword)
                break   
        else:
            turns-=1
            if turns==7:
                print("------------")
                print("Try again:Left with 7 turns-->")
            elif turns==6:
                print("------------")
                print("      O     ")
                print("Try again:Left with 6 turns-->")
            elif turns==5:
                print("-------------")
                print("      O     ")
                print("      |     ")
                print("Try again:Left with 5 turns-->")
            elif turns==4:
                print("-------------")
                print("      O     ")
                print("     \|     ")
                print("Try again:Left with 4 turns-->")
            elif turns==3:
                print("-------------")
                print("      O     ")
                print("     \|/    ")
                print("Try again:Left with 3 turns-->")
            elif turns==2:
                print("-------------")
                print("      O      ")
                print("     \|/     ")
                print("     /       ")
                print("Try again:Left with 2 turns-->")
            elif turns==1:
                print("-------------")
                print("      O      ")
                print("     \|/     ")
                print("     / \      ")
                print("Try again:Left with 1 turns-->")
            elif turns==0:
                print("-------------")
                print("      O      ")
                print("     /|\     ")
                print("     / \      ")
                print("ohh NO--you lost:")
                break           
                       
###############################################driver code
print("Enter your name:")
name=input()
print("Welcome",name,"!!!!!!")
print("Let's play the hangman game!!!")
print("-------------------------------")
print("Guess the word-->")
hang_man()