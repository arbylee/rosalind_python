class Rosalind:
    def count_nucleotides(self, dna_string):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        for nucleotide in dna_string:
            if nucleotide == 'A':
                a_count += 1
            if nucleotide == 'C':
                c_count += 1
            if nucleotide == 'G':
                g_count += 1
            if nucleotide == 'T':
                t_count += 1
        return a_count, c_count, g_count, t_count

    def rna_transcription(self, dna_string):
        resulting_rna = ""
        for nucleotide in dna_string:
            if nucleotide == 'G' or nucleotide == 'A' or nucleotide == 'C':
                resulting_rna += nucleotide
            if nucleotide == 'T':
                resulting_rna += 'U'
        return resulting_rna

