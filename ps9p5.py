def calculate_tuition(credit_hours, district_code):
    if district_code == 'I':
        tuition_rate = 250
    elif district_code == 'O':
        tuition_rate = 550
    else:
        print("Invalid district code!")
        return
    tuition_owed = credit_hours * tuition_rate
    return tuition_owed
last_name = input("Enter student's last name: ")
credit_hours = int(input("Enter credit hours: "))
district_code = input("Enter district code (I or O): ")
tuition_owed = calculate_tuition(credit_hours, district_code)
print(f"Student name: {last_name}")
print(f"Tuition owed: ${tuition_owed}")