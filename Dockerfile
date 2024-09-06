# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o código da aplicação para dentro do container
COPY . .

# Define o comando padrão para iniciar o container, que será um shell
CMD ["bash"]
