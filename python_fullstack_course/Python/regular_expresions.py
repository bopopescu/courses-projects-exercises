import re

# patterns = ['term1', 'term2']

# text = 'This is a string with term1, not the other!'

# for pattern in patterns:
#     print('I am searching for: '+pattern)

#     if re.search(pattern,text):
#         print('MATCH!')
#     else:
#         print("NO MATCH!")


# match = re.search("term1", text)

# # print(match.start())

# print(re.findall('match','test phrase match in match middle'))

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns = ['[^!.?]+']

multi_re_find(test_patterns, test_phrase)