import random
import string


def count_json_obj(json_data, str_value, object_str="model"):
    """
    Count occurrences of a specific string value within a list of dictionaries.

    Parameters:
        json_data (list): A list of dictionaries.
        str_value (str): The string value to search for.
        object_str (str, optional): The key within the dictionaries to compare against. Defaults to "model".

    Returns:
        int: Number of occurrences of the specified string value.
    """
    return sum(1 for item in json_data if item.get(object_str) == str_value)


def generate_str(str_length: int = 8):
    """
    Generate a random string of specified length.

    Parameters:
        str_length (int): Length of the generated random string.

    Returns:
        str: Random string of specified length.
    """
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(str_length))
