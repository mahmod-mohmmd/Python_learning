def calculate_bonus(base_salary , performance_rating):
    if performance_rating == 5 :
        bonus_percentage = 0.20
    elif performance_rating >= 3  :
        bonus_percentage = 0.10        
    else :
        bonus_percentage = 0.0
        print ( "Needs Improvement")
    return base_salary * bonus_percentage
    
def calculate_tax(gross_salary):
    if gross_salary > 7000 :
        tax_percentage = 0.15
    elif gross_salary >= 3000 :
        tax_percentage = 0.10
    else:
        tax_percentage = 0.0
        print("Tax Exempt")
    return gross_salary * tax_percentage

def main_hr_app() :
    print("---🏢 Corporate Payroll System 🏢---")
    emp_name = input("Enter Employee Name: ").strip().title()
    base_salary = float(input("Enter Base Salary (EGP): "))
    performance_rating = int(input("Enter Performance Rating (1-5): "))
    if performance_rating < 1 or performance_rating > 5 or base_salary < 0 :
        print("❌Invalid data entered. Please restart and check your inputs.")
        return 
    
    
    bonus = calculate_bonus(base_salary , performance_rating )
    gross_salary = base_salary + bonus 
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax 
    
    print("\n" + "="*40)
    print(f"📄 PAYROLL STATEMENT FOR: {emp_name}")
    print("="*40)
    print(f"• Base Salary:       {base_salary:.2f} EGP")
    print(f"• Earned Bonus:      {bonus:.2f} EGP")
    print(f"• Tax Deductions:    {tax:.2f} EGP")
    print("-" * 40)
    print(f"💰 NET PAYABLE CASH: {net_salary:.2f} EGP")
    print("="*40)
    
main_hr_app()
