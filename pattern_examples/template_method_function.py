def get_text():
    return 'plain-text'


def get_csv():
    return 'csv'


def convert_to_text(value):
    print("[CONVERT]")

    return f"{value} as text"


def template_function(getter, converter=None):
    data = getter()

    if converter:
        data = converter(data)

    return data


if __name__ == "__main__":
    result = template_function(get_text)
    print(result)

    result = template_function(get_csv, convert_to_text)
    print(result)
