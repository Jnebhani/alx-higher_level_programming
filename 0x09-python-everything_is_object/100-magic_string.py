#!/usr/bin/python3
def magic_string:
    setattr(magic_string, "d", getattr(magic_string, "d", -1) + 1)
     return "Bestschool" + (", Bestschool" * magic_string.d)
