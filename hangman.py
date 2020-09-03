import random

words = ('python', 'java', 'kotlin', 'javascript')
random_word = list(random.choice(words))
# help_word = random_word[:3] + (len(random_word) - 3) * '-'
word = list(len(random_word) * '-')
old_letter = set()
print("H A N G M A N")
tries = 8

while True:
    play_exit = input('Type "play" to play the game, "exit" to quit:')
    if play_exit == 'exit':
        break
    elif play_exit == 'play':
        while tries and '-' in word:
            print('\n' + ''.join(word))
            letter = input("Input a letter: ")
            if len(letter) > 1:
                print("You should input a single letter")
            elif letter.istitle() or not letter.isalpha():
                print("It is not an ASCII lowercase letter")
            elif letter in old_letter:
                print("You already typed this letter")
            else:
                old_letter.add(letter)
                while random_word.count(letter):
                    word[random_word.index(letter)] = letter
                    random_word[random_word.index(letter)] = '-'
                    if not random_word.count(letter):
                        break
                    print()
                else:
                    print("No such letter in the word")
                    tries -= 1

        print(f"\n{''.join(word)}\nYou guessed the word!\nYou survived!" if '-' not in word else "You are hanged!")
