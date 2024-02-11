#!/usr/bin/python3
"""
Module containing the entry point of the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter at EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

