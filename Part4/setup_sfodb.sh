export PGPASSWORD='sfo'
psql -h localhost -p 8731 -U sfo -d sfo -a -f ELT/create_tables.sql
cd ELT
python upload_data.py
psql -h localhost -p 8731 -U sfo -d sfo -a -f src_cleansing.sql
sh stg_transform.sh
cd ../gooddata
sh connect_datasource.sh
sh setup_ws.sh
cd ..