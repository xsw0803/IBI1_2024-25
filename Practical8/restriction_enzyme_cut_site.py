import re
DNA_seq = 'ATCGGATCGGTAGACTAGAACTGATACGTAACGTACCCAAAAGTACAGTA'
recognition_seq = 'GATCG'

def cut_position(DNA_seq, recognition_seq):
    count = 0
    length = len(DNA_seq)
    reco_length = len(recognition_seq)
    judge = True
    for i in range(0, len(DNA_seq)):
        if DNA_seq[i] not in ['A', 'G', 'T', 'C']:
            unexpected = True
    if unexpected == True:
        print('Unexpected nucleotides in the sequence.')
        judge = False
    if judge == True:
        for i in range(0, length - reco_length + 1):
            if DNA_seq[i:i + reco_length] == recognition_seq:
                print(f'The cut position is the {i + 1}th nucleotide "{DNA_seq[i]}".')
                count += 1
        if count == 0:
            print('No cut position matches.')

cut_position(DNA_seq, recognition_seq)

