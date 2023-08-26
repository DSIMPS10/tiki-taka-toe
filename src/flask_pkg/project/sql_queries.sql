CREATE TABLE Football_teams (
    id serial PRIMARY KEY,
    team_name VARCHAR (100) UNIQUE NOT NULL,
    league VARCHAR (100),
    country VARCHAR (100)
);

CREATE TABLE Players (
    id serial PRIMARY KEY,
    first_name VARCHAR (100),
    last_name VARCHAR (100),
    team_id INT NOT NULL,
	FOREIGN KEY (team_id)
      REFERENCES Football_teams (id)
	);