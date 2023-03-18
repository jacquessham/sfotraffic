psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/01_airline.sql
psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/02_destination_origin.sql
psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/03_activity_type.sql
psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/04_passenger_flights_statistics.sql
psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/05_cargo_flights_statistics.sql
psql -h localhost -p 8731 -U sfo -d sfo -a -f sql_executor/06_landing_statistics.sql