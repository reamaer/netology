HELP = """
help - output help for the program
add - adding task to list (task name request from user)
show - print all tasks
"""

today = []
tomorrow = []
other = []

run = True

while run:
    command = input('Input command: ').lower()
    if command == str('help'):
        print(HELP)
    elif command == str('show'):
        print('today: ', today, 'tomorrow: ', tomorrow, 'others: ', other)
    elif command == str('add'):
        date_task = input('Input date task: ')
        if date_task == 'today':
            task = input('Input task name: ')
            today.append(task)
            print('Task added in today list')
        elif date_task == 'tomorrow':
            task = input('Input task name: ')
            tomorrow.append(task)
            print('Task added in tomorrow list')
        else:
            task = input('Input task name: ')
            other.append(task)
            print('Task added in other tasks')
    else:
        if command == 'exit':
            print('Thanks for using! Good bye!')
            run = False
        else:
            print('Unknown command')
        #     print('Good bye')
        #     break
