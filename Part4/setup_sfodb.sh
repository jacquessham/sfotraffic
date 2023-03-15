export PGPASSWORD='sfo'
psql -h localhost -p 8731 -U sfo -d sfo -a -f ELT/create_table.sql
