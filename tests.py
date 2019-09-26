import string


def alphabet_position(s):
    r = ""
    for i in s:
        if i.isalpha():
            print(string.ascii_lowercase.index(i))


print(alphabet_position("The sunset sets at twelve o' clock."))
