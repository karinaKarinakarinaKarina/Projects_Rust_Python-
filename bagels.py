import random
num_digits = 3 #количество цифр в заданном числе
max_guesses = 8

def secret_num():
    #строка из num_digits уникальных цифр
    numbers=list('0123456789')
    random.shuffle(numbers) #перетасовка цифр
    secretNum = ''
    #первые num_digits цифр из списка
    for i in range(num_digits):
        secretNum +=str(numbers[i])
    return secretNum

def clues(guess,secretNum):
    #возвращение подсказок для полученной догадки
    if guess== secretNum:
        return 'Congratulations! You are right!'
    cluess=[]
    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            #right digit on right position
            cluess.append('Fermi')
        elif guess[i] in secretNum:
            #right digit on wrong position
            cluess.append('Pico')
    if len(cluess)==0:
        return 'Bagels' #no right digits
    else:
        #подсказки сортируем в алфавитном порядке, чтобы их порядок исходных ничего не значил
        cluess.sort()
        #список подсказок в одну строку
        return' '.join(cluess)



def main():
    print('Bagels, a logic game.')
    print('I am thinking of a'+str(num_digits)+'-digit number with no repeated digits. Try to guess it. Here are some clues:\n')
    print(' Pico - One digit is correct but in the wrong position.\n')
    print('Fermi - One digit is correct and in the right position\n')
    print('Bagels - No digits is correct')

    while True:
        secretNum = secret_num() #то, что нужно угадать
        print('I have thought up the number. Try to guess it :))')
        print('You have only' + str(max_guesses) + 'guesses to understand what is the digit.')
        num_guess=1
        while num_guess <=max_guesses:
            guess=''
            while len(guess) != num_digits or not guess.isdecimal(): #проверка, что все символы строки являются десятичными
                print('Guess #{}:'.format(num_guess))
                guess = input('> ')
            cclues = clues(guess,secretNum)
            print(cclues)
            num_guess +=1
            if guess==secretNum:
                break
            if num_guess > max_guesses:
                print('Too much guesses,bro! The answer was {}.'.format(secretNum))
        #хочет ли игрок сыграть еще раз?
        print('Maybe you wanna play again?(print yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
if __name__ == '__main__':
    main()
