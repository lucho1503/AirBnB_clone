#!/usr/bin/python3
"""
console - this console contains the entry point
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand """
    prompt = "(hbnb) "
    clss = {'BaseModel'}

    def do_create(self, create):
        """ create instance de basemodel
            and save file .json """
        if create == "":
            print('** class name missing **')
        elif create not in self.clss:
            print("** class doesn't exist **")
        else:
            create = eval(create)()
            create.save()
            print(create.id)

    def do_show(self, show):
        """ print string representation
            of an instance based """
        arg = show.split()
        if show == "":
            print("** class name missing **")
        elif arg[0] not in self.clss:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            inst = models.storage.all().get(key)
            if not inst:
                print("** no instance found **")
            else:
                print(inst)

    def do_destroy(self, destroy):
        """ deletes an instance based on the class
            name and id (save the change in the JSON file
        """
        arg = destroy.split()
        if destroy == "":
            print("** class name missing **")
        elif arg[0] not in self.clss:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            inst = models.storage.all().get(key)
            if not inst:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, alls):
        """ """
        data = models.storage.all()
        if alls is "":
            for keys, objs in data.items():
                print(objs)
        else:
            arg = alls.split()
            if arg[0] not in self.clss:
                print("** class doesn't exist **")
            else:
                for keys, objs in data.items():
                    obj = objs.to_dict()
                    if obj['__class__'] == arg[0]:
                        print(obj)

    def do_EOF(self, line):
        """ Quit command to exit the program\n """
        return True
        do_EOF = do_quit

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    commands = HBNBCommand()
    commands.cmdloop()
