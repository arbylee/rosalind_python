import random
import unittest
from rosalind import Rosalind

class TestRosalindSolutions(unittest.TestCase):
    def test_counting_nucleotides(self):
        input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        self.assertEqual((20,12,17,21), Rosalind().count_nucleotides(input))

    def test_rna_transcription(self):
        input = "GATGGAACTTGACTACGTAAATT"
        self.assertEqual('GAUGGAACUUGACUACGUAAAUU', Rosalind().rna_transcription(input))

if __name__ == '__main__':
    unittest.main()
