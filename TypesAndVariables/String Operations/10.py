###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title: ', movie.upper())

# print title in small letters
print('Title: ', movie.lower())

# print how many times the vowel "e" appears in the title
print('Number of "e" in the title: ', movie.count('e'))

# print where in the text is the word "Lord"
print('Where is the word "Lord": ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('Where is the word "dragon": ', movie.find('dragon'))