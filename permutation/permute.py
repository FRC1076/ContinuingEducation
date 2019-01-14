def permutor(text, permutation):
    """
    The permutor function has two arguements.
    It takes the text and scrambles it according to
    the permutation argument.
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
    Return True if all of the elements of permutation
    are present.  Otherwise return False.  Note,
    the empty array is a valid permutation.
    (works for an empty string)
    """
    pass

def get_permutatation_by_length(length, permutation_set):
    """
    A permutation set is an array of permutations.  Element i
    of the permutation array is the permutation for a string
    of length i.
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
    Just using some of the above functions to permute each word (using
    the appropriate permutor for the word length, and then
    joining them back into a sentence.
    """
    pass
