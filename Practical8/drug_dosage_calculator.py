weight = float(input("What's your weight(kg)?"))
paracetamol = int(input("What's your paracetamol strength(mg/5ml)?\n120mg/5ml or 250mg/5ml"))

def dosage(weight, paracetamol):
    if paracetamol in [120, 250]:
        if 10 <= weight <=100:
            paracetamol_pre = weight * 15
            volume = paracetamol_pre / paracetamol * 5
        else:
        
            volume = 'Out of weight range.'
    else:
        volume = 'Out of paracetamol strength range.'
    return volume

print(f'Patient should take {dosage(weight, paracetamol)} ml of paracetamol.')