import gradio as gradio

from utils import generate_response

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label='Openai Chatbot')
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(generate_response, [msg, chatbot],[msg, chatbot])

demo.lauch