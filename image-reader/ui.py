import gradio as gr
from .image import groq_image

def main() -> None:
    css = '''
    #outbox textarea{
        min-height: 240px !important;
        max-height: 75vh !important;
        resize: vertical !important;

        font-size: 15px;
        line-height: 1.5;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;

        padding: 12px 14px;
        box-sizing: border-box;

        background-color: #fafafa;
        border-radius: 8px;
        border: 1px solid #d0d0d0;

        overflow-y: auto;
    }
    '''


    ui = gr.Interface(
        fn=groq_image,
        inputs=[
            gr.Image(type='pil', label='Upload an image of an animal'),
            gr.Textbox(label='Ask a question about the animal',
                       lines=2, placeholder='what about the cat in the image?')
        ],
        outputs=gr.Textbox(
                    label='Answer',
                    lines=8,
                    max_lines=40,
                    # show_copy_button=True,
                    elem_id='outbox'
                    ),
            title='Animal Image Analyzer',
            css=css
    )

    try:
        ui.launch(share=False)
    finally:
        ui.close()

if __name__ == "__main__":
    main()
else:
    print('Error')
