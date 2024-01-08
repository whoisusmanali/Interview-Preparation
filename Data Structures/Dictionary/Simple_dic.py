#Dictionary is the combination of Key and Values
Pakistan_states = {
    'Punjab': 'Lahore',
    'Sindh' : 'Karachi',
    'KPK' : 'Peshawar',
    'Balochistan' : 'Quetta'
}

print(Pakistan_states['Balochistan'])

#Look for all the keys
for key in Pakistan_states.keys():
    print(key)

#Look for all the values
for values in Pakistan_states.values():
    print(values)

#Look for both of these things
for key, values in Pakistan_states.items():
    print(key, "States has", values, "Capital")


#Mutate the values in dic let's start with updating the value
Pakistan_states['Punjab'] = 'Faisalabad'


#delete an item
del Pakistan_states['Sindh']
Pakistan_states.pop('KPK')
print(Pakistan_states.values())
