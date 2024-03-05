def count_json_obj(obj, object_str):
    return sum(1 for item in data if item.get("model") == "task_management.board")
