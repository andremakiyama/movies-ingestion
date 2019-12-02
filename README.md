Este programa foi desenvolvido para capturar dados de filmes da plataforma themoviedb(api.themoviedb.org)

O programa foi desenvolvido pensando na plataforma da Google GCP utilizando Python

1) Função para coletar os dados vindos da API de filmes e persistir o JSON no GCP Storage raw data
Para realizar o deploy da GCP Functions, cujo objetivo do método é escutar no path uma chamada para realizar o consumo da API:
Commit no GitHub branch master pasta data_capture
https://github.com/andremakiyama/movies-ingestion


chamada da API(linux):

curl -X POST "https://us-central1-movies-dataflow.cloudfunctions.net/movie_capture_json" -H "Content-Type:application/json" --data '{"path":"now_playing", "api_key":"3a759be71aa9bae9de1e0621d0ef7f14", "tablename":"now_playing"}'

curl -X POST "https://us-central1-movies-dataflow.cloudfunctions.net/movie_capture_json" -H "Content-Type:application/json" --data '{"path":"3", "api_key":"3a759be71aa9bae9de1e0621d0ef7f14", "tablename":"movie_info"}'

Aonde:
    path=caminho da API Movies
    api_key=chave da API para sua aplicação


2) Coleta dos arquivos e persistência dos dados no GCP BigQuery