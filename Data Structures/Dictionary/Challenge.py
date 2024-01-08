# Remove the record with None values and store it into new dictionary without deleting any value from the first dictionary
user_prefrences = {
    'timezone': "GMT",
    "language": "English",
    "notifications": None,
    "currency" : "USD",
    "theme":None
}
new_user_preferences = {}
def remove_none(values):
    for key, values in user_prefrences.items():
        if values == None:
            pass
        else:
            new_user_preferences[key] = values

Remove_none = remove_none(user_prefrences)

print(new_user_preferences)
        
