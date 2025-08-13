# Projeto B2BFlow - Desafio

Projeto desenvolvido para o desafio da B2BFlow.  
Backend em Python usando FastAPI para gerenciar contatos e enviar mensagens via API externa.

---

### Tecnologias Usadas
- Python
- FastAPI
- Supabase
- SQLAlchemy
- Dotenv
- Requests

## Setup

### Pré-requisitos
- Python 3.13.5
- FastAPI 0.116.1
- Conta no Supabase criada e configurada
- Conta no Z-API criada e configurada 

### 1. Criar tabela no Supabase

A tabela `contacts` não precisa ser criada manualmente. Ela é criada automaticamente pelo ORM SQLAlchemy na primeira execução da aplicação, baseado no modelo definido no código. Isso facilita a manutenção e garante que o esquema esteja sempre atualizado.


| Coluna | Tipo     | Observação             |
|--------|----------|-----------------------|
| id     | UUID     | Primary Key, auto-gerado|
| name   | text     | Não nulo              |
| phone  | text     | Não nulo, único       |


### 2. Variáveis de ambiente

Você vai precisar configurar duas partes diferentes no arquivo `.env` (pode ser um único arquivo ou dois separados):

#### Para a Z-API(env/zapi.env)
```env
CLIENT_TOKEN=seu_client_token_aqui
INSTANCE_ID=sua_instance_id_aqui
TOKEN=seu_token_aqui
```

#### Para o Supabase (env/supabase.env)
```env
SUPABASE_KEY=sua_supabase_key_aqui
SUPABASE_URL=sua_supabase_url_aqui

DATABASE_CLIENT=seu_database_client_aqui
DB=sua_string_de_conexao_ao_banco
```
---

### 3. Rodar o projeto
1. Instale as dependências:

```bash
    pip install -r requirements.txt
```

2. Execute o servidor FastAPI:
```bash
    uvicorn main:app --reload
```

3. Após iniciar, a documentação automática estará disponível
```bash
    http://localhost:8000/docs
```

---




### Endpoints

| Método | Rota                    | Descrição                          |
|--------|-------------------------|----------------------------------|
| POST   | `/v1/contacts`           | Criar um novo contato             |
| GET    | `/v1/contacts`           | Listar todos os contatos          |
| GET    | `/v1/contacts/get-by-phone`   | Buscar contato pelo telefone      |
| POST   | `/v1/contacts/send-message-all` | Enviar mensagem para todos contatos
| DELETE | `/v1/contacts`           | Deletar todos os contatos         |
| DELETE | `/v1/contacts/delete-by-phone` | Deletar contato pelo telefone  |

## Criação de contato

#### Exemplo de requisição para criar contato

```json
{
  "name": "Jonnathas",
  "phone": "5511999999999"
}
```

#### Resposta de sucesso
```json
{
  "status": "success",
  "message": "Contact created successfully"
}
```


## Envio de mensagem

#### Resposta de sucesso ao enviar mensagem
```json
{
  "phone": "55119599999999",
  "status": "success",
  "message": "Message sent successfully"
}
```

#### Resposta de erro ao enviar mensagem

```json
{
  "status": "error",
  "error": "No contacts found"
}
```

## Testes

### Como rodar os testes

Para rodar os testes, use o comando abaixo no terminal, a partir da raiz do projeto:

```bash
python -m pytest tests/nome_do_arquivo.py
```
Se quiser rodar todos os testes da pasta:

```bash
python -m pytest tests/
```
---

### Considerações Finais
Este projeto foi desenvolvido como parte do desafio técnico da B2BFlow para demonstrar conhecimentos em backend com FastAPI, manipulação de banco de dados via ORM e integração com APIs externas.

Fique à vontade para explorar o código, contribuir e sugerir melhorias. Qualquer dúvida, estou à disposição!