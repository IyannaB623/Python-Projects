import string

while True:

    password = input('Enter your password:')
    strength = 0
    uppercase_count = 0
    lowercase_count = 0
    specialchar_count = 0
    digit_count = 0
    password_length = len(password)
    notes = ''

    for x in password:
        if x in string.ascii_lowercase:
            lowercase_count += 1
        elif x in string.ascii_uppercase:
            uppercase_count += 1
        elif x in string.digits:
            digit_count += 1
        elif x in string.punctuation:
            specialchar_count += 1
        else:
            print('')
                    
            #print('lower:{}, upper:{}, digits:{}, specialchar:{}, passwordlength:{}'.format(lowercase_count, uppercase_count, digit_count, specialchar_count, password_length))
            # check if variables are counting correctly ^

    if uppercase_count >= 1:
        strength += 1
    if lowercase_count >= 1:
        strength += 1
    if specialchar_count >= 1:
        strength += 1
    if digit_count >= 1:
        strength += 1
    if password_length >= 8:
        strength += 1

    if strength < 5:
        notes += 'Notes:'
    if uppercase_count == 0:
        notes += ' + include at least one uppercase letter'
    if lowercase_count == 0:
        notes += ' + include at least lowercase letter missing'
    if digit_count == 0:
        notes += ' + include at least one number'
    if specialchar_count == 0:
        notes += ' + inlcude at least one special character'
    if password_length < 8:
        notes += ' + password length needs to be atleast 8 characters long'

    if strength >= 5:
        print('Excellent! Your password is very strong!')
    elif strength < 5:
        print('You recieved a score of {}/5 for password strength. Refer to the following notes to help strengthen your password. {}'.format(strength, notes))\

    check_again = input('Would you like to input another password(Y/N):')
    yes_no = check_again.upper()        

    if(yes_no == 'N'):
        print('Cool Beans!')
        break

