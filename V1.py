# DIT AS 92004

# ==========================
# Section 1: Name Input and Validation
# ==========================

# Name input and validation subroutine
def get_name():
    while True:
        sub_name = input("Enter your name: ")
        if len(sub_name) > 0:
            return sub_name 
        else:
            print("Invalid input. Please enter your name.")

# Subroutine to variable
name = get_name()

# ==========================
# Section 2: Age Input and Age Range Validation
# ==========================

# Age input and validation subroutine
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

# Subroutine to variable
age = get_age(name)

# Age range validation subroutine
def validate_age(age):
    if age < 12:
        print("Sorry, you must be 12 or older to participate.")
        exit()
    if age > 17:
        print("Sorry, you must be 17 or younger to participate.")
        exit()

# Validate age
validate_age(age)

# Blank line
print()


# ==========================
# Section 3: Activity Selection
# ==========================

# Activity print, input and validation subroutine
def choose_activity():

    # Activity options list
    activity_list = [
        'Music Jam Session (2 hours, easy, $5 fee)',
        'Science Experiments Lab (3 hours, moderate, $10 fee)',
        'Sports Leadership Training (4 hours, challenging, $12 fee)'
    ]

    # Activity options list print
    print('Choose an activity: ')
    print(f'1. {activity_list[0]}')
    print(f'2. {activity_list[1]}')
    print(f'3. {activity_list[2]}')

    # Activity input with validation
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

# Subroutine to variable
chosen_activity = choose_activity()

# Chosen activity calculations
if chosen_activity == 1:
    activity_fee = 5
    activity_duration = 2
    activity_name = 'Music Jam Session'
    activity_difficulty = 'easy'

elif chosen_activity == 2:
    activity_fee = 10
    activity_duration = 3
    activity_name = 'Science Experiments Lab'
    activity_difficulty = 'moderate'

elif chosen_activity == 3:
    activity_fee = 12
    activity_duration = 4
    activity_name = 'Sports Leadership Training'
    activity_difficulty = 'challenging'

# Blank line
print()


# ==========================
# Section 4: Meal Selection
# ==========================

# Meal print, input and validation subroutine
def sub_chosen_meal():
    # Meal options list
    meal_choice = ['Standard', 'Vegetarian', 'Dairy-free', 'Gluten-free','No meal']

    # Meal options list print
    print('Choose a meal option: ')
    print(f'1. {meal_choice[0]}')
    print(f'2. {meal_choice[1]}')
    print(f'3. {meal_choice[2]}')
    print(f'4. {meal_choice[3]}')
    print(f'5. {meal_choice[4]}')

    # Meal input with validation
    while True:
        try:
            chosen_meal = int(input("Enter the number of your chosen meal: "))
            if chosen_meal in [1, 2, 3, 4]:
                break
            if chosen_meal == 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return chosen_meal

# Subroutine to variable
chosen_meal = sub_chosen_meal()

# Meal options calculation subroutine
def sub_meal_choice(chosen_meal):
    if chosen_meal == 1:
        return 'Standard'
    elif chosen_meal == 2:
        return 'Vegetarian'
    elif chosen_meal == 3:
        return 'Dairy-free'
    elif chosen_meal == 4:
        return 'Gluten-free'
    elif chosen_meal == 5:
        return 'No meal'
    
# Subroutine to variable
meal_choice = sub_meal_choice(chosen_meal)

# Meal fee calculation
def sub_meal_fee(chosen_meal):
    if chosen_meal in [1, 2, 3, 4]: 
        return 7
    else:
        return 0


# Subroutine to variable
meal_fee = sub_meal_fee(chosen_meal)

# Total fee calculation
total_fee = activity_fee + meal_fee

# Blank line
print()


# ==========================
# Section 5: Summary and Final Decision
# ==========================

# Output
print(f'{name}, Aged {age}, has chosen the {activity_name} activity, which is {activity_difficulty} and lasts for {activity_duration} hours. You have chosen the {meal_choice} meal option. The total fee is ${total_fee}.')

# Final decision input and output
final_decision = input(f"Do you want to proceed with the payment of ${total_fee} (yes/no): ")

if final_decision.lower() == 'yes' or final_decision.lower() == "y":
    print("Payment accepted. Thank you!")
    exit()
else:
    print("Payment cancelled.")
    exit()