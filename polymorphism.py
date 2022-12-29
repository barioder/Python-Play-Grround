# Polimorphism with class methods 

class Arsenal():
    def position (self):
        print('Arsenal is in 1st place')
    
    def bestplayer(self):
        print('The best player is Saka')

class ManCity():
    def position (self):
        print('ManCity is in second position')
    
    def bestplayer(self):
        print('The best player is Haaland')


arsenal_update = Arsenal()
mancity_update = ManCity()
print(arsenal_update, mancity_update)

for team in (arsenal_update, mancity_update):
    team.position()
    team.bestplayer()
    print('\n')