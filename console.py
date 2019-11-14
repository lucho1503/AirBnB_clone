#!/usr/bin/python3
"""
console - this console contains the entry point
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand """
    prompt = "(hbnb) "

    def do_create(self, args):
        if args is "":
            """ ** class name missing ** """
        elif args is not "BaseModels":
            """ ** class doesn't exist ** """
        else:
            create = BaseModel()
            create.save()
            print(create.id)

    def help_create(self, args):
        pass

    def do_EOF(self, line):
        """ Quit command to exit the program\n """
        return True
        do_EOF = do_quit

    def help_quit(self, args):
        print("quit command exit")

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    commands = HBNBCommand()
    commands.cmdloop()
