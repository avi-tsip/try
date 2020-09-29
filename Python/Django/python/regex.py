import re

patters = ['term1', 'term2']
text = 'this is a string with term1 but not the second one'

"""Find the matching word and its start and end index"""
for word in patters:
    match = re.search(word, text)
    print(f'I am searching for {word}')
    if (match):
        print(f'We got a match for {word}! starting at index {match.start()} and ends at {match.end()}')
    else:
        print(f'No match for {word}')

"""Find all instances of a pattern"""
print(re.findall('match', 'this function looking to match the phrase I need to find a match inside'))

"""Metacharacters"""
def multiReFind(patterns, phrase):
    for pat in patterns:
        print(f'Searching for patthern {pat}')
        print(re.findall(pat, phrase))
        print('\n')

# Repetition
# Looking for s followed by 0 or more d's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['sd*']
multiReFind(test_pattern,test_phrase)

# Looking for s followed by 1 or more d's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['sd+']
multiReFind(test_pattern,test_phrase)

# Looking for s followed by 0 or 1 d's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['sd?']
multiReFind(test_pattern,test_phrase)

# Looking for s followed by 3 d's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['sd{3}']
multiReFind(test_pattern,test_phrase)

# Looking for s followed by 1 or 3 d's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['sd{1, 3}']
multiReFind(test_pattern,test_phrase)

# Looking for s followed by 1 or 0 d's or s's
test_phrase = 'sssddd..dd.sss.dd.ss.dsdsdsds.'
test_pattern = ['s[sd]+']
multiReFind(test_pattern,test_phrase)

#Excluding terms (!?.) 0 or 1 times
phrase = 'This is a new phrase. But it has punctuation. How can I remove it?'
test_pattern = ['[^!?.+]']
multiReFind(test_pattern, phrase)

# Return only lower case
phrase = 'This is a new phrase. But it has punctuation. How can I remove it?'
test_pattern = ['[a-z]+']
multiReFind(test_pattern, phrase)

# Return only Upper case
phrase = 'This is a new phrase. But it has punctuation. How can I remove it?'
test_pattern = ['[A-Z]+']
multiReFind(test_pattern, phrase)

# Return only digits
phrase = 'This has numbers: 123456 and symbols like #hashtag?'
test_pattern = [r'\d+']
multiReFind(test_pattern, phrase)

# Return only Non digits
phrase = 'This has numbers: 123456 and symbols like #hashtag?'
test_pattern = [r'\D+']
multiReFind(test_pattern, phrase)

# Return only white spaces
phrase = 'This has numbers: 123456 and symbols like #hashtag?'
test_pattern = [r'\s+']
multiReFind(test_pattern, phrase)

# [r'\S+'] will return non white space
# [r'\w+'] will return alpha numberic characters
# [r'\W+'] will return NON alpha numberic characters