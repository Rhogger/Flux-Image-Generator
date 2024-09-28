# Flux Image Generator

## Descrição

Este componente gera uma imagem a partir de um texto fornecido e retorna a url da imagem. Ele utiliza o modelo do Flux.dev para a geração de imagens.

## Pré-requisitos

- Possuir uma conta no fal.ai.
- Possuir uma API-KEY no fal.ai.

<br>

## Entradas

| Nome | Tipo | Descrição | Obrigatório |
|------|------|-----------|-------------|
| prompt | String | Texto que será utilizado para gerar a imagem. | Sim |
| api-key | String | Chave de Api gerada pelo fal.ai | Sim |

<br>

## Saídas

| Nome | Tipo | Descrição |
|------|------|-----------|
| image_url | String | Link da imagem gerada. |

