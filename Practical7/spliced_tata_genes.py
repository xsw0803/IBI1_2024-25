import re
prompt = 'Which slice do you want?'
prompt += '\nGTAG or GCAG or ATAC.'
print(prompt)
user_input = str(input())
input = open('tata_genes.fa', 'r')
output = open(f'{user_input}_spliced_genes.fa', 'w')

donor = user_input[:2]
acceptor = user_input[-2:]
print(donor, acceptor)

sliced_list = []
name_list = []
for line in input:
    if not re.search(r'>', line):
        sliced_seq = re.findall(donor+r'.+'+acceptor, line)
        for i in sliced_seq:
            sliced_list.append(i)
        if not re.findall(donor+r'.+'+acceptor, line):
            name_list.pop()
    else:
        name_list.append(line)
    
print(len(name_list))
print(len(sliced_list))

def count_tata(seq):
    length = 7
    count = 0
    for u in range(len(seq) - length + 1):
        seq_check = seq[u:u + length]
        if re.search(r'TATA[A|T]A[A|T]', seq_check):
            count += 1
    return count

t = 0
for i in sliced_list:
    t += 1
    if t == 1:
        if re.search(r'TATA[A|T]A[A|T]', i):
            output.write(f'{name_list[t-1][:-1]}  Number of TATA box instances is {count_tata(i)}.\n')
            output.write(i)
    else:
        if re.search(r'TATA[A|T]A[A|T]', i):
            output.write(f'\n{name_list[t-1][:-1]}  Number of TATA box instances is {count_tata(i)}.\n')
            output.write(i)
