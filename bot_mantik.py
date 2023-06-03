# bot_logic in original

import random

def kazanan_takim(yil):
    
    if yil == '2022':
        return 'https://upload.wikimedia.org/wikipedia/tr/a/a4/Afa_logo.png'
    
    elif yil == '2018':
        return 'https://w7.pngwing.com/pngs/89/927/png-transparent-2018-world-cup-france-national-football-team-1998-fifa-world-cup-france-emblem-label-team.png'
    
    elif yil == '2014':
        return 'https://upload.wikimedia.org/wikipedia/tr/archive/a/a9/20221128082239%21DFBEagle.png'
    elif yil == '2010':
        return 'https://upload.wikimedia.org/wikipedia/tr/c/cd/RFEF.PNG'
    
    elif yil == '2006':
        return 'https://w7.pngwing.com/pngs/419/868/png-transparent-italy-national-football-team-italy-national-under-21-football-team-italy-women-s-national-football-team-world-cup-italy.png'
    elif yil == '2002':
        return 'https://w7.pngwing.com/pngs/1018/611/png-transparent-2018-world-cup-brazil-national-football-team-2014-fifa-world-cup-brasil-copa-sport-logo-jersey-thumbnail.png'
    
    elif yil == '1998':
        return 'https://w7.pngwing.com/pngs/89/927/png-transparent-2018-world-cup-france-national-football-team-1998-fifa-world-cup-france-emblem-label-team.png'
def mvp_oyuncu(yil):
    
    if yil == '2022':
        return 'Lionel Messi'
    elif yil == '2018':
        return 'Luka Modric'
    
    elif yil == '2014':
        return 'Lionel Messi'
    elif yil == '2010':
        return 'Diego Forlan '
    
    elif yil == '2006':
        return 'Zinedine Zidane'
    elif yil == '2002':
        return 'Oliver Kahn'
    
    elif yil == '1998':
        return 'Ronaldo Nazario'