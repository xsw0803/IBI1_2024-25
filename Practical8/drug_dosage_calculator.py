weight = float(input("What's your weight(kg)?"))

paracetamol = 120

def dosage(weight, paracetamol):
    if 10 <= weight <=100:
        paracetamol_pre = weight * 15
        volume = (paracetamol_pre // paracetamol)
    else:
        print('Out range of weight.')
        volume = 'Out range of weight'
    return volume

print(dosage(weight, paracetamol))