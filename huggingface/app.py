import gradio as gr
from transformers import pipeline

# Modelos
modelo_a = pipeline("text-generation", model="tiiuae/falcon-rw-1b")
modelo_b = pipeline("text2text-generation", model="google/flan-t5-base")
modelo_julgamento = pipeline("text2text-generation", model="google/flan-t5-base")

def gerar_resposta(modelo, pergunta):
    try:
        resultado = modelo(pergunta, max_length=100, do_sample=True, top_p=0.9)[0]['generated_text']
        return resultado.strip().replace(pergunta, '').strip()
    except Exception as e:
        return f"[ERRO ao gerar resposta do modelo: {e}]"

def julgar_respostas(pergunta, resposta_a, resposta_b):
    prompt_julgamento = f"""
Considere as duas respostas abaixo para a pergunta do usuário.

Pergunta: {pergunta}

Resposta A: {resposta_a}

Resposta B: {resposta_b}

Qual resposta está mais clara, útil e correta? Responda apenas com "A" ou "B", seguido de uma breve justificativa.
"""
    try:
        julgamento = modelo_julgamento(prompt_julgamento, max_length=100)[0]['generated_text']
        if 'A' in julgamento[:5]:
            vencedora = 'A'
        elif 'B' in julgamento[:5]:
            vencedora = 'B'
        else:
            vencedora = 'Empate/Erro'
        return vencedora, julgamento.strip()
    except Exception as e:
        return "Erro", f"[ERRO ao julgar respostas: {e}]"

def chatbot(pergunta):
    resposta_a = gerar_resposta(modelo_a, pergunta)
    resposta_b = gerar_resposta(modelo_b, pergunta)
    vencedora, justificativa = julgar_respostas(pergunta, resposta_a, resposta_b)

    return f"""🧠 Julgamento do Árbitro:

Resposta A: {resposta_a}

Resposta B: {resposta_b}

➡️ Vencedora: {vencedora}
📝 Justificativa: {justificativa}"""

gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Pergunta do Usuário"),
    outputs=gr.Textbox(label="Resultado do Julgamento"),
    title="Chatbot com Árbitro em Cascata"
).launch()