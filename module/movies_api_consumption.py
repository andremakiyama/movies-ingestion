import requests

def getapidata(path,key):
    api_string='https://api.themoviedb.org/3/movie/' + path + '?api_key='+key
    print("API Consumption string: " + api_string)

    try:
        request= requests.get(api_string)
        
        api_results = request.json()['results']
        
        if len(api_results) <= 0:
            print("Dados não encontrados")
            system.exit(2)
            
        return api_results
    except Exception as e:
        print(e)
        sys.exit(1)