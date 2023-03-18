export PGPASSWORD='sfo'
psql -h localhost -p 8731 -U sfo -d sfo -a -f ELT/create_tables.sql
cd ELT
python upload_data.py
psql -h localhost -p 8731 -U sfo -d sfo -a -f src_cleansing.sql
cd ..