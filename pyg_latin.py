pyg = 'ay'

original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
  # if word contains characters only characters
  word = original.lower() # convert to lowercase
  first = word[0] # take first letter of word
  new_word = word + first + pyg # combine elements
  new_word = new_word[1:len(new_word)] # remove first letter
  print new_word

else:
  print 'empty'
