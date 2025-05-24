import requests
import gradio as gr

# DEEPSEEK API URL 
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_content(topic, keywords, tone="Professional"):
    prompt = f"Write a blog post about '{topic}' in a {tone} tone.\n\n" \
             f"Include the following keywords: {keywords}.\n\n" \
             f"Ensure the content is well-structured with an introduction, main section, and a conclusion."
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No content generated.")
    else:
        return f"Error: {response.text}"

# Gradio interface
interface = gr.Interface(
    fn=generate_content,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Keywords (Comma-separated)"),
        gr.Radio(["Professional", "Casual", "Persuasive"], label="Tone"),
    ],
    outputs=gr.Textbox(label="Generated Content"),
    title="AI Powered Content Writer",
    description="Enter a topic, keywords and tone, and AI will generate a blog post or marketing content"
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()

