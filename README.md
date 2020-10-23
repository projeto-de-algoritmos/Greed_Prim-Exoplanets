# Prim-Exoplanets

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Greed<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0129411  |  Guilherme Mendes Pereira |
| 17/0163571 |  Murilo Loiola Dantas |

## Sobre 
O projeto busca representar tridimensionalmente a árvore geradora mínima de todos os exoplanetas decobertos até o momento (com algumas exceções), tendo a Terra como raíz. A árvore geradora mínima foi calculada utilizando o Algoritmo de Prim. Na representação, as distâncias e posições de cada planeta (pontos) são proprocionais aos valores reais.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python<br>
**Framework**: (caso exista)<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.

## Uso 
* Clone o repositório:
```bash
git clone https://github.com/projeto-de-algoritmos/Greed_Prim-Exoplanets.git
```
* Acesse o repositório e instale as bibliotecas necessárias:
```bash
cd Greed_Prim-Exoplanets/
pip3 install -r requirements.txt
```
* Execute visualizaton.py e aguarde a plotagem do Prim-Exoplanets:
```bash
python3 src/visualizaton.py
```
* Após a execução será possível a visualização do gráfico gerado no browser.
 
## Outros
* Os dados necessários para calcular a distância entre os planetas foram tirados daqui: [NASA - Confirmed Planets](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=planets).
* Nem todos os planetas descobertos foram utilizados no projeto. 10 planetas não continham um valor de distância na planilha e, por isso, foram descartados. Outros apenas foram descobertos muito recentemente e ainda não estão catalogados.
* O grafo gerado a partir da tabela e utilizado como base para o Algoritmo de Prim possui 18.344.089 arestas, representando todas as distâncias entre todos os 4.283 vértices/planetas.