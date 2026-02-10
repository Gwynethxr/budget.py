import random 
import json
def load_menu ():
    try:
        with open('menu.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: menu.json not found")
        return []
def get_recommendation():
    menu = load_menu()
    if not menu: return

    print("\n---Input Decision Dinner---")
    user = int(input("Search by (1).Taste or (2).country : "))
    heading = "-------------------------------------------"
    if user == 1:
        
        taste = set()
        for food in menu:
            for t in food['taste']:
                taste.add(t)
        taste_list = list(taste)
        m_display = ""
        for i,value in enumerate(taste_list,1):
            m_display += f"{i}.{value}\n"
        user_choice = int(input(f'{heading}\n{m_display}What are you prefer for taste: '))
        #####################################################################################
        for index,values in enumerate(taste_list,1):
            if user_choice == index:
                user_choice = values
        matches = [m for m in menu if user_choice in m['taste'] ]
    
        if matches :
            result = random.choice(matches)
            return print(f"\n✅ Match Found: {result['name']} from {result['country']}")
        else:
            return print(f"No matches for that taste. Try being less picky! 😉")
    else:
        result = random.choice(menu)
        print(f"\nGet 🎲 Random Pick: {result['name']} from {result['country']}")
print(get_recommendation())