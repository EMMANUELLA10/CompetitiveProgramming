import textwrap

def wrap(string, max_width):
    if len(string) > max_width:
        x = ""
        for i in range(max_width):
            x += string[i]
        string = string[max_width:]
        print(x)
        return wrap(string, max_width)
    else:
        return string