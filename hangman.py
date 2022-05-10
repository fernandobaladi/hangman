import random
import os

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):

            continue
        line = aline
    return line

def clear_console():
    os.system('cls')

def remove_life(life):
    life -=1
    return life

def replace_characters(hidden_word, character_index, user_input):
    hidden_word_array = list(hidden_word.replace(" ", ""))
    hidden_word = ""
    for i in range(len(hidden_word_array)):
        if( i in character_index):
            hidden_word_array[i] = user_input.upper()
            hidden_word = hidden_word + user_input.upper() + " "
        else:
            hidden_word = hidden_word + hidden_word_array[i] + " "
    return hidden_word
    
def check_letter(word, user_input, hidden_word):

    if(len(user_input)>1):
        return False
    
    if(user_input.upper() in hidden_word):
        return False

    if user_input.lower() in word:
        character_index = [index for (index) in range(len(word)) if word[index] == user_input.lower()]
        return character_index
    else:
        return False


def user_input_character():
    user_input = input('Enter a letter: ')
    return user_input

def setup_game():
    with open('./files/data.txt', 'r',encoding='utf-8') as f:
        lines = f.read().splitlines()
        word = lines[random.randint(0,len(lines))]
        f.close()
    hidden_word = ''
    life = 6
    for i in word:
        hidden_word = hidden_word + '_ '
    return word, life, hidden_word

def print_info(hidden_word,life):
    print(hidden_word)
    print("Life: " + str(life))

def run():
    word, life, hidden_word = setup_game()
    clear_console()
    print_info(hidden_word,life)
    while(hidden_word.count('_')>0 and life>0):
        
        user_input = user_input_character()
        character_index = check_letter(word, user_input, hidden_word)
        if(not character_index):
            life = remove_life(life)
        else:
            hidden_word = replace_characters(hidden_word, character_index, user_input)
        
        clear_console()
        print_info(hidden_word,life)
    
    if(life>0):
        print("Great! You did it")
    else:
        print("Good luck next time :(")

if __name__ == "__main__":
    run()