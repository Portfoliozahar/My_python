


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()