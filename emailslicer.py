email = input('Enter your email:').strip()
indexref = email.index('@')
username = email[:indexref]
domain = email[indexref + 1:]

print('Your user name is {}, and your domain is {}'.format(username,domain))


