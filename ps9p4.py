def get_pay_rate(job_code):
    """
    Determine the pay rate based on job code.
    """
    if job_code == 'L':
        return 25
    elif job_code == 'A':
        return 30
    elif job_code == 'J':
        return 50
    else:
        return 0
def get_gross_pay(hours_worked, pay_rate):
    """
    Determine the gross pay based on hours worked and pay rate.
    """
    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate
    else:
        overtime_hours = hours_worked - 40
        gross_pay = 40 * pay_rate + overtime_hours * 1.5 * pay_rate
    return gross_pay
last_name = input("Enter last name: ")
job_code = input("Enter job code (L, A, or J): ")
hours_worked = float(input("Enter hours worked: "))
pay_rate = get_pay_rate(job_code)
if pay_rate == 0:
    print("Invalid job code.")
else:
    gross_pay = get_gross_pay(hours_worked, pay_rate)
    print("Last name:", last_name)
    print("Gross pay: $", format(gross_pay, '.2f'), sep='')