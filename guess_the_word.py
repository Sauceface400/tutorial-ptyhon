guess_the_word = ""
gues_num = 0
limit = 4
game_over = False
while guess_the_word != "lasagna" and not(game_over):
    if gues_num < limit:
        guess_the_word = input("Say the secret word: ")
        gues_num += 1
    if guess_the_word == "lasagna":
        while guess_the_word != "beach" and not(game_over):
            if gues_num < limit:
                input("Enter the new word: ")
                gues_num += 1
    else:
        game_over = True
if game_over:
    print("YOU LOSE!")
