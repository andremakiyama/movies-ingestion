Este programa foi desenvolvido para capturar dados de filmes da plataforma themoviedb(api.themoviedb.org)

O programa foi desenvolvido pensando na plataforma da Google GCP utilizando Python

1) Função para coletar os dados vindos da API de filmes
Para realizar o deploy da GCP Functions, cujo objetivo do método é escutar no path uma chamada para realizar o consumo da API:
gcloud functions deploy movie_ingestion --runtime python37 --trigger-http


chamada da API:
{"path":"now_playing", "api_key":"3a759be71aa9bae9de1e0621d0ef7f14"}