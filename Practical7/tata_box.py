import re
import pandas as pd

input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open('tata_genes.fa', 'w')
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

for gene_seq in gene['Gene sequence']:
    if re.search(r'TATA[A|T]A[A|T]', gene_seq):
        tata_gene_name = gene.loc[gene['Gene sequence'] == gene_seq, 'Gene name'].iloc[0]
        output.write(f'>{tata_gene_name}\n')
        output.write(f'{gene_seq}\n')
        
input.close()
output.close()

    