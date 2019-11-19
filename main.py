import module.movies_api_consumption as apirequest
import flask


def movie_ingestion(request):
    json_request=request.get_json()
    
    api_results = apirequest.getapidata(json_request["path"],json_request["api_key"])

    response= '{\"' + json_request["path"] + '\":' + str(api_results) + "}"
    return response