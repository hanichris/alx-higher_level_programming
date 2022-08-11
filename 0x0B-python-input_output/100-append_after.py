#!/usr/bin/python3
"""Module defines the append_after() function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file.

    The insertion happens after each line containing a specific string.

    Args:
        filename (str): Text file to be modified.
        search_string (str): Specific string to look for in the text file.
        new_string (str): New line of text to insert into the text file.
    """
    with open(filename, mode="r+", encoding='utf-8') as fp:
        data = list(fp)
        fp.seek(0)
        for line in data:
            if search_string in line:
                fp.write(line)
                fp.write(new_string)
            else:
                fp.write(line)
        fp.truncate()
