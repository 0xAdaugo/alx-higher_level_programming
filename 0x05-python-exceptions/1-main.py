#!/usr/bin/python3
safe_print_integer = _import_('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_ben_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
