#!/usr/bin/python3
"""The AirBnB console"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    storage = FileStorage()
    storage.reload()

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program (Ctrl-D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_count(self, arg):
        """Prints the number of instances of a class."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            count = len(eval(class_name).all())
            print(count)
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** invalid syntax **")

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** invalid syntax **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on its ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances = self.storage.all().values()
        instance = next((inst for inst in instances if inst.__class__.__name__ == class_name and inst.id == instance_id), None)
    
        if instance:
            print(instance)
        else:
            print("** no instance found **")


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances = self.storage.all().values()
        instance = next((inst for inst in instances if inst.__class__.__name__ == class_name and inst.id == instance_id), None)

        if not instance:
            print("** no instance found **")
            return

        del self.storage.all()[f"{class_name}.{instance_id}"]
        self.storage.save()


    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        instances = self.storage.all().values()
        instances_filtered = [str(instance) for instance in instances if instance.__class__.__name__ == class_name]

        print(instances_filtered)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances = self.storage.all().values()
        instance = next((inst for inst in instances if inst.__class__.__name__ == class_name and inst.id == instance_id), None)

        if not instance:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        if len(args) < 5:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = ' '.join(args[3:]).strip('"')

        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return

        if hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            try:
                setattr(instance, attribute_name, attribute_type(attribute_value))
                instance.save()
            except (ValueError, TypeError):
                print("** invalid value type **")
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

