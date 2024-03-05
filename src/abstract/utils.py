def count_json_obj(json_data, str_value, object_str="model"):
    return sum(1 for item in json_data if item.get(object_str) == str_value)
