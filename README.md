# Ferramenta de Análise de Dados

Esta é uma ferramenta de análise de dados que utiliza Flask, LangChain, LLAMA 3.1, e Pandas para fornecer análises baseadas em perguntas sobre conjuntos de dados CSV.

## Configuração com Docker

1. Clone este repositório:
   ```
   git clone https://github.com/blpilla/data-analysis-tool.git
   cd data-analysis-tool
   ```

2. Baixe o modelo LLAMA 3.1 e coloque-o no diretório raiz do projeto.

3. Atualize o caminho do modelo em `app/models.py`:
   ```python
   llm = LlamaCpp(model_path="/app/llama-3.1.bin")
   ```

4. Crie o diretório 'uploads' e configure as permissões:
   ```
   mkdir uploads
   chmod 777 uploads
   ```

5. Construa e inicie os containers Docker:
   ```
   docker-compose up --build
   ```

6. Abra um navegador e vá para `http://localhost:5000`.

7. Faça upload de um arquivo CSV e faça uma pergunta sobre os dados.

## Configuração sem Docker

Se preferir executar sem Docker, siga estas etapas:

1. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```
   python run.py
   ```

## Estrutura do Projeto

- `app/`: Contém os principais componentes da aplicação.
- `static/`: Arquivos estáticos (CSS).
- `templates/`: Templates HTML.
- `uploads/`: Diretório para armazenar arquivos enviados pelos usuários.
- `config.py`: Configurações da aplicação.
- `run.py`: Script para executar a aplicação.
- `requirements.txt`: Lista de dependências.
- `Dockerfile`: Instruções para construir a imagem Docker.
- `docker-compose.yml`: Configuração para orquestrar os serviços Docker.

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT.
