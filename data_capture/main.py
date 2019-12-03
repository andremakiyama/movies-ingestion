import module.movies_api_consumption as apirequest
import module.gcp_raw_storage_persist as gcp_rawpersist
import re

from pytz import timezone
import datetime
import flask


brasil_timezone = timezone("Brazil/East")
dateTimeObj = datetime.datetime.now(brasil_timezone)
timestampStr = dateTimeObj.strftime("%Y%m%d-%H%M%S")

def movie_capture_json(request):
    json_request=request.get_json()
    tablename = re.sub('[^a-zA-Z0-9 \n\.]', '_', str(json_request["tablename"]))
    filename = tablename + "_" +timestampStr
    
    api_results = str(apirequest.getapidata(json_request["path"],json_request["api_key"]))
    results = re.sub('None', '"none"', re.sub('False', 'false', re.sub('True', 'true', api_results)))
    
    #json_file= "{'dbname':" + "'" + tablename + "'," + "'timestamp':" + "'," + timestampStr + "'," + "'data':" + results+ "}"
    corrected_json = re.sub("'", '"', results)
    gcp_rawpersist.saveFile(filename, corrected_json)
    
    return corrected_json