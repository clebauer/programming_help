import random

def pick_a_word():
    #https://www.randomlists.com/random-words
    word_list = ['rich', 'decision', 'faulty', 'nine', 'ruthless', 'crash', 'turn', 
                 'belief', 'desire', 'ambitious', 'horses', 'messy', 'complex', 
                 'watch', 'activity', 'box', 'coat', 'succeed', 'sand', 'imaginary',
                 'fire', 'parallel', 'equal', 'twig', 'part', 'well-off', 'test',
                 'zinc', 'wriggle', 'female', 'sweater', 'base', 'pigs', 'disarm',
                 'juvenile', 'nutritious', 'deceive', 'husky', 'berry', 'rescue']
    rand_num = random.randint(0, len(word_list)-1)
    return word_list[rand_num]

def ask_for_letter():
    letter = raw_input("What letter would you like to guess?: ").lower()
    if letter == 'exit':
        return 'exit'
    if len(letter) > 1 or not letter.isalpha():
        print "That's not a single letter, try again."
        return ask_for_letter()
    else:
        return letter

def generate_body_part(num):
    side_post = " |    "

    body_parts = [' O', ' |', '/|\\', ' |', '/ \\']
    
    side_list = list(side_post)
    side_list[4] = body_parts[num]
    side_post = ''.join(side_list)
    return side_post
    
# FROM OTHER FILE
# def generate_body_part(num):
#     side_post = ' |   ! '
#     parts = [' O', ' |', '/|\\', ' |', '/ \\']
#     part_list = list(side_post)
#     part_list[5] = parts[num]
#     body_part = ''.join(part_list)
#     return body_part

# def print_hangman(pts):
#     top_post = '_______'
#     first_post = ' |    !'
#     bottom_post = '_|_____'
#     whole_enchilada = [top_post, first_post, bottom_post]
#     for i in range(pts):
#         whole_enchilada.insert(len(whole_enchilada)-1, generate_body_part(i))
#     
#     for x in whole_enchilada:
#         print x

def print_hangman(pts, wrong_letters):
    top_post = "______"
    first_side_post = " |   ! "
    side_post = " |    "
    bottom_post = "_|____ Letters guessed: {}".format(wrong_letters)

    whole_enchilada = [top_post, first_side_post, bottom_post]
    
    for i in range(pts): #3 (0, 1, 2)
        whole_enchilada.insert(len(whole_enchilada)-1, generate_body_part(i))
    
    for j in range(5-pts):
        whole_enchilada.insert(len(whole_enchilada)-1, side_post)
    
    for x in whole_enchilada:
        print x

def play_the_game():
    wrong_letters = []
    word = pick_a_word()
    answer = ['_' for x in word] # print with ' '.join(answer)
    mistake_pts = 0
    
    print ' '.join(answer), '\n'
    
    # while we haven't finished the word AND while hangman isn't dead
    while (''.join(answer).find('_') != -1) and mistake_pts < 5:
        letter = ask_for_letter()
        if letter == 'exit':
            return 
        if letter in word:
            if letter not in answer:
                idxs = [pos for pos, char in enumerate(word) if char == letter]
                for x in idxs:
                    answer[x] = word[x]
                print ' '.join(answer), '\n'
            else:
                print 'You already guessed that letter correctly, try again!'
                print ' '.join(answer), '\n'
        else:
            if letter in wrong_letters:
                print 'You already guess that letter incorrectly, try again!'
            else:
                wrong_letters.append(letter)
                mistake_pts += 1
                print ' '.join(answer)
                print_hangman(mistake_pts, wrong_letters)
                
    if mistake_pts == 5:
        print "Aw man, sorry! The word was {}.".format(word)
        return
    else:
        print "Congratulations, you saved him! You got the word, {}!".format(word)
        return

def play_hangman(have_played = 0):
    q_str = '' if have_played == 0 else ' again'
    
    is_play = raw_input("Hey, do you want to play Hangman{}? (Y/N): ".format(q_str)).upper()
    if is_play == 'N':
        print "Aw, maybe next time!"
        None
    elif is_play == 'Y':
        print "Awesome! Let's get started! Type exit to exit at any time."
        play_the_game()
        play_hangman(1)
    else:
        print "That.. was not a yes or no. Try again!"
        play_hangman(0)

play_hangman()
