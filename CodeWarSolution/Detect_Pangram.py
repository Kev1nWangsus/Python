# Detect Pangram
# Check if string s contains all alphabet characters

import string

'''
orginal version
def is_pangram(s):
    return len(set(string.ascii_lowercase)) <= len(set(s.lower()))
'''

# Better one:
def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

# set operation "<=" checks if right side set contains all elements of left set
