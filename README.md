# Naming-US-States

First we've a CSV file name 50_states.csv by a code commented right at tthe bottom of main.py, (cuz it was just one time use) there we've included all the U.S States names.
Then, we,ve shaped our turtle in blank_states_img.gif and make it cover the whole screen, and by the help of that code we clicked on speciffic part of screen,
and it gives us the x-y coordinates of that part. For all 50 states we get the positions.

After creating CSV, we run the while loop which creates a prompt first than ask us to guess state, we already created a list of states in guess.py so whatever we write
in prompt if it's not in that list nothing will happpen.

If guessed the right state name, the name will move to it's marked location on a map.

In order exit the program we have write exit in prompt.

Once we write exit, an exit method in guess.py will check the answer we've given correctly and will generate a Dataframe of the states which we were unable to guess
by a name of missed_states.csv

