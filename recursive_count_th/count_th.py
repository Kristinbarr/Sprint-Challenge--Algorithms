'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # initialize count
    count = 0
    
    # base case if word has no length
    if len(word) == 0:
        return count

    # increment count if first 2 letters are 'th'
    if 'th' in word[:2]:
        count += 1

    # add count to current scoped count to return it to the next instance
    count += count_th(word[1:])
    
    # return count
    return count
    

# print(count_th('abcthxyz'))