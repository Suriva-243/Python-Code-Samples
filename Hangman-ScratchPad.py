import random
word_list = ["cat", "dog", "rat","snake"] 
chosen_word = random.choice(word_list)
game_over=False

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct_letters = []
# TODO-1: - Use a while loop to let the user guess again.
while not game_over: 
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+='_'
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win.")


    
       

