from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import pandas as pd
import matplotlib.pyplot as plt
import base64

from io import BytesIO

llm = LlamaCpp(model_path="/path/to/llama-3.1.bin")

prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="Dados: {data_description}\nPergunta: {question}\nAnálise:",
)

llm_chain = LLMChain(llm=llm, prompt=prompt_template)

def analyze_data(file_path, question):
    df = pd.read_csv(file_path)
    data_description = f"DataFrame com {df.shape[0]} linhas e {df.shape[1]} colunas. Colunas: {', '.join(df.columns)}"
    response = llm_chain.run(data_description=data_description, question=question)
    return response


def generate_graph(file_path):
    df = pd.read_csv(file_path)
    numeric_column = df.select_dtypes(include=['number']).columns[0]
    plt.figure(figsize=(10, 5))
    plt.hist(df[numeric_column])
    plt.title(f'Histograma de {numeric_column}')
    plt.xlabel(numeric_column)
    plt.ylabel('Frequência')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64