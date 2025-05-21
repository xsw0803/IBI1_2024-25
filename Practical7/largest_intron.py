import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron = re.findall(r'GT.+AG', seq)
print(seq)
print(f'The intron sequence is {intron[0]}.')
print(f'The length of intron is {len(intron[0])} .')