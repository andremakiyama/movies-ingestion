import json
import logging
import os
import traceback
from datetime import datetime

from google.cloud import bigquery
from google.cloud import storage
import pytz

BQ = bigquery.Client()
BQ_DATASET = 'raw_data'

def json_bigquery_ingestion(data, context):
    bucket_name = data['bucket']
    file_name = data['name']

    try:
         insert_into_bigquery(bucket_name, file_name)
    except Exception:
         print(Exception)
            

def insert_into_bigquery(bucket_name, file_name):
    blob = CS.get_bucket(bucket_name).blob(file_name)
    
    row = json.loads(blob.download_as_string())
    table = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
    print("CONTEUDO DO JSON? " + row)
    
    #errors = BQ.insert_rows_json(table,
     #                            json_rows=[row],
      #                           row_ids=[file_name],
       #                          retry=retry.Retry(deadline=30))
    if errors != []:
        raise BigQueryError(errors)

