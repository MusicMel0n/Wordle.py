from typing import List
import random
from colorama import init
from colorama import Fore
from colorama import Style

converted_list = []

def loading_words() -> list:
    in_file = open("wordle.txt", "r+")
    word_list = in_file.readlines()
    for element in word_list:
        converted_list.append(element.strip())
    print(f"Loaded {len(converted_list)} words")
    return converted_list

def choose_word(converted_list: List[str]) -> str:
    secret_word = random.choice(converted_list).lower()
    return secret_word

def split(word) -> list:
    return [char for char in word]

def listtostring(list) -> list:
    str1 = ""
    return (str1.join(list))

wordlist = loading_words()

def main(secret_word: str):
    init()

    print("---------")
    print("Welcome To Wordle")
    print("You have 5 guesses")
    secret_word1 = split(secret_word)
    print(secret_word1)

    for guesses in reversed(range(5)):
        guess = input("Guess a word: \n")

        if len(guess) != 5:
            print("Your guess has to be 5 characters long!")
            break

        if guess not in converted_list:
            print("Word does not exist")
            break

        print(f"you have {guesses} guesses left")
        guess1 = split(guess)
            
        for i in guess1:
            if i in secret_word1:
                if secret_word1.index(i) == guess1.index(i):
                    guess1[guess1.index(i)] = Fore.GREEN + i + Style.RESET_ALL

                elif i in secret_word1 and secret_word1.index(i) != guess1.index(i):
                    guess1[guess1.index(i)] = Fore.YELLOW + i + Style.RESET_ALL

        print(listtostring(guess1))

        if guess == secret_word:
            print("Correct!")
            break
  
if __name__ == "__main__":
    main(choose_word(wordlist))

#fix issue where if there are two of the same element it doesnt change both to green
#try making it so when a word is green you cannot overwrite it
