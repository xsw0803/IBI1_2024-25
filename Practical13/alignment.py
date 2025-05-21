import os
import re
from Bio.Align import substitution_matrices
from Bio.Align import PairwiseAligner

'''os.chdir('/Users/xsw0803/Desktop/Programme/IBI_practicals/IBI1_2024-25/Practical13')'''
input = open('Sequence.fa')
matrix = substitution_matrices.load("BLOSUM62")
aligner = PairwiseAligner()
aligner.substitution_matrix = matrix

sequence = {}
seq_list = []
for line in input:
    if not re.search(r'>', line):
        seq = line.rstrip()
        seq_list.append(seq)
        sequence[seq] = seq_name
    else:
        seq_name = re.findall(r'>(.*)', line.rstrip())[0]

def compare(seq1, seq2, identical=0, score=0):
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            score += matrix[seq1[i]][seq2[i]]
        else:
            identical += 1
            score += matrix[seq1[i]][seq2[i]]
    return score, identical

for i in range(len(seq_list)):
    if i != 2:
        seq1 = seq_list[i]
        seq2 = seq_list[i+1]
    else:
        seq1 = seq_list[i]
        seq2 = seq_list[i-2]
    score_sum, identical = compare(seq1, seq2, identical=0, score=0)    
    percentage = f'{identical / len(seq_list[0]):.2%}'
    print(f'For the {sequence[seq1]} and {sequence[seq2]}:\nThe identical percentage is {percentage}.')
    print(f'The score is {score_sum}.\n')

'''
1. Length and subcellular localisation of human Sod2
    Length = 222 amino acids
    Localization: Mitochondria

2. The range of	percentage identities in the reported online BLAST results:
    Range = 58.1% ~ 100%

3. Comparison analysis
SODM_HUMAN and SODM_MOUSE:
Identical percentage = 90.09%
Score = 1097.0
SODM_HUMAN and random:
Idnetical percentage = 4.95%
Score = -260.0
SODUM_MOUSE and random:
Idnetical percentage = 4.50%
Score = -262.0

4. Huamn and mouse SODM sequences are mostly related.
'''
