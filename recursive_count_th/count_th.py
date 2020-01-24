'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # base case: if word length is less than 2
    if len(word) < 2:
      return 0

    count = 0

    # then recurse with the rest of the word -1 character
    remaining_word = word[1:]
    count = count_th(remaining_word)

    # callstack unwinds and then counts the chars
    # if first 2 letters of the word are 'th', count+1
    if word[:2] == 'th':
      count += 1

    return count
