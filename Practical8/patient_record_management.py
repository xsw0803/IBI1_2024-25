class patients:
    def __init__(self, name, age, date_last, medical_history):
        self.name = name
        self.age = age
        self.date_last = date_last
        self.medical_history = medical_history
    
    def detail(name, age, date_last, medical_history):
        print(f'{name}\t{age}\t{date_last}\t{medical_history}')

patients.detail('Jack', 18, '2025.04.06', 'A fever last week.')
