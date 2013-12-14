#!/usr/bin/env python

import sys
import os
import csv
import re


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = re.sub(i, j, text)
    return text


def append_with_break(text, s):
    if not s:
        return text
    if text:
        return text + '\\\\\n' + s
    return s


def main():
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        print("Usage: makeadr.py filename.csv")
        sys.exit(1)

    replacements = {'Herrn': '',
                    'Frau': '',
                    'Professor(in)?': 'Prof.',
                    'Juniorprofessor(in)?': 'Jun.-Prof.'}

    fmt = "\\adrentry{%s}{%s}{%s}{}{}{}{}{}\n"

    with open(sys.argv[1], 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name, title, degree, given_name, institute, chair, building, address, place = row
            title = replace_all(title, replacements)

            first = ' '.join([title, degree, given_name, name]).lstrip()
            third = building
            third = append_with_break(third, address)
            third = append_with_break(third, place)

            institute = append_with_break(institute, chair)
            institute = institute.replace('&', '\\&')

            print(fmt % (first, institute, third.lstrip()))


if __name__ == '__main__':
    main()