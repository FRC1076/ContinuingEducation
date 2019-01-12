def permutor(text, permutation):
    """
    The permutor function has two arguements. It takes the text and scrambles it according to what's inputted into the permutation arguement.
    """
    scrambled = ""
    for x in permutation:
        scrambled = scrambled + text[x]
    return scrambled

def decoder(permutator):
    pass
