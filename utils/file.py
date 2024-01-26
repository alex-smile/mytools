def read_file(path):
    with open(path, "rb") as fp:
        return fp.read()


def write_to_file(content, path, mode="w"):
    with open(path, mode) as fp:
        fp.write(content)