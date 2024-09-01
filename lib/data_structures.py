

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
    spicy_Foods_string=[food["name"]for food in spicy_foods]
    return spicy_Foods_string

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    length = len(spicy_foods)
    for i in range(length):
        emoji_No = "🌶" * spicy_foods[i]["heat_level"]
        print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {emoji_No}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None 


def print_spiciest_foods(spicy_foods):
    length = len(spicy_foods)
    for i in range(length):
        emoji_No = "🌶" * spicy_foods[i]["heat_level"]
        if spicy_foods[i]["heat_level"] > 5:
            print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {emoji_No}')

def get_average_heat_level(spicy_foods):
    heat_levels =[food["heat_level"] for food in spicy_foods]
    print(heat_levels)
    sum = 0
    for i in range(0, len(heat_levels)):
        sum = sum + heat_levels[i]
        print(sum)
        average = sum / len(heat_levels)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
create_spicy_food(spicy_foods,{
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })
print(spicy_foods)