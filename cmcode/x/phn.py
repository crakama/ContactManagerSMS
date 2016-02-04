import sys

print "The arguments given to the interpreter are:"
print sys.argv



def create_phonebook(phonebook_name):
    # create a new phonebook
    pass


def add_entry(name, number, phonebook_name):
    # add a new name and number to the given phonebook
    pass


if __name__ == '__main__':
    pass


    args = sys.argv[:]      # make a copy
    script = args.pop(0)    # name of script is first arg
    if not args:
        print "Not enough arguments"
        quit()
    command = args.pop(0)   # the next arg will be the main command

    if command == 'create':
        phonebook_name = args.pop(0)
        create_phonebook(phonebook_name)

    elif command == 'add':
        name = args.pop(0)
        number = args.pop(0)
        phonebook_name = args.pop(0)
        add_entry(name, number, phonebook_name)