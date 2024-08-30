# Use a imagem base oficial completa do Python 3.12.5
FROM python:3.12.5

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instala as dependências adicionais que podem ser necessárias para o LLAMA
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Copia o resto do código da aplicação
COPY . .

# Cria o diretório de uploads
RUN mkdir -p uploads

# Expõe a porta que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]