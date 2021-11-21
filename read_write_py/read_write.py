def write_to_file():
    """Append User input based on User's confirmation."""
    while True:
        writein = input('Would you like to add a line?: (Y or N) ')

        if writein == 'Y':
            f = open('./todos.txt', 'a')
            user_line = input('Ok what\'s the line?: ')
            print(user_line, file=f)
            print('Your line is recorded. Thank you.')
            f.close()
            read_from_file()
            break
        elif writein == 'N':
            read_from_file()
            break
        else:
            validate_input(writein)


def read_from_file():
    """Display file contents based on User confirmation."""
    while True:
        view_line = input('Would you like to view the file contents?: ')
        if view_line == 'Y':
            f = open('./todos.txt')
            for lines in f:
                print(lines)
            f.close()
            break
        elif view_line == 'N':
            print('Ok, Bye!')
            break
        else:
            validate_input(view_line)


def validate_input(user_input):
    """Validate User's input against acceptable Input values."""
    if user_input not in ['Y', 'N']:
        print('Try again')


write_to_file()
