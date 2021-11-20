"""Main entry point for requested exercises

Please write a class in the language of your choice that contains the following two public methods:

aboveBelow
accepts two arguments
An unsorted collection of integers (the list)
an integer (the comparison value)
returns a hash/object/map/etc. with the keys "above" and "below" with the corresponding count of integers from the list
 that are above or below the comparison value
Example usage:

input: [1, 5, 2, 1, 10], 6

output: { "above": 1, "below": 4 }

stringRotation
accepts two arguments
a string (the original string)
a positive integer (the rotation amount)
returns a new string, rotating the characters in the original string to the right by the rotation amount and have the
 overflow appear at the beginning
Example usage:

input: "MyString", 2

output: "ngMyStri"

"""

import pprint


class AboveBelow:
    @staticmethod
    def above_below(integer_list: list, comp_value: int) -> dict:
        """Given a list and an integer, returns a dictionary with the keys "above" and "below" with the count of
         integers from the list that are above or below the comparison value.
        Additionally, added two keys for equal and unhandled values, such as a incompatible types.
        """
        result = {
            'above': 0,
            'below': 0,
            'equal': 0,
            'unhandled': 0
        }
        for value in integer_list:
            try:
                value = int(value)
            except (TypeError, ValueError):
                result['unhandled'] += 1
                continue
            try:
                if value > comp_value:
                    result['above'] += 1
                elif value < comp_value:
                    result['below'] += 1
                elif value == comp_value:
                    result['equal'] += 1
            except TypeError:
                result['unhandled'] += 1
        return result


class StringRotation:
    @staticmethod
    def string_rotation(string: str, rotation_amount: int) -> str:
        """Given a string and a positive integer, return a new string that's been wrapped around the given index.
        If the rotation amount is greater than the string length, I think it should still wrap around by the remainder.
        """
        if rotation_amount < 0 or not isinstance(rotation_amount, int):
            raise ValueError("rotation_amount must be a positive integer")
        string_length = len(string)
        index = rotation_amount % string_length  # handles rotation amounts greater than string length
        new_string = string[-index:] + string[:-index]
        return new_string


if __name__ == '__main__':
    # Above/Below class + examples
    above_below = AboveBelow()
    # Given example
    pprint.pp(above_below.above_below([1, 5, 2, 1, 10], 6))
    # Contrived example
    pprint.pp(above_below.above_below([9, 2, 5, 123, 3, 5, 7, 1, 5, 89, 23, 4, 56, 10], 10))
    # Example with inputs other than integers
    pprint.pp(above_below.above_below(['9', 2, 6, 4, 9.1, 8.4, 3.2, 3.9, 'cat'], 3))

    # StringRotation examples
    string_rotation = StringRotation()
    # Given example
    print(string_rotation.string_rotation('MyString', 2))
    # Example with a value that wraps around the length of the string
    print(string_rotation.string_rotation('MyString', 15))
    # Example with a different string
    print(string_rotation.string_rotation('Once upon a time', 14))
