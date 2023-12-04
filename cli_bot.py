def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def change_contact(args,contacts):
    name,phone = args
    contacts.update({name:phone})
    return "Contact updated"

def input_error(fn):
    def inner(*args, **kwargs):
        try:
            return fn(args, kwargs)
        except ValueError:
            "Give me name and phone please"
        except TypeError:
            "Enter correct type"
    return inner

@input_error
def add_contact(args,contacts):
    name,phone = args
    contacts[name] =phone
    return "Contact added"




def main():
    print('Welcome to the assistant bot!')
    contacts = {}
    while True:
        user_input =input("Enter the command >>>>>")
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'all':
            print(contacts)
        elif command.isdecimal():
            print(contacts[args[0]])
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()