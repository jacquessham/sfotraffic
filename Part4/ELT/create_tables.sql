-- Create Schema
\connect sfo;
CREATE SCHEMA IF NOT EXISTS SRC__SFO_STATS;
CREATE SCHEMA IF NOT EXISTS STG__SFO_STATS;
CREATE SCHEMA IF NOT EXISTS OUT__SFO_STATS;

-- For Source Stage
-- Create tables for source tables
CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__PASSENGER_STATISTICS (
	ACTIVITY_PERIOD VARCHAR(256),
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	PRICE VARCHAR(256),
	TERMINAL VARCHAR(256),
	BOARDING_AREA VARCHAR(256),
	PAX_COUNT VARCHAR(256),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__CARGO_STATISTICS(
	ACTIVITY_PERIOD VARCHAR(256),
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	CARGO_TYPE VARCHAR(256),
	CARGO_AIRCRAFT_TYPE VARCHAR(256),
	CARGO_WEIGHT_LBS VARCHAR(256),
	CARGO_WEIGHT_TONS VARCHAR(256),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__LANDING_STATISTICS(
	ACTIVITY_PERIOD VARCHAR(256),
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	LANDING_AIRCRAFT_TYPE VARCHAR(256),
	BODY_TYPE VARCHAR(256),
	AIRCRAFT_MANU VARCHAR(256),
	AIRCRAFT_MODEL VARCHAR(256),
	AIRCRAFT_VERSION VARCHAR(256),
	LANDING_COUNT VARCHAR(256),
	TOTAL_LANDED_WEIGHT VARCHAR(256),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

-- Create tables for source tables
CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__CLEAN__PASSENGER_STATISTICS (
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	PRICE VARCHAR(256),
	TERMINAL VARCHAR(256),
	BOARDING_AREA VARCHAR(256),
	PAX_COUNT NUMERIC(12,0),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__CLEAN__CARGO_STATISTICS(
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	CARGO_TYPE VARCHAR(256),
	CARGO_AIRCRAFT_TYPE VARCHAR(256),
	CARGO_WEIGHT_LBS NUMERIC(12,0),
	CARGO_WEIGHT_TONS NUMERIC(12,0),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS SRC__SFO_STATS.SRC__CLEAN__LANDING_STATISTICS(
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	LANDING_AIRCRAFT_TYPE VARCHAR(256),
	BODY_TYPE VARCHAR(256),
	AIRCRAFT_MANU VARCHAR(256),
	AIRCRAFT_MODEL VARCHAR(256),
	AIRCRAFT_VERSION VARCHAR(256),
	LANDING_COUNT NUMERIC(12,0),
	TOTAL_LANDED_WEIGHT NUMERIC(12,0),
	UPLOAD_TIMESTAMP TIMESTAMP,
	UPLOAD_TAG VARCHAR(256),
	UPLOAD_VERSION NUMERIC(12,0)
);

-- For Staging Stage
-- Create tables for stage tables to filter duplicated tables
CREATE TABLE IF NOT EXISTS STG__SFO_STATS.UNIQUE__PASSENGER_STATISTICS (
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	PRICE VARCHAR(256),
	TERMINAL VARCHAR(256),
	BOARDING_AREA VARCHAR(256),
	PAX_COUNT NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS STG__SFO_STATS.UNIQUE__CARGO_STATISTICS(
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	ACTIVITY_TYPE VARCHAR(256),
	CARGO_TYPE VARCHAR(256),
	CARGO_AIRCRAFT_TYPE VARCHAR(256),
	CARGO_WEIGHT_LBS NUMERIC(12,0),
	CARGO_WEIGHT_TONS NUMERIC(12,0)
);

CREATE TABLE IF NOT EXISTS STG__SFO_STATS.UNIQUE__LANDING_STATISTICS(
	ACTIVITY_PERIOD DATE,
	OP_AIRLINES VARCHAR(256),
	OP_CODE VARCHAR(256),
	PUB_AIRLINES VARCHAR(256),
	PUB_CODE VARCHAR(256),
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256),
	LANDING_AIRCRAFT_TYPE VARCHAR(256),
	BODY_TYPE VARCHAR(256),
	AIRCRAFT_MANU VARCHAR(256),
	AIRCRAFT_MODEL VARCHAR(256),
	AIRCRAFT_VERSION VARCHAR(256),
	LANDING_COUNT NUMERIC(12,0),
	TOTAL_LANDED_WEIGHT NUMERIC(12,0)
);

-- For Output Stage
-- Create tables for output stage connect to GoodData
CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__AIRLINE (
	ITAT_CODE VARCHAR(256) PRIMARY KEY,
	AIRLINE_NAME VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__DESTINATION_ORIGIN (
	LOCATION_ID VARCHAR(256) SERIAL PRIMARY KEY,
	GEO_SUMM VARCHAR(256),
	GEO_REGION VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__ACTIVITY (
	ACTIVITY_TYPE VARCHAR(256) PRIMARY KEY
);


CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__PASSENGER_FLIGHTS_STATISTICS (
	PASSENGER_RECORD_ID VARCHAR(256) SERIAL PRIMARY KEY,
	TERMINAL VARCHAR(256),
	BOARDING_AREA VARCHAR(256),
	PASSENGER_COUNT NUMERIC(12,2),
	ACTIVITY_TYPE VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__ACTIVITY (ACTIVITY_TYPE),
	IATA_CODE VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__AIRLINE (ITAT_CODE),
	LOCATION_ID VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__DESTINATION_ORIGIN (LOCATION_ID),
	PRICE_CATEGORY VARCHAR(256),
	FLIGHT_DATE TIMESTAMP
);

CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__CARGO_FLIGHTS_STATISTICS (
	CARGO_RECORD_ID VARCHAR(256) SERIAL PRIMARY KEY,
	CARGO_AIRCRAFT_TYPE VARCHAR(256),
	CARGO_TYPE_CODE VARCHAR(256),
	CARGO_WEIGHT NUMERIC(12,2),
	ACTIVITY_TYPE VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__ACTIVITY (ACTIVITY_TYPE),
	IATA_CODE VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__AIRLINE (ITAT_CODE),
	LOCATION_ID VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__DESTINATION_ORIGIN (LOCATION_ID),
	FLIGHT_DATE TIMESTAMP
);

CREATE TABLE IF NOT EXISTS OUT__SFO_STATS.OUT__LANDING_STATISTICS (
	LANDING_ID VARCHAR(256) SERIAL PRIMARY KEY,
	AIRCRAFT_BODY_TYPE VARCHAR(256),
	AIRCRAFT_MANUFACTURER VARCHAR(256),
	AIRCRAFT_MODEL VARCHAR(256),
	LANDING_AIRCRAFT_TYPE VARCHAR(256),
	LANDING_WEIGHT NUMERIC(12,2),
	LANDING_COUNT NUMERIC(12,0),
	LOCATION_ID VARCHAR(256) REFERENCES OUT__SFO_STATS.OUT__DESTINATION_ORIGIN (LOCATION_ID),
	FLIGHT_DATE TIMESTAMP
);
