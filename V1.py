# ==========================
# Section 1: Name Input
# ==========================
def get_name():
    while True:
        sub_name = input("Enter your name: ")
        if len(sub_name) > 0:
            return sub_name 
        else:
            print("Invalid input. Please enter your name.")

# ==========================
# Section 2: Age Input and Validation
# ==========================
def get_age(name):
    while True:
        try:
            age = int(input(f"Hi {name}, please enter your age: "))
            if age > 0:
                return age
            else:
                print("Invalid input. Age must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number for your age.")

def validate_age(age):
    if age < 12:
        print("Sorry, you must be 12 or older to participate.")
        exit()
    if age > 17:
        print("Sorry, you must be 17 or younger to participate.")
        exit()

# Blank line
print()

# ==========================
# Section 3: Activity Selection
# ==========================

def choose_activity(chosen_activity):
    activity_list = [
        'Music Jam Session (2 hours, easy, $5 fee)',
        'Science Experiments Lab (3 hours, moderate, $10 fee)',
        'Sports Leadership Training (4 hours, challenging, $12 fee)'
    ]

    print('Choose an activity: ')
    print(f'1. {activity_list[0]}')
    print(f'2. {activity_list[1]}')
    print(f'3. {activity_list[2]}')

    while True:
        try:
            chosen_activity = int(input("Enter the number of your chosen activity: "))
            if chosen_activity in [1, 2, 3]:
                return chosen_activity
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



 # Chosen activity fee calculation

chosen_activity = choose_activity()

# Chosen activity fee calculation
if chosen_activity == 1:
    activity_fee = 5
elif chosen_activity == 2:
    activity_fee = 10
elif chosen_activity == 3:
    activity_fee = 12

# Chosen activity duration calculation
if chosen_activity == 1:
    activity_duration = 2
elif chosen_activity == 2:
    activity_duration = 3
elif chosen_activity == 3:
    activity_duration = 4

# Chosen activity name calculation
if chosen_activity == 1:
    activity_name = 'Music Jam Session'
elif chosen_activity == 2:
    activity_name = 'Science Experiments Lab'
elif chosen_activity == 3:
    activity_name = 'Sports Leadership Training'

# Chosen activity difficulty calculation
if chosen_activity == 1:
    activity_difficulty = 'easy'
elif chosen_activity == 2:
    activity_difficulty = 'moderate'
elif chosen_activity == 3:
    activity_difficulty = 'challenging'

# Blank line
print()

# ==========================
# Section 4: Meal Selection
# ==========================
def chosse_meal():
    # Meal options list
    meal_options = ['Standard', 'Vegetarian', 'Dairy-free', 'Gluten-free','No meal']

    # Meal options list print
    print('Choose a meal option: ')
    print(f'1. {meal_options[0]}')
    print(f'2. {meal_options[1]}')
    print(f'3. {meal_options[2]}')
    print(f'4. {meal_options[3]}')
    print(f'5. {meal_options[4]}')

    # Meal input with validation
    while True:
        try:
            chosen_meal = int(input("Enter the number of your chosen meal: "))
            if chosen_meal in [1, 2, 3, 4]:
                meal_fee = 7
                break
            if chosen_meal == 5:
                meal_fee = 0
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

chosen_meal = chosse_meal()

# Chosen meal fee calculation
if chosen_meal == 1 or chosen_meal == 2 or chosen_meal == 3 or chosen_meal == 4: 
    meal_fee = 7
else:
    meal_fee = 0

# Total fee calculation
total_fee = activity_fee + meal_fee

# Blank line
print()

# ==========================
# Section 5: Summary and Final Decision
# ==========================

name = get_name()
age = get_age(name)

# Output
print(f'{name}, Aged {age}, has chosen the {activity_name} activity, which is {activity_difficulty} and lasts for {activity_duration} hours. You have chosen the {meal_options[chosen_meal - 1]} meal option. The total fee is ${total_fee}.')

# final decision input and output
final_decision = input(f"Do you want to proceed with the payment of ${total_fee} (yes/no): ")

if final_decision.lower() == 'yes' or final_decision.lower() == "y":
    print("Payment accepted. Thank you!")
    exit()
else:
    print("Payment cancelled.")
    exit()




# ==========================
# Main Program
# ==========================

# Subroutine to name variable
name = get_name()

# Subroutine to age variable
age = get_age(name)

# Age validation
validate_age(age)

# Blank line
print()

# Activity input
chosen_activity = choose_activity()

# Get activity details
activity_name, activity_duration, activity_difficulty, activity_fee = get_activity_details(chosen_activity)

# Blank line
print()

# Meal selection
chosen_meal, meal_choice, meal_fee = choose_meal()

# Total fee calculation
total_fee = activity_fee + meal_fee

# Blank line
print()

# Summary
display_summary(name, age, activity_name, activity_difficulty, activity_duration, meal_choice, total_fee)

# Final decision
confirm_payment(total_fee)
# ==========================