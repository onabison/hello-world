def string_to_list(value, delimiter=" "):
    value = value.replace(f"{delimiter}{delimiter}", delimiter)
    result = value.split(delimiter)
    return result