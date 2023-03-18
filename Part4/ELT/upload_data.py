import datetime
import json
import pandas as pd
from connect_db import *


# Read params to get files and metadata
params = json.load(open('elt_params.json'))
dataset2table = {
    'pax':'SRC__SFO_STATS.SRC__PASSENGER_STATISTICS',
    'cargo':'SRC__SFO_STATS.SRC__CARGO_STATISTICS',
    'landing':'SRC__SFO_STATS.SRC__LANDING_STATISTICS'
}

col_names = json.load(open('col_names.json'))

# Connect to db and get version
conn = connect_db()
cursor = conn.cursor()
upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Read file and upload data to db
for file, dataset, tag in zip(params['upload_file'], params['dataset'], params['upload_tag']):
    # Find table name
    table = dataset2table[dataset]

    # Find out version
    cursor.execute(f'select max(upload_version) from {table}')
    version = cursor.fetchone()[0]
    # If never upload, then version 1
    if version is None or version < 1:
        version = 1
    else:
        # psycopg2 will return some weird float format, so convert to int
        version = int(version) 
        version += 1

    # Read file to pandas
    df_curr = pd.read_csv(file, dtype=str)
    df_curr = df_curr.rename(columns=col_names[table])
    df_curr['UPLOAD_TIMESTAMP'] = upload_time
    df_curr['UPLOAD_TAG'] = tag
    df_curr['UPLOAD_VERSION'] = version

    # Upload data to db row by row
    rows = [tuple(x) for x in df_curr.to_numpy(na_value='None')]
    cols = ','.join(list(df_curr.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    
    # Execute query
    row_counter = 0
    for row in rows:
        query_curr_row = f'INSERT INTO {table}({cols}) VALUES {row}'
        cursor.execute(query_curr_row)
        conn.commit()
        row_counter += 1
        if row_counter % 1000 == 0:
            print(f'{row_counter} rows uploaded in {table}')

cursor.close()



