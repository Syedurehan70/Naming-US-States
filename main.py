from turtle import Turtle, Screen
from guess import Guess

n = 0
l = 50
screen = Screen()
tim = Turtle()
file = Guess()
guessed_states = []

screen.title("U.S States Game")
# saving image doc by it's path
image = "blank_states_img.gif"
# adding a new turtle shape which doesn't existed before
screen.addshape(image)
# turning turtle into that shape
tim.shape(image)

game_on = True
while game_on:
    # this will add a prompt on the screen, capitalize, make first word capital and rest small, cuz that's how it is
    # in file
    answer_state = screen.textinput(title=f"{n}/{l} States Correct", prompt="Guess the name of state? ").capitalize()
    if answer_state == "Exit":
        file.exit(guessed_states=guessed_states)
        break
    # if the answer is correct than only it's going to get placed on map, otherwise we'll ask again
    # and correct ans counter will be increases
    if answer_state in file.data_list:
        file.data_update(answer_state)
        n += 1
        guessed_states.append(answer_state)

# this fun takes two arguments as x and y position and print it
# def get_cmouse_click_coor(x, y):
#     print(x, y)
#
#
# # this attribute listen to the click on the screen, and passes x and y coordinates in the function of that point
# # on screen
# turtle.onscreenclick(get_cmouse_click_coor)
#
# # it does tha same work as exit on screen, but we need click for position so screen should stay open
# # that's why mainloop()
# turtle.mainloop()
screen.exitonclick()