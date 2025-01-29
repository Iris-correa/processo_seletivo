# Desafio Técnico - Capitani Group
---
## Descrição do processo de solução

Neste processo o objetivo é gerar um arquivo posicional simulando a geração de um código para cada compra de um produto. Em cada código obtem-se as variáveis, sendo elas número do pedido, quantidade do produto e valor unitário do produto, respectivamente. Após obter esses valores é calculado o valor total de cada pedido *(valor total = quantidade x valor unitário)* e posteriormente salvar um relatório dos 5 pedidos com os valores mais altos.  

**Organização do projeto**:

├── src/               # Diretório do código-fonte principal
│   ├── files/ # Diretório de arquivos
│   │   ├── orders_code.txt # arquivo de entrada
│   │   ├── report_top_5.txt # relatório de saída
│   ├── generetor/           # Diretório dos módulos
│   │   ├── file_input_generetor.py # script para gerar o arquivo de entrada
│   │   ├── report_generetor.py # script para gerar o relatório
│   └── README.md   

## file_input_generetor.py
---
Este script tem o objeto de gerar o arquivo posicional de entrada. Sua construção é feita por duas funções:

- **positional_lines(i)**
 Gerar separadamente os valores necessários para contemplar o código de cada pedido, utilizando a biblioteca random e zfill() para limitar os caracteres de cada variável. 
 Parâmetros: Recebe o índicie da quantidade de linhas para interar o número do pedido em sequência.

 - **file_save(file_path, num_lines)**
 Unificar as 3 variaveis em uma linha e salvar cada linha posicional de entrada no respectivo diretório.
 Parâmetros: caminho do arquivo e número de linhas que serão geradas. 

 ## report_generetor.py
---
 Este script tem o objeto de processar o arquivo de entrada e gerar o relatório com os top 5 pedidos de maior valor. Sua construção é feita pelas seguintes funções:

 - **process_line(line)**
 Recebe a linha a ser processada, utiliza a sintaxe slicing para buscar os valores de cada variável separadamente com o padrão de índice por posição. Após localizar esses valores é feito o cálculo de valor total do pedido e retornado com o número do pedido.
 Parâmetros: Recebe a linha a ser processada.

 - **process_file(file_path)**
 Lê o arquivo de entrada por linha, utilizando a função anterior *(process_line(line))* para processar e retonar os valores totais com o número do pedido em tuplas adicionando em uma lista com todos os pedidos e seus valores. Após a lista gerada é feito a ordenação pegando apenas o segundo valor de cada tupla com o reverse como true (ordenação decrescente) e retornando apenas os 5 maiores. 
 Parâmetro: caminho do arquivo de entrada.

- **save_file_top_five(top_five, file_path)**
Salva o relatório em txt no diretório recebido como parâmetro.

## Decisões de projeto e justificativas
---
**Gerar o arquivo de entrada:**

Para não ocorrer problemas caso não tenha o arquivo de entrada, facilitar e garantir cada linha com a padronização correta.

**Utilizar a sintaxe slicing:**

Teria também a possibilidade de utilizar o regex, porém como o padrão de cada linha é fixa e não existem preocupações com a variação de posicionamento, utilizar slicing é mais simples e mais rápido. 

**Utilizar Try e execep:**

Caso ocorra algum problema em abrir/escrever um arquivo ou processar o arquivo posicional, ele captura o erro e retorna para facilitar o debug.

**Separar os arquivos em diretórios diferentes:**

Facilidade na execução e o entendimento para futuras refatorações.

## Possíveis Melhorias
---

- Utilização de pandas/pyspark para melhorar o processamento e a capacidade conforme for aumentando a quantidade de pedidos.

- Separar as funções dos arquivos de geração para mais módulos e facilitar ainda mais manutenções futuras.

- Implementar testes unitários, funcionais ou de aceitação.

- Retornar o relatório em csv/json para integrar com uma plataforma de monitoramento para análise de dados.

- Conectar com um banco de dados relacional e armazenar esses dados e disponibilizar com variação temporal. 

- Gerar uma DAG que orquestre o projeto e rode em determinado tempo para disponibilizar o relatório automaticamente.

##  Execução do programa
---
Verifique se o python 3 está instalado na sua máquina:

- Abra o terminal

`python3 --version`

caso não esteja, procure como instalar em seu SO.

Acesse o diretório do projeto.

Execute o seguinte comando:

`python main.py`

E verifique se os dois arquivos foram gerados/atualizados na paste files.






