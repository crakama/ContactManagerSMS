"""HTML Cleaner.

Usage:
  add -n <name> -p <phonenumber>
  cleanup [-p | --pretty] <element> <replacement> <filename>
  cleanup (-h | --help)
  cleanup (-V | --version)
  add     (-n| --name)
Options:
  -h --help     Show this screen.
  -p --pretty   Prettify the output.
  -V --version  Show version.
  -n --name    prompt user for name

"""

from docopt import docopt, DocoptExit
import sys
import cmd

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)

class  (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_example(self, arg):
        """Usage: name <host> <port> [--timeout=<seconds>]"""

        print(arg)
opt = docopt(__doc__)

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
