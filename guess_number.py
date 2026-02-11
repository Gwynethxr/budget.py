import random
enemy = [{'name':"Goblin","health":5,"attack":1},{'name':"Dragon","health":20,"attack":3}] #data monster
running = True
name = [n['name'] for n in enemy]

#CHOOSE ENEMY AND MONSTER DATA , STAT


for x,y in enumerate(enemy,1):
        print(f"{x}.{y['name']}")
choose_enemy = int(input("Choose your enemy: "))
monster = name[choose_enemy-1]
monster_health = 0
for person in enemy:
        if person['name'] == monster:
            monster_health = person['health']
#PLAYER STAT
player_hp = 10
#START GAME
while running:
    
    


    max_guess = 5
    guess = random.randint(1,max_guess)
    user_attack = int(input("Guess a number from 1 to 5: "))
    if user_attack > max_guess:
         print(f"Cannot more than {guess}")
         continue
    if user_attack == guess:
        monster_health -= 1
        print(f"Your decreasing {monster} HP \nHealth: {monster_health}\n")
        if monster_health == 0 :
            print(f"You are Winning the game ")
            break
    elif user_attack != guess:
        player_hp -= 1
        print(f"You get attacked by {monster}, \nCurrent Health: {player_hp}\n")
        if player_hp == 0:
            print(f"You LOSE!")
            break