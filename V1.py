#Name and Age inputs
name = input("Enter your name: ")
age = input("Enter your age: ")

#Choose an activity list input
activity_list = ['Music Jam Session (2 hours, easy, $5 fee)','Science Experiments Lab (3 hours, moderate, $10 fee)','Sports Leadership Training (4 hours, challenging, $12 fee)']

print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')
chosen_activity = input("Enter the number of your chosen activity: ")