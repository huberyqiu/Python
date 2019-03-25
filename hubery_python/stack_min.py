"""
This script is enhanced stack version, it has below functions:
p: Push data into Stack
o: Pop data from Stack
v: View all data in Stack
min: Get the min value from Stack
q: Quit
"""

import decimal

stack=[]
stackmin=[]

valid_choice=('p','o','v','min')

def pushit():
    num_input_raw=input('Please input a valid number: ').strip()
    try:
        num_input=int(num_input_raw)
        stack_depth = len(stack)
        stack.append(num_input)
        print('Push %s success' % num_input)
        if stack_depth == 0:
            cur_min = num_input
        else:
            min_from_stack = stackmin[stack_depth - 1]
            if min_from_stack > num_input:
                cur_min = num_input
            else:
                cur_min = min_from_stack
        print("cur_min value is: %s" % cur_min)

        stackmin.append(cur_min)

    except ValueError:
        print('[%s] Not a valid number, Ignored!' % num_input_raw)

def popit():
    if len(stack) == 0:
        print('Unable to Pop from empty stack!')
    else:
        print(stack.pop())
        stackmin.pop()

def getmin():
    stack_depth = len(stack)
    if stack_depth == 0 :
        print('This is empty stack, no min value returned!')
    else:
        print(stackmin[stack_depth-1])

def viewstack():
    print(stack)
    print(stackmin)


CMDs = {'p': pushit, 'o': popit, 'v': viewstack, 'min':getmin }


def showmenu():
    while True:
        prt="""\n Please enter the choice below:
           p: Push data into Stack       o: Pop data from Stack
           v: View all data in Stack     min: Get the min value from Stack
           Enter q to quit the job
           Your Choice: 
           """

        choice=input(prt).strip().lower()

        if choice == 'q':
            print('Thanks for your time to use this, Bye-Bye!')
            break
        if choice in valid_choice:
            print('You current choice is: [%s]' % choice)
            CMDs[choice]()
        else:
            print('Invalid Choice, please input an valid choice. Enter q to quit the program')


if __name__ == '__main__':
    showmenu()
