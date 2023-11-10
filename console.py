#!/usr/bin/python3
"""
    This module contains the entry point of the command interpreter
    Author: Ahmed Eldeeb (ahmedsabrieldeeb@gmail.com)
"""


import cmd
import io
import sys

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """The main cmd of the program for testing and adminstrative purposes"""

    all_instances = storage.all()

    prompt = "(hbnb) "

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity,
        "State": State,
        "City": City
    }


    def default(self, line):
        """
        Handle dynammic commands that don't
        abide by do_command format

        Args:
            line (str): the line to be parsed
        """
        if (line[-6:] == '.all()'):
            self.handle_dot_all(line)
        elif (line[-8:] == '.count()'):
            self.handle_dot_count(line)
        else:
            pass

    def handle_dot_all(self, line):
        """Printing all instances of a specific class"""
        args = line.split('.')
        self.do_all(args[0])
    
    def handle_dot_count(self, line):
        """Count number of instances of a specific class"""
        args = line.split('.')

        # capture the printed value to count them
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

        # call the needed method to capture its repsonse
        self.do_all(args[0])

        # get the value printed
        list_of_instances = sys.stdout.getvalue()

        # restore the stdout to its original state
        sys.stdout = stdout_backup

        # count number of instances process
        if(list_of_instances == "[]\n"):
            print('0')
        else:
            print(len(list_of_instances.split('", "')))

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Usage:
            create <class name>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        obj = HBNBCommand.class_dict[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage:
            show <class name> <instance id>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            desired_obj = (storage.all())[id_key]
        except KeyError:
            print("** no instance found **")
            return

        print(desired_obj)

    def do_destroy(self, line):
        """
        Deletes an instance from the JSON file
        based on the class name and id

        Usage:
            destroy <class name> <instance id>
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            removing_obj = (storage.all())[id_key]
            storage.destroy(removing_obj)
            del removing_obj
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name

        Usage:
            all
            all <class name>
        """

        args = line.split()  # splitting by whitespace by default
        if args:
            if args[0] in HBNBCommand.class_dict.keys():
                class_name = args[0]
                objs_list = [str(HBNBCommand.all_instances[key]) \
                        for key in HBNBCommand.all_instances \
                    if HBNBCommand.all_instances[key].__class__.__name__ == class_name]
                print(objs_list)
                return 
            else:
                print("** class doesn't exist **")
                return

        all_instances = storage.all()
        objs_list = [str(all_instances[key]) for key in all_instances]
        print(objs_list)

    def do_update(self, line):
        """
        Updates an instance in the JSON file
        based on the class name and id, updating
        only one key-value pair, so any more key-value
        pairs coming after first one will be ignored

        Usage:
            update <class name> <instance id> <attribute name> <value>

        Pre-Conditions and Assumptions:
            id, created_at, upated_at cannot't be passed as arguments
            attribute value must be formatted as "<value>"
            attribute name will always be existed (valid) for the instance
        """
        args = line.split()  # splitting by whitespace by default
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        try:
            id_key = args[0] + '.' + args[1]
            desired_obj = (storage.all())[id_key]
        except KeyError:
            print("** no instance found **")
            return

        setattr(desired_obj, args[2], (args[3])[1:-1])
        desired_obj.save()

    def do_EOF(self, line):
        """
        Exiting the program by pressing Ctrl+D
        """
        return True

    def do_quit(self, line):
        """
        Exiting the program by typing 'quit'
        """
        return True

    def emptyline(self):
        """Do nothing when pressing Enter"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
