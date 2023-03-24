import math

while True:

    input_number = input('Pick a number between 2-10:')

    a = int(input_number)

    if a < 2 or a > 10:
            print('Try again!')
    else:
        break

b = ((a * 2) + 5 ) * 50
print('Step 1: Multiply your number by 2')
print('Step 2: Now add 5')
print('Step 3: Next multiply that by 50')

while True: 
        prior_upcoming = str(input('Has your birthday already passed this year? (Y/N):').capitalize())

        if (prior_upcoming == 'Y' or prior_upcoming == 'N'):
                break
        else:
                print('Please answer "Y" for Yes or "N" for No')


if prior_upcoming == 'Y':
        print('Step 4: Ok so add 1773 to your number')
        b += 1773
else:
        print('Step 4: Ok so add 1772 to your number')
        b += 1772

year_born = int(input('What year were you born? ex:(1999):'))

print('Nice, ok so now subtract the year you were born to your number')

c = (b - year_born)
cstr = str(c)

num = cstr[0]
age = cstr[-2:]

print('So let me get this straight...')
print('Your total number should be {}. However, the first digit(s) of that number which is {}, is you number you picked at the start.'.format(c, a))
print('Your age happens to be the last digit(s) of that number, so you are {} years old!'.format(age))

