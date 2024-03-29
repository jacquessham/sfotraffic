TRUNCATE TABLE OUT__SFO_STATS.OUT__CARGO_FLIGHTS_STATISTICS CASCADE;

INSERT INTO OUT__SFO_STATS.OUT__CARGO_FLIGHTS_STATISTICS(
	CARGO_AIRCRAFT_TYPE,
	CARGO_TYPE_CODE,
	CARGO_WEIGHT,
	ACTIVITY_TYPE,
	AIRLINE_RECORD_ID,
	LOCATION_ID,
	FLIGHT_DATE
) SELECT
	L.CARGO_AIRCRAFT_TYPE,
	L.CARGO_TYPE,
	L.CARGO_WEIGHT_TONS,
	L.ACTIVITY_TYPE,
	M.AIRLINE_RECORD_ID,
	R.LOCATION_ID,
	L.ACTIVITY_PERIOD
FROM STG__SFO_STATS.UNIQUE__CARGO_STATISTICS AS L
JOIN OUT__SFO_STATS.OUT__AIRLINE AS M
ON L.PUB_CODE = M.ITAT_CODE AND L.PUB_AIRLINES = M.AIRLINE_NAME
JOIN OUT__SFO_STATS.OUT__DESTINATION_ORIGIN AS R
ON L.GEO_SUMM = R.GEO_SUMM AND L.GEO_REGION = R.GEO_REGION
;