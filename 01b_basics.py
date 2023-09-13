# name = input('what is your name?')
name = 'Randy'
print('Hello', name, '!', sep = '+', end = 'END\n')
print(f'Hello, {name}!')

print(f'2 + 3 = {2+3}')

#ask the user how old they are, and tell them how old they'll be next year
# age_str = input('How old are you? ')
age_str = '48'
age = int(age_str)
# print(f'Next year you will be {age + 1}')

#types

am_i_hungry = True    # <= (snake case) amIHungry (camel case)
aih_type = type(am_i_hungry)
print(f'{aih_type = }')

#Exercise 01b.2
import turtle

window = turtle.Screen()
t = t.Turtle()

t.pendown()

t.forward(10)

window.mainloop()