import random

word_bank = [
'apple'
'cakes', 
'heart', 
'kitty',
'cheer', 
'pause', 
'legal', 
'plate', 
'error', 
'apple',
'beach',
'brain',
'bread',
'brush',
'chair',
'chest',
'chord',
'clock',
'cloud',
'heart',
'house',
'juice',
'light',
'money',
'music',
'party',
'pizza',
'plant',
'radio',
'river',
'salad',
'sheep',
'shoes',
'smile',
'snack',
'snake',
'spice',
'tiger',
'train',
'water',
'whale',
'wheel',
'woman',
'world',
'write',
'youth'
]

used_words = []
word = random.choice(word_bank)
final = word.capitalize()
attempts = 10

while(True):

    while(True):
        guess = input('Your guess:').lower()
            
        if(len(guess) != 5):
                print('Please enter a 5 letter word')
        if(guess in used_words):
                print('You already used that word! Try again.')
        else:
            break
        
    index = ''
    correct_index = 0
    correct_letters = 0


    if(guess[0] == word[0]):
        correct_index += 1 
        index += ' Index 1 is correct.'
    if(guess[1] == word[1]):
        correct_index += 1
        index += ' Index 2 is correct.'
    if(guess[2] == word[2]):
        correct_index += 1
        index += ' Index 3 is correct.'
    if(guess[3] == word[3]): 
        correct_index += 1   
        index += ' Index 4 is correct.'
    if(guess[4] == word[4]): 
        correct_index += 1
        index += ' Index 5 is correct.'


    for x in word:
        if x in guess:
            correct_letters += 1
    
    attempts -= 1
    used_words.append(guess) 

    print('correct letters: {}, correct indexes: {} -{} tries left:{}'. format(correct_letters, correct_index, index, attempts))
    
    if correct_letters == 5 and correct_index == 5: 
        print('You win the word is {}!'.format(final))
        break
    if attempts < 1:
        print('You have ran out of attemps. The word was {}.'.format(final))
        break