#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
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

    def do_show(self, args):


    def do_EOF(self):
        """ in proccess """
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True 

    def emptyline(self):
        pass

if __name__ == '__main__':
    commands = HBNBCommand()
    commands.cmdloop()
