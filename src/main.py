import gradio as gr
from models.groq_client.chat import ChatAI


def main() -> None:
    ui = gr.ChatInterface(
        fn=ChatAI,
        title="SlaveBot",
        description="I am servant AI bot of Lord Moiz. All hail Moiz. Banzai",
        # type="messages"
    )

    try:
        ui.launch(share=False)
    finally:
        ui.close()


if __name__ == "__main__":
    main()
else:
    print("Error")
