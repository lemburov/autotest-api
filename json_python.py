# import json
#
#
# json_data = '{"name": "Alex", "age": 40, "is_student": false}'
# parsed_data = json.loads(json_data)
#
# print(parsed_data)
#
#
# data = {"name": "мария", "age": 20, "is_student": True}
#
# json_string = json.dumps(data, indent=1)
#
# print(json_string)
#
# with open("json_example.json", "r", encoding="utf-8") as file:
#     read_data = json.load(file)
#     print(read_data, type(data))
#
# with open("json_data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False