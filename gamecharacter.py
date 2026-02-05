class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self,new_health):
        self._health = new_health
        if new_health < 0 :
            self._health = 0
        if new_health > 100: # equal to if self._health > 100
            self._health = 100
        
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self,new_mana):
        pass

hero = GameCharacter("Kratos")
hero.health -= 30 #hero.health = hero.health(100) - 130(new_health) = -30
hero.mana -= 10
print(hero.health)