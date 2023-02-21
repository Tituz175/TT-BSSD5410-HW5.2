def process_file(fname, enc):
    with open(fname, "r", encoding=enc) as file:
        dat = file.read()
    return dat


# end def process_file(fname, enc):

