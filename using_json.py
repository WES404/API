import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl", 
        "number" : "+1 734 383 4456"
    } ,
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name: ", info["name"])
print("number: ", info["phone"]["number"])