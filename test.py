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

# ==========================
# Section 3: Activity Selection
# ==========================
def choose_activity():
    activity_list = [
        'Music Jam Session (2 hours, easy, $5 fee)',
        'Science Experiments Lab (3 hours, moderate, $10 fee)',
        'Sports Leadership Training (4 hours, challenging, $12 fee)'
    ]

    print('Choose an activity: ')
    for i, activity in enumerate(activity_list, start=1):
        print(f'{i}. {activity}')

    while True:
        try:
            chosen_activity = int(input("Enter the number of your chosen activity: "))
            if chosen_activity in [1, 2, 3]:
                return chosen_activity
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def sub_chosen_activity_fee(chosen_activity):
    return [5, 10, 12][chosen_activity - 1]

def sub_chosen_activity_duration(chosen_activity):
    return [2, 3, 4][chosen_activity - 1]

def sub_chosen_activity_name(chosen_activity):
    return ['Music Jam Session', 'Science Experiments Lab', 'Sports Leadership Training'][chosen_activity - 1]

def sub_chosen_activity_difficulty(chosen_activity):
    return ['easy', 'moderate', 'challenging'][chosen_activity - 1]

# ==========================
# Section 4: Meal Selection
# ==========================
def choose_meal():
    meal_options = ['Standard', 'Vegetarian', 'Dairy-free', 'Gluten-free', 'No meal']

    print('Choose a meal option: ')
    for i, meal in enumerate(meal_options, start=1):
        print(f'{i}. {meal}')

    while True:
        try:
            chosen_meal = int(input("Enter the number of your chosen meal: "))
            if chosen_meal in [1, 2, 3, 4]:
                return chosen_meal, meal_options[chosen_meal - 1], 7
            elif chosen_meal == 5:
                return chosen_meal, meal_options[chosen_meal - 1], 0
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# ==========================
# Section 5: Summary and Final Decision
# ==========================
def display_summary(name, age, activity_name, activity_difficulty, activity_duration, meal_choice, total_fee):
    print()
    print(f'{name}, Aged {age}, has chosen the {activity_name} activity, which is {activity_difficulty} and lasts for {activity_duration} hours.')
    print(f'You have chosen the {meal_choice} meal option. The total fee is ${total_fee}.')

def confirm_payment(total_fee):
    final_decision = input(f"Do you want to proceed with the payment of ${total_fee} (yes/no): ")
    if final_decision.lower() in ['yes', 'y']:
        print("Payment accepted. Thank you!")
    else:
        print("Payment cancelled.")
    exit()

# ==========================
# Main Program
# ==========================
print()  # Blank line

# Name and age
name = get_name()
age = get_age(name)
validate_age(age)

print()  # Blank line

# Activity section
chosen_activity = choose_activity()
activity_name = sub_chosen_activity_name(chosen_activity)
activity_duration = sub_chosen_activity_duration(chosen_activity)
activity_difficulty = sub_chosen_activity_difficulty(chosen_activity)
activity_fee = sub_chosen_activity_fee(chosen_activity)

print()  # Blank line

# Meal section
chosen_meal, meal_choice, meal_fee = choose_meal()

# Total
total_fee = activity_fee + meal_fee

print()  # Blank line

# Summary and payment
display_summary(name, age, activity_name, activity_difficulty, activity_duration, meal_choice, total_fee)
confirm_payment(total_fee)
