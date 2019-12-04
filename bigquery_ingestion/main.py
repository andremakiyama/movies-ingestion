import json
import logging
import os
import traceback
from datetime import datetime

from google.cloud import bigquery
from google.cloud import storage
import pytz

BQ = bigquery.Client()
bq_dataset = "raw_data"

CS = storage.Client()
gcp_folder_raw="rawdataprepare/"
bucket_name= "movies-rawdata-prepare"

def json_bigquery_ingestion(data, context):
    bucket_name = data['bucket']
    file_name = data['name']
    print("Iniciating the raw ingestion process " + file_name)
    try:
        insert_into_bigquery(bucket_name, file_name)
    except Exception as e:
         print(e)

def insert_into_bigquery(bucket_name, file_name):
    file_name_params = file_name.split("-")
    file_path = file_name_params[0]
    timestamp = file_name_params[1]

    print(file_path)
    print(timestamp)
    file_path_split = file_path.split("/")
    table_name = file_path_split[1]
    
    table = BQ.dataset(bq_dataset).table(table_name)
    dataset_ref = BQ.dataset(bq_dataset)
    
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

    uri = "gs://"+ bucket_name + "/" + file_name
    print("URI: " + uri)
    
    load_job = BQ.load_table_from_uri(
        uri, dataset_ref.table(table_name), job_config=job_config
    )  # API request
    print("Starting job {} ".format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print("Job finished. ")

    destination_table = client.get_table(dataset_ref.table(file_path))
    print("Loaded {} rows. ".format(destination_table.num_rows))

