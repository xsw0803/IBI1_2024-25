import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
intron = re.findall(r'GT.+AG', seq)
print(seq)
print(intron)
print(f'The length of intron is {len(intron[0])} .')