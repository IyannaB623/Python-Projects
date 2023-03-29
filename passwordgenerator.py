import string
import random

uppercase1 = random.choice(string.ascii_uppercase)
lowercase1 = random.choice(string.ascii_lowercase)
lowercase2 = random.choice(string.ascii_lowercase)
lowercase3 = random.choice(string.ascii_lowercase)
lowercase4 = random.choice(string.ascii_lowercase)
digits = ['0','1','2','3','4','5','6','7','8','9']
digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))
specialchar1 = random.choice(string.punctuation)

print('Welcome to the Password Generator!')
print('You can have two options of how your password will be generated')

while True:
    print('Option 1: A fully generated password')
    print('Option 2: A custom generated password with any special words, characters, or numbers you would like your password to have')
    option_choice =  int(input("Enter '1' for Option 1 or '2' for Option 2:"))
    print(option_choice)

    def fullygenerated():

        password = uppercase1 + lowercase1 + lowercase2 + lowercase3 + lowercase4 + digit1 + digit2 + specialchar1 

        print('With Option 1, your password is: {}'.format(password))

    def customgenerated():
        
        original_specialword = input('What word would you like your password to have?:')
        specialword = original_specialword
        missing_lower = 0
        missing_upper = 0
        missing_specialchar = 0
        missing_digits = 0
        missing_length = 0
        word_length = len(specialword)

        for x in specialword:

            if x in string.ascii_lowercase:
                missing_lower += 1
            if x in string.ascii_uppercase:
                missing_upper += 1
            if x in string.punctuation:
                missing_specialchar += 1
            if x in digits:
                missing_digits += 1
            if word_length < 8:
                missing_length += 1

        if missing_lower == 0:
            specialword += lowercase1
        if missing_upper == 0:
            specialword += uppercase1
        if missing_specialchar == 0:
            specialword += specialchar1
        if missing_digits == 0:
            specialword += digit1      
                
        y = len(specialword)
        
        while y < 8:
            y += 1
            specialword += digit2
                
        password = specialword 
        
        if original_specialword == password:
            print('You already have a strong password! You can keep it as is: {}'.format(password))
        else:
            print('With Option 2, your password is: {}'.format(password))

    if option_choice == 1:
        fullygenerated()
    if option_choice == 2:
        customgenerated()

    new_password = input('Would you like to generate another password?(Y/N)').upper()
    
    if(new_password == 'N'):
        break