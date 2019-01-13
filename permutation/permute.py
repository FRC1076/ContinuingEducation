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

def decoder(permutator):
    def decoder(permutation):
    depermutation = []
    for x in range (0, len (permutation)):
        depermutation.append (permutation.index(x))
    return depermutation
