#!/usr/bin/env python3
""" Divides a long list of text into columns """
import pyperclip


def main():
    raw_string = pyperclip.paste()

    # Splits the text by newlines.
    whole_data = raw_string.strip().splitlines()
    output_string = ""
    
    for i, line in enumerate(whole_data):
        # Alternates between lines
        if i % 2 == 0:
            output_string += line
        else:
            # Computes the needed spaces for padding
            spaces = " " * (20 - len(whole_data[i-1]))
            output_string += "{}{}\n".format(spaces, line)

    # Success
    pyperclip.copy(output_string)
    print("Converted!")


if __name__ == '__main__':
    main()
