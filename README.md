--Finalidade
Este programa foi desenvolvido para capturar dados de filmes da plataforma themoviedb(api.themoviedb.org)

--Ferramentas utilizadas
O programa foi desenvolvido na plataforma da Google Cloud utilizando a linguagem Python
    Ferramentas GCP utilizadas - Build, Repository, Functions, BigQuery, Logs 

--Deploy
O código está no git https://github.com/andremakiyama/movies-ingestion e foi criada uma esteira por etapa da aplicação utilizando  Build e Repository. Ou seja, a cada commit na branch master do git, ocorrerá o build e o deploy na ferramenta Functions

--Aplicação
A ingestão via API está divida em duas partes - foi desenvolvida deste modo para que fosse possível utilizar a função schema auto detection do BigQuery, que possibilita a criação da tabela e ingestão de dados dinamicamente sem a necessidade de "modelar" a tabela previamente. Mantendo assim a camada de dados "RAW" e possibilitando a captura e possível utilização de dados principalmente de cunho exploratório com maior agilidade sem a necessidade de um modelador da base
    1)Coleta dos dados das APIs de filmes
    2)Ingestão dos dados no GCP BigQuery

1)data_capture Função para coletar os dados vindos da API de filmes e persistir o JSON no GCP Storage na pasta 'rawdataprepare'
Chamada da API(linux):

curl -X POST "https://us-central1-movies-dataflow.cloudfunctions.net/movie_capture_json" -H "Content-Type:application/json" --data '{"path":"now_playing", "api_key":"1t87gn18sehm8wqhk8wem", "tablename":"now_playing"}'

curl -X POST "https://us-central1-movies-dataflow.cloudfunctions.net/movie_capture_json" -H "Content-Type:application/json" --data '{"path":"3", "api_key":"1t87gn18sehm8wqhk8wem", "tablename":"movie_info"}'

Aonde:
    path= caminho/rota da API que deseja consumir(do site TheMovieDb)
    api_key= chave da API gerada pelo site themoviedb para sua aplicação


2)bigquery_ingestion Coleta o JSON no Storage e persiste seus dados no GCP BigQuery
No caso deste fluxo, assim que o dado for coletado e enviado ao Storage pela parte 1, a trigger será acionada automaticamente e os dados serão persistidos dentro do dataset 'raw_data'