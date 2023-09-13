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
    