CREATE TABLE "fact_fixtures" (
  "id" integer PRIMARY KEY,
  "date" timestamp,
  "venue_id" integer,
  "home_team_id" integer,
  "away_team_id" integer,
  "goals_home" integer,
  "goals_away" integer,
  "score_half_home" integer,
  "score_half_away" integer,
  "score_full_home" integer,
  "score_full_away" integer,
  "status_long" varchar(30)
);

CREATE TABLE "dim_teams" (
  "id" integer PRIMARY KEY,
  "name" varchar(30),
  "logo" varchar(100)
);

CREATE TABLE "dim_venues" (
  "id" integer PRIMARY KEY,
  "name" varchar(30),
  "city" varchar(30),
  "capacity" integer,
  "image" varchar(100)
);

CREATE TABLE "fact_events" (
  "id" integer PRIMARY KEY,
  "fixtureId" integer,
  "time" integer,
  "teamId" integer,
  "playerId" integer,
  "assistId" integer,
  "type" varchar(20),
  "detail" varchar(20),
  "comment" varchar(20)
);

CREATE TABLE "dim_players" (
  "id" integer PRIMARY KEY,
  "name" varchar(30),
  "age" integer,
  "nationality" varchar(20),
  "height" integer,
  "weight" integer
);

CREATE TABLE "fact_team_statistics" (
  "id" integer PRIMARY KEY,
  "fixtureId" integer,
  "teamId" integer,
  "type" varchar(20),
  "value" integer
);

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("home_team_id") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("away_team_id") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("venue_id") REFERENCES "dim_venues" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("playerId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("assistId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_team_statistics" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_team_statistics" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;