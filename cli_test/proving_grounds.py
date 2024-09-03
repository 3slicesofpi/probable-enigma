# import cmd
# class promptClass(cmd.Cmd):
#     def do_greet(self, arg):
#         """Say Hello!"""
#         if arg:
#             print('hello', arg)
#         else:
#             print('no arg given')
#
#     def do_manyarg(self, line):
#         """Give two arguments"""
#         a, b = [str(s) for s in line.split(',')]
#         if a and b:
#             print(a,b)
#         else:
#             print('two args needed')
#     def do_quit(self, arg):
#         """Quits the Program"""
#         raise SystemExit
#
# prompt = promptClass()
# prompt.prompt = '>'
# prompt.cmdloop('...')

from dataclasses import dataclass, field, make_dataclass
from typing import Any, List, Tuple


class DataClassFactory:
    @staticmethod
    def create_data_class(class_name: str, fields: List[Tuple[str, type, Any]]):
        """
        Create a new data class with the given class name and fields.

        :param class_name: Name of the new data class.
        :param fields: List of tuples, where each tuple contains the field name, field type, and default value.
        :return: A new data class.
        """
        return make_dataclass(class_name, fields)


# Example usage:

# Define fields for a new data class called 'Person'
person_fields = [
    ('name', str, 'Unknown'),
    ('age', int, 0),
    ('is_student', bool, False)
]

# Create the data class using the factory
Person = DataClassFactory.create_data_class('Person', person_fields)

# Create an instance of the newly created data class
person_instance = Person(name='Alice', age=30)

# Output the instance details
print(person_instance)
print(f"Name: {person_instance.name}, Age: {person_instance.age}, Is Student: {person_instance.is_student}")
