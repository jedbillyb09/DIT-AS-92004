# Name input with validation
while True:
    name = input("Enter your name: ")
    if len(name) > 0:
        break
    else:
        print("Invalid input. Please enter a your name.")

# Age input with validation
while True:
    try:
        age = int(input(f"Hi {name}, please enter your age: "))
        if age > 0:
            break
        else:
            print("Invalid input. Age must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")

# Age validation
if age < 12:
    print("Sorry, you must be 12 or older to participate.")
    exit()
if age > 17:
    print("Sorry, you must be 17 or younger to participate.")
    exit()

# Blank line
print()

# Activity list
activity_list = [
    'Music Jam Session (2 hours, easy, $5 fee)',
    'Science Experiments Lab (3 hours, moderate, $10 fee)',
    'Sports Leadership Training (4 hours, challenging, $12 fee)'
]

# Choose list print
print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')


# Activity input with validation
while True:
    try:
        chosen_activity = int(input("Enter the number of your chosen activity: "))
        if chosen_activity in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Chosen activity fee calculation
if chosen_activity == 1:
    activity_fee = 5
elif chosen_activity == 2:
    activity_fee = 10
elif chosen_activity == 3:
    activity_fee = 12

# Blank line
print()

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
        if chosen_meal in [1, 2, 3, 4, 5]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Chosen meal fee calculation
if chosen_meal == 1 or chosen_meal == 2 or chosen_meal == 3 or chosen_meal == 4: 
    meal_fee = 7
else:
    meal_fee = 0

# Total fee calculation
total_fee = activity_fee + meal_fee

# Blank line
print()

# Output
print(f'{name}, aged {age}, has chosen "{activity_list[chosen_activity - 1]}", meal option: "{meal_options[chosen_meal - 1]}". The total fee is ${total_fee}.')