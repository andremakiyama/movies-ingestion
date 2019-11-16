#chamada {"path":"now_playing", "api_key":"3a759be71aa9bae9de1e0621d0ef7f14"}


import module.movies_api_consumption as apirequest
import flask


def movie_ingestion(request):
    json_request=request.get_json()
    
    response = apirequest.getapidata(json_request["path"],json_request["api_key"])

    api_results = ""
    try:
        api_results = response.json()['results']
        if len(api_results) <= 0:
            print("Dados não encontrados")
            system.exit(2)
    except Exception as e:
        print(e)
        exit(99)
    
    teste = str(api_results[0])
    return teste