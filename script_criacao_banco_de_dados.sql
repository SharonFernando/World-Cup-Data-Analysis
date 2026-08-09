CREATE TABLE "fact_fixtures" (
  "id" integer PRIMARY KEY,
  "date" timestamp,
  "leagueId" integer NOT NULL,
  "seasonYear" integer NOT NULL,
  "venueId" integer NOT NULL,
  "homeTeamId" integer NOT NULL,
  "awayTeamId" integer NOT NULL,
  "goalsHome" integer,
  "goalsAway" integer,
  "scoreHalfHome" integer,
  "scoreHalfAway" integer,
  "scoreFullHome" integer,
  "scoreFullAway" integer,
  "statusLong" varchar(50)
);

CREATE TABLE "dim_teams" (
  "id" integer PRIMARY KEY,
  "name" varchar(100),
  "logo" varchar(100)
);

CREATE TABLE "dim_venues" (
  "id" integer PRIMARY KEY,
  "name" varchar(100),
  "city" varchar(100),
  "capacity" integer,
  "image" varchar(100)
);

CREATE TABLE "fact_events" (
  "id" integer PRIMARY KEY,
  "fixtureId" integer NOT NULL,
  "time" integer,
  "teamId" integer NOT NULL,
  "playerId" integer NOT NULL,
  "assistId" integer NOT NULL,
  "type" varchar(50),
  "detail" varchar(100),
  "comments" varchar(100)
);

CREATE TABLE "dim_players" (
  "id" integer PRIMARY KEY,
  "name" varchar(100),
  "teamId" integer NOT NULL,
  "position" varchar(50)
);

CREATE TABLE "fact_stats" (
  "id" integer PRIMARY KEY,
  "fixtureId" integer NOT NULL,
  "teamId" integer NOT NULL,
  "type" varchar(50),
  "value" integer
);

CREATE TABLE "dim_leagues" (
  "id" integer PRIMARY KEY,
  "name" varchar(100),
  "type" varchar(50),
  "logo" varchar(100),
  "countryName" varchar(50)
);

CREATE TABLE "dim_seasons" (
  "leagueId" integer NOT NULL,
  "year" integer NOT NULL,
  "start" timestamp,
  "end" timestamp,
  PRIMARY KEY ("leagueId", "year")
);

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("homeTeamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("awayTeamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("venueId") REFERENCES "dim_venues" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("leagueId") REFERENCES "dim_leagues" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("leagueId", "seasonYear") REFERENCES "dim_seasons" ("leagueId", "year") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("playerId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("assistId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_stats" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_stats" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "dim_seasons" ADD FOREIGN KEY ("leagueId") REFERENCES "dim_leagues" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "dim_players" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;