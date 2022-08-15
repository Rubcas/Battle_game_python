"""Goal: Fantasy Battle Game
Player chooses between Wizard, Elf, Human
Chosen character battles Dragon
Program (your code!) calculates winner
"""

#Declaration of players as strings
wizard = "Wizard"
elf= "Elf"
human="Human"

#Declaration of hit points of each character
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

#Declaration of damage points of each character
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

#Prints out the name of each character
print("1)   ", wizard)
print("2)   ", elf)
print("3)   ", human)

#Prompts user to choose a character. Then assigns that value to "character". Then, declares new variables and assigns hitpoints and damage
while True:
    character = input("Choose your character:")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("unknow character")
print("You have chosen the character: ", character)
print("Health:", my_hp)
print("Damage:", my_damage)
print()


while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        print()
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon's strikes back at", character )
    print("The",character,"hitpoints are now:",my_hp)
    print()
    if my_hp <= 0:
        print("The Dragon has lost the battle")
        break