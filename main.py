from turtle import Turtle, Screen
import random

race_is_on = False

my_screen = Screen()

my_screen.bgpic("Ground.gif")

Poke_image = ["Arcanine.gif", "Charizard.gif", "Dodrio.gif", "Pidgeot.gif", "Rapidash.gif", "Tauros.gif"]
for image in Poke_image:
    my_screen.addshape(image)

my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make Your Bet", prompt="Which Pokémon will win the Race? Enter a name (Arcanine, Charizard, Dodrio, Pidgeot, Rapidash, Tauros): ")

Pokemons = ["Arcanine", "Charizard", "Dodrio", "Pidgeot", "Rapidash", "Tauros"]
POKE = []

i = 0
y = -100
for pokemon_name in Pokemons:
    pokemon = Turtle()
    pokemon.shape(Poke_image[i])
    pokemon.penup()
    pokemon.goto(x=-230, y=y)
    POKE.append(pokemon)
    i += 1
    y += 40

finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=230, y=-150)
finish_line.pendown()
finish_line.setheading(90)
finish_line.color("white")
finish_line.width(5)
finish_line.forward(300)
finish_line.hideturtle()

if user_bet:
    race_is_on = True

while race_is_on:
    for pokemon, name in zip(POKE, Pokemons):
        if pokemon.xcor() >= 230:
            race_is_on = False
            if name == user_bet:
                print(f"You WON the BET! {name} won the race!")
            else:
                print(f"You LOST the BET! {name} won the race!")
            break

        pokemon.forward(random.randint(1, 10))

my_screen.exitonclick()
