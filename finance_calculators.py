import math

"""
Allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator 
"""


# Check empty value function
def check_empty(value):
    length_of_value = len(value)
    if length_of_value > 0:
        return True
    else:
        print(f"The value is empty.")
        return False


# return integer value
def get_int(value) -> int:
    if check_empty(value):
        try:
            return int(value)
        except:
            return -1
    else:
        return -1


# return float value
def get_float(value) -> float:
    if check_empty(value):
        try:
            return float(value)
        except:
            return -1
    else:
        return -1  # Correct the unreachable code 15-04-2024


# Calculate bond repayment function
# return monthly bond repayment
# repayment = (i * P) / (1 - (1 + i) ** (-n))
def calculate_repayment(amount: float, interest_rate: float, months: int) -> float:
    P = amount
    i = (interest_rate / 12) / 100
    n = months
    return (i * P) / (1 - (1 + i) ** (-n))


# calculate simple interest function
# return total amount
# A = P(1 + r x t)
def simple_interest(amount: float, interest_rate: float, year: int) -> float:
    r = interest_rate / 100
    P = amount
    t = year
    return P * (1 + r * t)


# calculate compound interest function
# return total amount
# A = P(1 + r)t
def compound_interest(amount: float, interest_rate: float, year: int) -> float:
    r = interest_rate / 100
    P = amount
    t = year
    return P * math.pow((1 + r), t)


# bond function
def bond():
    amount = get_float(input("Please enter the present value of the house : £")) # Add currency symbol 15-04-2024
    interest_rate = get_float(input("Please enter the interest rate (only the number) : ").strip("%"))
    months = get_int(input("Please enter the number of months you plan to take to repay the bond : "))

    if amount > 0 and interest_rate > 0 and months > 0:
        repayment = calculate_repayment(amount, interest_rate, months)
        print(f"The value of the house: £{amount}") # Add currency symbol 15-04-2024
        print(f"interest rate : {interest_rate}%")
        print(f"No. of months : {months}")
        print(f"You will have to repay each month : £{repayment:.2f}") # Add currency symbol 15-04-2024

    else:
        print("System can't calculate the bond repayment.")


# investment function
def investment():
    total_amount = 0
    count = 0

    amount = get_float(input("Please enter the amount of money that you are depositing : £")) # Add currency symbol 15-04-2024
    interest_rate = get_float(input("Please enter the interest rate (only the number): ").strip("%"))
    year = get_int(input("Please enter the number of years you plan on investing: "))

    if amount >= 0 and interest_rate >= 0 and year >= 0:

        while True:

            interest = input("Please enter either 'simple' or 'compound' interest : ")
            interest = interest.lower().strip()

            if interest == "simple":
                total_amount = simple_interest(amount, interest_rate, year)
                break  # Remove the ; 15-04-2024
            elif interest == "compound":
                total_amount = compound_interest(amount, interest_rate, year)
                break # Remove the ; 15-04-2024
            else:
                count += 1
                if count == 3:
                    print("You attempt more then 3 times. End the program.")
                    break # Remove the ; 15-04-2024

                print("You should enter either 'simple' or 'compound'") # Correct the unreachable code 15-04-2024

        if total_amount > 0:
            print(f"----- {interest} interest ----- ")
            print(f"Deposit amount : £{amount} ") # Add currency symbol 15-04-2024
            print(f"interest rate : {interest_rate}%")
            print(f"No. of years : {year} ")
            print(f"The total amount of {interest} interest: £{total_amount:.2f} ") # Add currency symbol 15-04-2024

        else:
            print("System can't calculate the investment.")

    else:
        print("System can't calculate the investment.")


# Start the program
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home lay")
program_end_count = 0

while True:

    menu = input("Please enter either 'investment' or 'bond' from the menu above to proceed : ")
    lower_menu = menu.lower().strip()

    match lower_menu:
        case 'investment':
            print("------ Investment ------")
            investment()
            break # Remove the ; 15-04-2024
        case 'bond':
            print("------ Bond ------")
            bond()
            break # Remove the ; 15-04-2024
        case other:
            print("You should enter either 'investment' or 'bond'")
            program_end_count += 1
            if program_end_count == 3:
                print("You attempt more then 3 times. End the program.")
                exit() # Remove the ; 15-04-2024
