# Projeto Restaurante: Sistema de Gerenciamento de Restaurantes

## Descrição

Este projeto em Python visa criar um sistema simples para gerenciar restaurantes, seus cardápios, avaliações e integração com uma API externa. O sistema permite:

- **Criar restaurantes:** Defina o nome, categoria e gerencie o status (ativo/inativo).
- **Gerenciar cardápio:** Adicione pratos e bebidas ao cardápio com nome, preço e descrição.
- **Aplicar descontos:** Implemente descontos específicos para pratos e bebidas.
- **Avaliar restaurantes:** Simule avaliações de clientes com notas.
- **Calcular média de avaliações:** Exiba a média de avaliações de cada restaurante.
- **Integrar com API:** Busca dados de restaurantes de uma API externa, formata e salva em arquivos JSON.
- **API com FastAPI:** Cria uma API REST para consultar os dados dos restaurantes.

## Funcionalidades

### Restaurante

- **Cadastro:** Nome, categoria.
- **Status:** Ativo/Inativo.
- **Cardápio:** Lista de pratos e bebidas.
- **Avaliações:** Armazena avaliações de clientes.
- **Média de avaliações:** Calcula e exibe a média.

### Cardápio

- **Pratos:** Nome, preço, descrição, desconto.
- **Bebidas:** Nome, preço, tamanho, desconto.

### API Externa

- Coleta dados de restaurantes da API: `https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`.
- Formata os dados e salva em arquivos JSON individuais por restaurante.

### API REST (FastAPI)

- **Rota `/api/hello`:** Exibe mensagem de boas-vindas.
- **Rota `/api/restaurantes/`:** 
    - Sem parâmetros: Retorna dados de todos os restaurantes.
    - Com parâmetro `restaurante`: Retorna o cardápio do restaurante especificado.

## Como Executar

1. **Pré-requisitos:** Python 3.7+ instalado.
2. **Instalar dependências:** `pip install -r requirements.txt`
3. **Executar o arquivo principal:** `python main.py`
4. **API FastAPI:** 
    - Inicie o servidor: `uvicorn main:app --reload`
    - Acesse a documentação da API em: `http://127.0.0.1:8000/docs`