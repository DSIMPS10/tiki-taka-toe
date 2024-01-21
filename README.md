# tiki-taka-toe

The app and API for the Tiki Taka Toe football grid guessing game. 

## Setup 

### Installations

- Use the requirements.txt file to import all the necessary python libraries

### Running the Flask API locally

- The API can run locally to connect to the Elephant SQL Postgres database
- The code for the flaks API is stored in the `flask_pkg` folder
- A `.env` file in the `flask_pkg` folder containing credentials for the database connection is required (see the `dotenv_example` file for the format required)

#### API steps:

1. Change cwd to flask_pkg: `cd tiki-taka-toe/src/flask_pkg`
2. Run the API locally on mac: `flask --app project run --debug` (for windows use: `python -m flask --app project run --debug`)
3. The API will now be running (you shoudl see in the terminal: Serving Flask app 'project')

### Running the tiki-taka-toe game

- The main logic for the game can be run from the `tic_tac_toe.py` file (in the `src` folder)

#### Game steps:

1. Change `cwd` to tiki-taka-toe/src folder
2. Run the file `tic_tac_toe.py` (can be done in the terminal)
3. Select level by typing one of the options: easy/medium/hard (will choose a grid with a corresponding level of dificulty)
4. A grid will appear with 6 teams (and a dictionary containing info on the grid selected)
5. Chose a position on the grid to guess a player for (index starts at 1 in the bottom left square)
6. Type in the index and the 2 corresponding teams will be printed out to guess a player for.
7. Guess a player and see if it's correct, if so a symbol (O or X) will appear in the grid
8. Keep going until someone wins!
