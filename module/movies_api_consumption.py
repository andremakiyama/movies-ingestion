import requests

def getapidata(path,key,log):
    api_string='https://api.themoviedb.org/3/movie/' + path + '?api_key='+key
    print("API Consumption string: " + api_string)
    log.debug("API Consumption string: " + api_string)
    try:
        a= requests.get(api_string)
        return a
    except Exception as e:
        log.error("e")
        sys.exit(1)