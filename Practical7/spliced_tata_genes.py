import re
import pandas as pd
prompt = 'Which slice do you want?'
prompt += '\nGTAG or GCAG or ATAC:'
print(prompt)
user_input = str(input())

input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open(f'{user_input}_spliced_genes.fa', 'w')

seq = ''
gene = pd.DataFrame(columns=['Gene name', 'Gene sequence'])
for line in input:
    if re.search(r'>', line):
        name = re.findall(r'gene:(.*?)\s', line)[0]
        gene.loc[len(gene['Gene name'])] = [name, '']
        seq = ''
    else:
        seq += line.rstrip()
        gene.loc[len(gene['Gene name'])-1, 'Gene sequence'] = seq

def count_tata(seq):
    length = 7
    count = 0
    for u in range(len(seq) - length + 1):
        seq_check = seq[u:u + length]
        if re.search(r'TATA[A|T]A[A|T]', seq_check):
            count += 1
    return count

for gene_seq in gene['Gene sequence']:
    if re.search(r'TATA[A|T]A[A|T]', gene_seq):
        if re.search(user_input[:2]+r'.+'+user_input[-2:], gene_seq):
            gene_name = f'>{gene.loc[gene['Gene sequence'] == gene_seq, 'Gene name'].iloc[0]}'
            output.write(f'{gene_name}\tNumber of TATA box is {count_tata(gene_seq)}.\n')
            output.write(f'{gene_seq}\n')
            continue