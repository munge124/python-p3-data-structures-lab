spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = []
    i = 0
    while(i < len(spicy_foods)):
        name_list.append(spicy_foods[i].get('name'))
        i += 1
    return name_list   
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    i = 0
    while(i < len(spicy_foods)):
        if(spicy_foods[i].get('heat_level') > 5):
            spiciest_foods.append(spicy_foods[i])
        i += 1
    return spiciest_foods    
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print( f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    i = 0
    while(i < len(spicy_foods)):
        if(spicy_foods[i].get('cuisine') == cuisine):
            return spicy_foods[i]
        i += 1
    return None    
    pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = []
    i = 0
    while(i < len(spicy_foods)):
        if(spicy_foods[i].get('heat_level') > 5):
            spiciest_foods.append(spicy_foods[i])
        i += 1
    for food in spiciest_foods:
        print( f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {'🌶' * food.get('heat_level')}")
    pass    

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total += food.get('heat_level')
    return total/len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
print(create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
))