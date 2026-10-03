import json 

student = {
    "name": "Rahim",
    "age": 20,
    "department":"CSE"
}

Json_data_of_the_student = json.dumps(student) 

print(Json_data_of_the_student) 