#TIM LUCAS
#LAB 2
#2025 06 10

MARBLE_COST = 1.20

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

marble_quantity = int(input("Enter the number of marbles you wish to purchase: "))

total_cost = MARBLE_COST * marble_quantity

print(f"\n\nOrder prepared for {first_name} {last_name}")
print(f"\n{marble_quantity} marbles ordered @ ${MARBLE_COST:.2f}")
print(f"\nTotal cost is ${total_cost:.2f}")