def permutor(text, permutation):
    """
    The permutor function has two arguements.
    It takes the text and scrambles it according to
    the permutation arguement.
    """
    scrambled = ""
    for x in permutation:
        scrambled = scrambled + text[x]
    return scrambled

def decoder(permutation):
    """
    decoder takes a permutation array and returns the
    corresponding depermutation array necessary to decode
    a permuted string
    """
    depermutation = []
    for x in range (0, len (permutation)):
        depermutation.append (permutation.index(x))
    return depermutation

def permutation_is_valid(permutation):
    """
    Return True if all of the elements of permutation appropriate
    for the length are present.  Otherwise return False.  Note,
    the empty array is a valid permutation.
    """
    pass

def permute_sentence(sentence, permutation_set):
    """
    Using the appropriate permutation in the permutation set,
    permute each word of the string sentence.

    Hint:   Use split and join to break the sentence into an
    array of strings, and join to put back together as a string.
    >>> sentence = "These are the times that try folks souls."
    >>> words = sentence.split(' ')
    >>> words
    ['These', 'are', 'the', 'times', 'that', 'try', 'folks', 'souls.']
    >>> ' '.join(words)
    'These are the times that try folks souls.'

    Remember, this is like an accumulate with a loop kind of function.
    Just using some of the above functions.
    """
    pass
