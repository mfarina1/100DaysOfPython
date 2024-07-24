# Returns True/False - two strings are anagrams (assume input consists of alphabets only)


def count_letters(str):
    ''' 
    Returns a dictionary which maps each letter in a string to the number of times it appears in the string.
    '''
    d = {}
    for i in str.lower():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


def anagram(str1, str2) -> bool:
    '''
    Returns true if two strings are anagrams of each other and false otherwise.
    '''
    if len(str1) != len(str2):
        return False
    elif str1 == str2:
        return True
    return count_letters(str1) == count_letters(str2)
        

if __name__ == '__main__':
    str1 = "beata"
    str2 = "abeta"
    
    print("result: ", anagram(str1, str2))

    str3 = "gOd"
    str4 = "doG"

    print("result 2: ", anagram(str3, str4))

    str5 = "taco"
    str6 = "cat"
     
    print('result 3: ', anagram(str5, str6))