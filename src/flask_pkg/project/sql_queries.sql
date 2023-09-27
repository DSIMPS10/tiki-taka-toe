CREATE TABLE Football_teams (
    id serial PRIMARY KEY,
    team_name VARCHAR (100) UNIQUE NOT NULL,
    league VARCHAR (100),
    country VARCHAR (100)
);

CREATE TABLE Players (
    id serial PRIMARY KEY,
    full_name VARCHAR (150),
    team_id INT NOT NULL,
	team_name VARCHAR (100),
	first_season INT NOT NULL,
	last_season INT NOT NULL,
	FOREIGN KEY (team_id)
      REFERENCES Football_teams (id)
	);

CREATE TABLE Guesses (
    id serial PRIMARY KEY,
    full_name VARCHAR (100),
    team_1 VARCHAR (100),
    team_2 VARCHAR (100),
    correct_guesses INT
	);

CREATE TABLE Grids (
    id serial PRIMARY KEY,
    pos_a  VARCHAR(150),
    pos_b  VARCHAR(150),
    pos_c  VARCHAR(150),
    pos_x  VARCHAR(150),
    pos_y  VARCHAR(150),
    pos_z  VARCHAR(150),
    total_score INT NOT NULL,
    max_matches INT NOT NULL,
    min_matches INT NOT NULL,
    mode_matches INT NOT NULL,
    median_matches INT NOT NULL,
    percentage_completion NUMERIC NOT NULL,
	);
