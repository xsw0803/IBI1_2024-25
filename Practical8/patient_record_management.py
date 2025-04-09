class patients:
    def __init__(self, name, age, date_last, medical_history):
        self.name = name
        self.age = age
        self.date_last = date_last
        self.medical_history = medical_history
    
    def detail(name, age, date_last, medical_history):
        print(f'Name: {name}\t\tAge: {age}\t\tLast submission date: {date_last}\t\tMedical history: {medical_history}')

patients.detail(input("What's your name?"), 
                input("What's you age?"), 
                input("What's your last submission date?"), 
                input("What's your medical history?"))
