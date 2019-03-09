import unittest

from permute import permutor, decoder, permutation_is_valid
 
class PermutationTest(unittest.TestCase):
    def test_permutor_Hello(self):
        self.assertEqual(permutor('Hello',[2,0,3,1,4]), "lHleo")

    def test_permutor_YowzahBang(self):
        self.assertEqual(permutor('Yowzah!', [ 4, 2, 0, 3, 5, 1, 6 ]), 'awYzho!')

    def test_decoder5(self):
        self.assertEqual(decoder([2,0,3,1,4]), [1, 3, 0, 2, 4])

    def test_decoder17(self):
        perm = [ 2, 3, 4, 7, 8, 9, 14, 15, 16, 0, 10, 11, 5, 6, 12, 1, 13]
        dec = decoder(perm)
        self.assertEqual(dec, [9, 15, 0, 1, 2, 12, 13, 3, 4, 5, 10, 11, 14, 16, 6, 7, 8])

    def test_permutor17(self):
        perm = [ 2, 3, 4, 7, 8, 9, 14, 15, 16, 0, 10, 11, 5, 6, 12, 1, 13]
        self.assertEqual(permutor('Conflagrationator', perm), 'nflrattorCioagnoa')

    def test_round_trip(self):
        p9 = [ 2, 5, 6, 3, 8, 1, 4, 0, 7 ]
        text = 'NineChars'
        self.assertEqual(permutor(permutor(text,p9), decoder(p9)), text)

    def test_round_trip_empty(self):
        p = [ ]
        text = ""
        self.assertEqual(permutor(permutor(text, p), decoder(p)), text)

    def test_permutation_missing_one_extra_two(self):
        p = [ 0, 2, 2 ]
        self.assertEqual(permutation_is_valid(p), False)

    def test_permutation_missing(self):
        p = [ 3, 2, 4, 5 ]
        self.assertEqual(permutation_is_valid(p), False)

    def test_permutation_valid_empty(self):
        p = [ ]
        self.assertEqual(permutation_is_valid(p), True)

    def test_permutation_valid_8_long(self):
        p = [ 2, 1, 4, 5, 3, 7, 6, 0 ]
        self.assertEqual(permutation_is_valid(p), True)

if __name__ == '__main__':
    unittest.main()

