import re
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open('pre_data.fa', 'w')
name_list = []
seq = []

t = 0
for line in input:
    t +=1
    if t == 1:
        name1 = re.sub(r'>.+gene:', '', line)
        name = re.sub(r'gene_.+]', '', name1)
        output.write(f'>{name}')
        name_list.append(f'{name}')
    else:
        if re.search(r'>', line):
            if re.search(r'_mRNA', line):
                name = re.sub(r'_mRNA.+]', '', line)
                output.write(f'\n{name}')
                name_list.append(f'{name}')
            else:
                name = re.sub(r'\s.+?]', '', line)
                output.write(f'\n>{name}')
                name_list.append(f'{name}')
        else:
            sequence = line[:-1]
            output.write(f'{sequence}') 
input.close()
output.close()

input2 = open('pre_data.fa', 'r')
output2 = open('tata_genes.fa', 'w')

t = 0
for line in input2:
    print(line)
    if not re.search(r'>', line):
        t += 1
        seq.append(line)
        if re.search(r'TATA[A|T]A[A|T]', line):
            output2.write(f'{name_list[t-1]}')
            output2.write(f'{seq[t-1]}')

    