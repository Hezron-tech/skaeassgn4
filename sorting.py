family = [{ "name" : "Hezzy", "age" : 24},
{ "name" : "Ashie", "age" : 20 },
{ "name" : "Sha" , "age" : 19 }]

print("sorted list: ")

def sort_family(family):
    return sorted(family,key=lambda x: x['name'])
    
print(sort_family(family))
