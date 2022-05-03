from typing import List
import random

def loading_words() -> list:
    converted_list = []
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

wordlist = loading_words()

def main(secret_word: str):
    x = ("_____")
    print("---------")
    print("Welcome To Wordle")
    print("You have 5 guesses")
    #a = x.replace("_", "a", 1)
    secret_word1 = split(secret_word)
    x1 = split(x)
    print(secret_word1)

    for guesses in reversed(range(5)):
        guess = input("Guess a word: \n")
        print(f"you have {guesses} guesses left")
        guess1 = split(guess)
        print(guess1)

        if guess == secret_word:
            print("Correct!")
            break

if __name__ == "__main__":
    main(choose_word(wordlist))