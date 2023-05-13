ANNUAL_SALARY = 66569
TOTAL_COST = 1000000
SEMI_ANNUAL_RAISE = 0.07
PORTION_DOWN_PAYMENT = 0.25
R = 0.04

def current_savings(portion_saved):
    monthly_salary = ANNUAL_SALARY / 12
    current_savings = 0
    for month in range(36):
        current_savings += monthly_salary * portion_saved
        current_savings += current_savings * R / 12
        if month % 6 == 0 and month > 0:
            monthly_salary += monthly_salary * SEMI_ANNUAL_RAISE
    return current_savings

target = TOTAL_COST * PORTION_DOWN_PAYMENT
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = ((high + low) / 2) / 10000

while abs(current_savings(guess) - target) >= epsilon: 
    if current_savings(1) < target:
        print("It is not possible to pay the down payment in 3 years.")
        break
    if current_savings(guess) > target:
        high = guess * 10000
    else:
        low = guess * 10000
    guess = ((high + low) / 2) / 10000
    num_guesses += 1
    print(f"Number of guesses is {num_guesses}")
    print(f"{(round(guess, 4))} is close to the savings rate needed. ")
    print(f"Based on the code, the current savings after 36 months is: {current_savings(guess)}")

