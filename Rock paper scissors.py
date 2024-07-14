
print("***ROCK PAPERS SCISSORS GAME***")


import random as r

lst=['rock','paper','scissors']

print("LETS PLAY!!! Choose any one of the following: ")
for i in range(len(lst)):
    print(lst[i]," ")
    

def fun(l):
    user=input("enter your choice: ")
    bot=r.choice(l)
    if user==bot:
        print(bot,"\n its a tie!")
    elif user=='rock' and bot=='paper':
        print(bot,"\n you lost!")
    elif user=='paper' and bot=='scissors':
        print(bot,"\n you lost!")
    elif user=='scissors' and bot=='rock':
        print(bot,"\n you lost!")
    elif user=='paper' and bot=='rock':
        print(bot,"\n you won!")
    elif user=='scissors' and bot=='paper':
        print(bot,"\n you won!")
    elif user=='rock' and bot=='scissors':
        print(bot,"\n you won!")
    else:
        print("wrong input, enter again")
        fun(l)

while True:
    fun(lst)
    play=input(" do u wanna have a match again? Y/N: ")
    if play in 'Yy':
        fun(lst)
    elif play in 'nN':
        print("Bye! see you again! Thanks for playing")
        break
    else:
        print("wrong input \n GAME OVER!!!")
