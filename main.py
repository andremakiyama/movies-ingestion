from flask import Flask, jsonify
import json
import module.movies_api_consumption as apirequest

def data_ingestion(request):
    data = request.get_json()


    return jsonify(data)