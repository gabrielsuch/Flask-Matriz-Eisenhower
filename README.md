# Matriz de Eisenhower


| Critérios | Pts. |
|---|---|
| [POST] **/categories** - Retorno conforme solicitado caso esteja tudo correto e retorno como solicitado caso ocorra o erro . | 1 |
| [PATCH] **/categories** - Retorno conforme solicitado caso exista o id e retorno conforme solicitado caso não exista o id. | 1 |
| [DELETE] **/categories** - Retorno conforme solicitado caso exista o id e retorno conforme solicitado caso não exista o id. | 1 |
| [POST] **/tasks** - Retorno conforme solicitado caso esteja tudo correto, retorno conforme solicitado caso ocorra o erro, retorno conforme solicitado caso valores de importance ou urgency sejam superiores a 2 e lógica para definir prioridade. | 3 |
| [PATCH] **/tasks** - Retorno conforme solicitado caso exista o id e retorno conforme solicitado caso não exista o id. | 2 |
| [DELETE] **/tasks** - Retorno conforme solicitado caso exista o id e retorno conforme solicitado caso não exista o id. | 1 |
| [GET] **/** - Listar categorias com suas respectivas tasks conforme solicitado. | 3 |
| Configurações - Flask  migrate funcionando, arquivo requeriments.txt e .env | 3 |

#
# Categories

## POST /categories - Formato da Requisição

```json
{
  "name": "Reunião",
  "description": "Chegar no horario"
}
```

### Status 201 - Created:
```json
{
	"id": 1,
	"name": "Reunião",
	"description": "Chegar no horario"
}
```

### Status 400 - Bad Request:
```json
{
	"missing_keys": [
		"description"
	]
}
```

### Status 409 - Conflict:
```json
{
	"msg": "category already exists!"
}
```

#

## PATCH /categories/1 - Formato de Requisição
```json
{
	"description": "Não chegar atrasado"
}
```

### Status 200 - OK:
```json
{
	"id": 1,
	"name": "Reunião",
	"description": "Não chegar atrasado"
}
```

### Status 400 - Bad Request:
```json
{
	"wrong_keys": [
		"horario"
	]
}
```

### Status 404 - Not Found:
```json
{
	"msg": "category not found!"
}
```

#

## DELETE /categories/1 - Formato da Requisição

<br>

## Status 204 - No Content:
```json
"No body returned for response"
```

## Status 404 - Not Found:
```json
{
	"msg": "category not found!"
}
```

#

# Tasks

## POST /tasks - Formato da Requisição
```json
{
  "name": "Passeio",
  "description": "Sair quando tiver tempo",
  "duration": 100,
  "importance": 1,
  "urgency": 1,
  "categories": [
    "Casa", "Trabalho"
  ]
}
```

### Status 201 - Created:
```json
{
	"id": 1,
	"name": "Formatar PC",
	"description": "Formatar quando tiver tempo",
	"duration": 100,
	"classification": "Do It First",
	"categories": [
		"Casa",
		"Trabalho"
	]
}
```

### Status 400 - Bad Request:
```json
{
  {
	"msg": {
		"valid_options": {
			"importance": [1,2],
			"urgency": [1,2]
		},
		"received_options": {
			"importance": 4,
			"urgency": 1
		}
	}
  }
}
```

### Status 409 - Conflict:
```json
{
	"msg": "task already exists!"
}
```

#

## PATCH /tasks/1 - Formato da Requisição
```json
{
  "importance": 2,
  "description": "Mudança na descrição"
}
```

### Status 200 - OK:
```json
{
	"id": 1,
	"name": "Passeio",
	"description": "Mudança na descrição",
	"duration": 100,
	"classification": "Delegate It",
	"categories": [
		"Casa",
		"Trabalho"
	]
}
```

### Status 400 - Bad Request:
```json
{
	"wrong_keys": [
		"outro"
	]
}
```

### Status 404 - Not Found:
```json
{
	"msg": "task not found!"
}
```

#

## DELETE /tasks/1 - Formato da Requisição
```json
"No body"
```

### Status 204 - OK:
```json
"No body returned for response"
```

### Status 404 - Not Found:
```json
{
	"msg": "category not found!"
}
```

#

# Get Categories and Tasks

## GET / - Formato da Requisição
```json
"No body"
```

### Status 200 - OK:
```json
[
    "id": 1,
    "name": "Reunião",
    "description": "Chegar no horário",
    "tasks": [
        {
            "id": 1,
            "name": "Apresentação",
            "description": "",
            "duration": 100,
            "classification": "Do It First"
        },
        {
            "id": 2,
            "name": "Apresentar planos",
            "description": "",
            "duration": 100,
            "classification": "Do It First"
        },
        {
            "id": 3,
            "name": "Finalização",
            "description": "",
            "duration": 100,
            "classification": "Do It First"
        }
    ]
]
```
