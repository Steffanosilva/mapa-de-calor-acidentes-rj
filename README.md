# 🗺️ Mapa de Calor de Acidentes de Trânsito – Rio de Janeiro (2024)

Este repositório apresenta um **mapa de calor interativo** com base nos registros de acidentes de trânsito ocorridos no Estado do Rio de Janeiro no ano de 2024.  
O objetivo é facilitar a **visualização espacial** das ocorrências, auxiliando análises geográficas, acadêmicas e exploratórias sobre segurança viária.


---

## 📁 Estrutura do Repositório

O projeto contém os seguintes arquivos e pastas:

.vscode/ <br>
acidentes-rj.py <br>
levantamento_de_acidentes_cprv_2024.csv <br>
mapa_calor_acidentes_rj.html <br>



### 🔹 Descrição dos Arquivos

- **`.vscode/`**  
  Pasta de configuração do Visual Studio Code utilizada durante o desenvolvimento.

- **`acidentes-rj.py`**  
  Script em Python responsável pelo processamento dos dados e geração do mapa de calor a partir das coordenadas geográficas (latitude e longitude).

- **`levantamento_de_acidentes_cprv_2024.csv`**  
  Base de dados em formato CSV contendo os registros de acidentes, incluindo informações geográficas.

- **`mapa_calor_acidentes_rj.html`**  
  Arquivo HTML gerado automaticamente pelo script Python.  
  Contém o **mapa de calor interativo**, pronto para visualização em navegador.


---

## 🌍 Como Visualizar o Mapa de Calor

### ✔️ Opção 1 — Visualização Local (Recomendada)

1. Faça o download ou clone este repositório:
   ```bash
   git clone https://github.com/Steffanosilva/mapa-de-calor-acidentes-rj.git
2. Localize o arquivo:
  ```bash
  mapa_calor_acidentes_rj.html
  ```
3. Clique duas vezes no arquivo ou: <br>
   * Clique com o botão direito <br>
   * Selecione **"Abrir com"** <br>
   * Escolha um navegador (Google Chrome, Edge ou Firefox)

📌 O mapa será carregado localmente com interatividade completa (zoom, deslocamento e camadas).


---

## 📊 Fonte dos Dados

Os dados utilizados neste projeto foram obtidos a partir do portal oficial de Dados Abertos do Governo do Estado do Rio de Janeiro:

* **Base de dados:** Levantamento de Acidentes - CPRv
* **Link direto:** https://dadosabertos.rj.gov.br/de/dataset/levantamento-de-acidentes/resource/0341a2ca-aeef-4c89-8891-64ac998939de


---

## 🧠 Tecnologias Utilizadas

* Python <br>
* Pandas <br>
* Folium <br>
* Leaflet.js <br>
* HTML
