class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search_by_disease(patients, disease):
    result = []
    for patient in patients:
        if patient.disease == disease:
            result.append(patient.name)
    return result

patients_data = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

patients = [Patient(patient["Name"], patient["Age"], patient["Disease"]) for patient in patients_data]

search_disease = "Flu"
patients_with_disease = search_by_disease(patients, search_disease)

print(f"Patients with {search_disease}: {patients_with_disease}")
