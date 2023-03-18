TRUNCATE TABLE OUT__SFO_STATS.OUT__DESTINATION_ORIGIN CASCADE;

INSERT INTO OUT__SFO_STATS.OUT__DESTINATION_ORIGIN(
	GEO_SUMM,
	GEO_REGION
)
SELECT DISTINCT
	GEO_SUMM,
	GEO_REGION
FROM STG__SFO_STATS.UNIQUE__PASSENGER_STATISTICS
UNION
SELECT DISTINCT
	GEO_SUMM,
	GEO_REGION
FROM STG__SFO_STATS.UNIQUE__CARGO_STATISTICS
UNION
SELECT DISTINCT
	GEO_SUMM,
	GEO_REGION
FROM STG__SFO_STATS.UNIQUE__CARGO_STATISTICS
;