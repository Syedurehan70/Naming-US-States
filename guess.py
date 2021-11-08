from turtle import Turtle
import pandas

FONT = ("Arial", 8, "normal")


# inherited class
class Guess(Turtle):
    def __init__(self):
        super().__init__()
        # sets turtle, read file
        self.hideturtle()
        self.penup()
        self.data = pandas.read_csv("50_states.csv")
        # convert it in list
        self.data_list = self.data["state"].to_list()

# this func sends ans to their coordinates
    def data_update(self, answer_state):
        # getting hold of specific row of answer_state
        state = self.data[self.data["state"] == answer_state]
        # getting hold of answer_state row coordinates
        state_x = int(state["x"])
        state_y = int(state["y"])
        self.goto(state_x, state_y)
        self.write(answer_state, align="center", font=FONT)

    def exit(self, guessed_states):
        # list comprehension applied
        un_guessed_states = [state for state in self.data_list if state not in guessed_states]
        remains = pandas.DataFrame(un_guessed_states)
        remains.to_csv("missed_states.csv")
