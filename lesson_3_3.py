import random

HELP = """
help - output help for the program
add - adding task to list (task name request from user)
show - print all tasks
random - add random task to today list
"""

RANDOM_TASKS = ['Watch TV', 'Go outside', 'Get rest', 'Car wash']

tasks = {

}

def add_todo(date_task, task):
    if date_task in tasks:
        tasks[date_task].append(task)
        print(f'Task {task} has been added in the list.')
    else:
        tasks[date_task] = [task]
        print(f'The {task} task was added on the date {date_task}.')


while True:
    command = input('Input command: ').lower()
    if command == str('help'):
        print(HELP)
    elif command == str('show'):
        date_task = input('Input your date task: ')
        if date_task in tasks:
            for task in tasks[date_task]:
                print(f'- {task}')
        else:
            print('No date in list')
    elif command == str('add'):
        date_task = input('Input date task: ')
        task = input('Input task name: ')
        add_todo(date_task, task)
    elif command == str('random'):
        task = random.choice(RANDOM_TASKS)
        add_todo('today', task)
    else:
        if command == 'exit':
            print('Thanks for using! Good bye!')
            break
        else:
            print('Unknown command!\nThe following commands are available:\n-help\n'
                  '-show\n-add')
        #   print('Good bye')
