from google.cloud import storage

storageClient = storage.Client()
bucket = storageClient.get_bucket('movies-rawdata-prepare')
foldername= "rawdataprepare/"

def saveFile(filename, text):
    print("Writting JSON into Storage "+foldername)
    try:
        blob = bucket.blob(foldername+filename)
        blob.upload_from_string(text)
        return 0
    except e:
        print(e)