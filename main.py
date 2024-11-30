from turtle import Turtle, Screen
import pandas as pd

# Setup the screen and turtle
turtle = Turtle()
screen = Screen()
screen.title("U.S State Guessing Game")
image = "bs.gif"  # Replace with your map image file
screen.addshape(image)
turtle.shape(image)

# Load the CSV data
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()

# Function to display a state's name at its coordinates
def write_state_on_map(state_name):
    state_data = data.loc[data["state"] == state_name].iloc[0]
    x, y = state_data["x"], state_data["y"]
    
    marker = Turtle()
    marker.hideturtle()
    marker.penup()
    marker.goto(x, y)
    marker.write(state_name, align="center", font=("Arial", 12, "normal"))

# Game logic
guessed_states = []
while len(guessed_states) < len(all_states):
    answer = screen.textinput(
        f"{len(guessed_states)}/{len(all_states)} States Correct",
        "What's another state's name?"
    )
    
    if answer is None: 
        break
    
    answer = answer.title() 
    
    if answer == "Exit":
        break
    
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        write_state_on_map(answer)

guessed_states_df = pd.DataFrame(guessed_states, columns=["Guessed States"])
guessed_states_df.to_csv("guessed_states.csv", index=False)
screen.mainloop()

