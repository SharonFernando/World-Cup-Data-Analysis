CREATE TABLE "fact_fixtures" (
  "id" integer PRIMARY KEY,
  "date" timestamp,
  "venueId" integer,
  "homeTeamId" integer,
  "awayTeamId" integer,
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
  "fixtureId" integer,
  "time" integer,
  "teamId" integer,
  "playerId" integer,
  "assistId" integer,
  "type" varchar(50),
  "detail" varchar(100),
  "comments" varchar(100)
);

CREATE TABLE "dim_players" (
  "id" integer PRIMARY KEY,
  "name" varchar(100),
  "age" integer,
  "nationality" varchar(100),
  "height" integer,
  "weight" integer
);

CREATE TABLE "fact_stats" (
  "id" integer PRIMARY KEY,
  "fixtureId" integer,
  "teamId" integer,
  "type" varchar(50),
  "value" integer
);

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("homeTeamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("awayTeamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_fixtures" ADD FOREIGN KEY ("venueId") REFERENCES "dim_venues" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("playerId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_events" ADD FOREIGN KEY ("assistId") REFERENCES "dim_players" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_stats" ADD FOREIGN KEY ("fixtureId") REFERENCES "fact_fixtures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "fact_stats" ADD FOREIGN KEY ("teamId") REFERENCES "dim_teams" ("id") DEFERRABLE INITIALLY IMMEDIATE;
