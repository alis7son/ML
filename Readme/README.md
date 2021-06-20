# Alisson Carvalho - Data Scientist

Modelo treinado utilizando o LinearRegression. 

### Arquitetura das pastas
Pasta "metrics" que salva as métricas de performace do modelo. Assim é possível acompanhar os resultados de cada novo treinamento.

"models" salva cada versão do modelo.

Obs: É possível cadastrar no banco de dados da aplicação as métricas e versões do modelo.
Também é posssível automatizar esses testes de performance do modelo através de tabelas fato e uma dimensão. Exportar
arquivo csv e aplicar a uma função que testa o modelo.

### Rotas
- POST
    ```/predict:``` versão final do modelo para previsão
        
        model inputs:
            -  X1: variável referente a classe social:1(A e B), 2(C)e 3(D e E)
            -  X2: variável referente a padrão de ingredientes: 1 (Produtos orgânicos/Especiais), 2 (Prod. Tradicionais)
            -  X3: variável referente ao tamanho - diâmetro (cm) entre: 15 e 50
        
        model output: 
        prediction: Valor numérico preço da pizza

- GET
    ```/model_health/<model_id>```: Metricas do modelo. MSE e f2_score. 
        
        model_id: id do modelo em produção