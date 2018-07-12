-- Adminer 4.6.3-dev PostgreSQL dump

\connect "d888fp495haud5";

DROP TABLE IF EXISTS "checkins";
CREATE TABLE "public"."checkins" (
    "loc_id" integer NOT NULL,
    "user_id" integer NOT NULL,
    "comment" text,
    CONSTRAINT "checkins_loc_id_user_id" PRIMARY KEY ("loc_id", "user_id"),
    CONSTRAINT "checkins_loc_id_fkey" FOREIGN KEY (loc_id) REFERENCES locations(loc_id) ON DELETE CASCADE NOT DEFERRABLE,
    CONSTRAINT "checkins_user_id_fkey" FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE NOT DEFERRABLE
) WITH (oids = false);

COMMENT ON COLUMN "public"."checkins"."loc_id" IS 'combined with user_id';

COMMENT ON COLUMN "public"."checkins"."user_id" IS 'combined with loc_id';


DROP TABLE IF EXISTS "locations";
DROP SEQUENCE IF EXISTS locations_loc_id_seq;
CREATE SEQUENCE locations_loc_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."locations" (
    "loc_id" integer DEFAULT nextval('locations_loc_id_seq') NOT NULL,
    "zipcode" character varying(9) NOT NULL,
    "town" text NOT NULL,
    "state" text NOT NULL,
    "latitude" text NOT NULL,
    "longitude" text NOT NULL,
    "population" integer NOT NULL,
    CONSTRAINT "locations_loc_id" PRIMARY KEY ("loc_id")
) WITH (oids = false);


DROP TABLE IF EXISTS "users";
DROP SEQUENCE IF EXISTS users_user_id_seq;
CREATE SEQUENCE users_user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."users" (
    "user_id" integer DEFAULT nextval('users_user_id_seq') NOT NULL,
    "user_name" text NOT NULL,
    "real_name" text NOT NULL,
    "hash" character varying(255) NOT NULL,
    CONSTRAINT "users_user_id" PRIMARY KEY ("user_id")
) WITH (oids = false);


-- 2018-07-12 03:37:54.864393+00
