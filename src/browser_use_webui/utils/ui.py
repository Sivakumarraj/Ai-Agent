"""User interface creation for the WebUI."""

import gradio as gr
from gradio.themes import Base

def create_ui(config):
    """Create the Gradio UI interface."""
    with gr.Blocks(title="Browser Use WebUI", theme=Base()) as demo:
        gr.Markdown(
            """
            # 🌐 Browser Use WebUI
            ### Control your browser with AI assistance
            """
        )
        
        with gr.Tabs():
            with gr.TabItem("Run Agent"):
                task = gr.Textbox(
                    label="Task Description",
                    lines=4,
                    value=config['task'],
                    info="Describe what you want the agent to do",
                )
                run_button = gr.Button("▶️ Run Agent")
                output = gr.Textbox(label="Output")
                
                run_button.click(
                    fn=lambda x: f"Running task: {x}",
                    inputs=task,
                    outputs=output
                )
    
    return demo