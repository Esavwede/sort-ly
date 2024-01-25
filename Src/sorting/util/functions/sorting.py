

def extract_extension(input_string):

    parts = input_string.split(".")

    if len(parts) > 1:
        return parts[-1]
    else:
        return input_string

