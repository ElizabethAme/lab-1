# TODO решите задачу
import json


def task() -> float:
    file_input = "input.json"
    with open(file_input, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    total_sum = sum([item["score"] * item["weight"] for item in json_data])
    return round(total_sum, 3)

print(task())
