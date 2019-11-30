from google.cloud import bigquery

client = bigquery.Client()
project = client.project
dataset_id = "raw_data"
tables=tablesList()
dataset_ref = client.dataset(dataset_id)
    
def executeQuery(query):
    query_job = client.query(query)  # API request
    result = query_job.result()  # Waits for query to finish
    return result

def tablesList():
    tables = client.list_tables(dataset_id)
    print("Tables contained in '{}':".format(dataset_id))
    tables_list=[]
    for table in tables:
        print("{}.{}.{}".format(table.project, table.dataset_id, table.table_id))
        tables_list+=table.table_id

def createTable(tablename):
    try:
        table = bigquery.Table(project+"."+dataset_id+"."+ tablename)
        table = client.create_table(table)
        
        print("Created table " + project+"."+dataset_id+"."+ tablename)
    except google.api_core.exceptions.Conflict:
        pass
        print("Table " + project+"."+dataset_id+"."+ tablename + "Already exists")
    except e:
        #TODO: improve error handling
        print(e)
    
def createTableSchemaDetection(uri,tablename):
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    load_job = client.load_table_from_uri(
        uri, dataset_ref.table(tablename), job_config=job_config
    )  # API request
    print("Starting job {}".format(load_job.job_id))
    load_job.result()  # Waits for table load to complete.
    print("Job finished.")
    destination_table = client.get_table(dataset_ref.table(tablename))
    print("Loaded {} rows.".format(destination_table.num_rows))

        