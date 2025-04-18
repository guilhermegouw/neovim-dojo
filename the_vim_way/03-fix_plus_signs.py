"""
Substitute every "+" with " + "
"""


message = "This"+" is"+" a"+" nice"+" message"
another_message = "This"+" is"+" another"+" nice"+" message"
not_a_message = "This"+" is"+" not"+" a"+" message"
not_another_message = "This"+" is"+" not"+" another"+" message"


def some_messages(
        message,
        another_message,
        not_a_message,
        not_another_message
    ):
    print(message)
    print(another_message)
    print(not_a_message)
    print(not_another_message)
