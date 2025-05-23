# 📊 Controle de Produção com SQLite

Este é um sistema simples de registro e análise da produção industrial usando Python e SQLite.  
Ele permite registrar produções, listar registros e calcular perdas com base em trocas de rolo.

## 🚀 Funcionalidades

- Registro de dados de produção:
  - Operador
  - Número da ordem
  - Tipo de aplicador
  - Código do produto
  - Quantidade total e atual
  - Horário de início e fim
  - Número de trocas de rolo
  - Ocorrências

- Listagem de registros em formato tabular
- Cálculo de perdas com base na quantidade esperada por troca de rolo

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- SQLite (banco de dados local)

## 🧩 Estrutura

- `controle_producao.py`: Arquivo principal com toda a lógica do programa
- `producao.db`: Banco de dados criado automaticamente ao executar o programa
- `.gitignore`: Ignora arquivos que não devem ser versionados (ex: banco de dados)

## ▶️ Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/controle-producao.git
   cd controle-producao
