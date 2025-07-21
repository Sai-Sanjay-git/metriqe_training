import gradio as gr
from vector_store_manager import get_pdf_list


def setup_gradio_ui():
    """sets up the launch of gradio web interface"""

    with gr.Blocks(title= "ask my pdf invoices")as app:
        gr.Markdown("# ASk question on pdf invoices")

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 1. manage the documents")
                file_uploader = gr.File(label="upload PDFs", file_count="multiple", file_types=[".pdf"])

                process_button = gr.Button("add the knowledgement", variant="primary")

                gr.Markdown("### 2. Current documents")
                pdf_list_dropdown = gr.Dropdown(label="select PDF to remove",choices= get_pdf_list())
                remove_button = gr.Button("remove from Knowlegdebase",variant="stop")
                clear_button = gr.Button("clear all data",variant="stop")

                processing_status = gr.Markdown("status: Ready for uploading the PDFS")

            with gr.Column(scale = 2):
                gr.Markdown("### 3. ask a question")
                question_input =gr.Text(label="question",placeholder="eg: what is the total invoice account ?")
                ask_button = gr.Button("ask the llm and get answers",variant="primary")

                gr.Markdown("### 4. ask a question")
                answer_output = gr.Markdown("your answer will appear here")
                gr.Markdown("### 5. sources")
                answer_output = gr.Markdown("source douments will appear here")
        app.load (get_pdf_list, outputs = pdf_list_dropdown)
        return app


if __name__ == "__main__":
    app = setup_gradio_ui()
    app.launch(share=True,debug = True)