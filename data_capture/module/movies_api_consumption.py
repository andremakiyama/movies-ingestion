import requests,json

def getapidata(path,key):
    api_string='https://api.themoviedb.org/3/movie/' + path + '?api_key='+key
    print("API Consumption string: " + api_string)

    try:
        request = requests.get(api_string)
        try:
            api_results = re.sub("}, {", '}\n{', json.dumps(request.json()['results']))[0:-1]
        except:
            api_results = json.dumps(request.json())
        if len(api_results) <= 0:
            print("Dados não encontrados")
            system.exit(2)
            
        return api_results
    except Exception as e:
        print(e)