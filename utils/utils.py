def remove_trailing_comma(inp):
    if inp.endswith(","):
        return inp[:-1]
    return inp