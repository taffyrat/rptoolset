import globalTools
#simple test game
#should create an admin, and two users
#each user should take a turn, attack a creature, and kill it
#creature should inflict poison on one of the players
#one player should level up, other should die
globalTools.createCharacterSheet("characters/Joe")
globalTools.createCharacterSheet("characters/Beck")
print globalTools.readCharacterSheet("characters/Joe")
print globalTools.readCharacterSheet("characters/Beck")

raw_input()