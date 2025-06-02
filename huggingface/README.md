---
title: SS VioletFMU
emoji: 💬
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: apache-2.0
---

SS VioletFMU é um chatbot experimental baseado em Gradio, utilizando dois modelos de linguagem para gerar respostas e um terceiro modelo árbitro para julgar qual resposta é melhor.

### 🧠 Como funciona

1. **Entrada do usuário:** o usuário envia uma pergunta.
2. **Resposta em paralelo:** dois modelos diferentes (Modelo A e Modelo B) geram respostas independentes.
3. **Julgamento:** um terceiro modelo (Modelo Árbitro) avalia as respostas e seleciona a melhor com uma justificativa.

### 🔧 Tecnologias

- [Gradio](https://gradio.app): interface web simples e interativa.
- [Transformers](https://huggingface.co/docs/transformers/index): para carregar e usar modelos pré-treinados.
- [Hugging Face Hub](https://huggingface.co/models): repositório dos modelos usados.

### 🤖 Modelos utilizados

- `tiiuae/falcon-rw-1b`: modelo de geração de texto (Modelo A)
- `google/flan-t5-base`: modelo de geração instruída (Modelo B e Árbitro)

### 🚀 Execute localmente

```bash
git clone https://huggingface.co/spaces/SEU_USUARIO/SS_VioletFMU
cd SS_VioletFMU
pip install -r requirements.txt
python app.py
