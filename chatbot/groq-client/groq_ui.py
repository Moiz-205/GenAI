import gradio as gr
from chat import ChatAI


def main() -> None:
    ui = gr.ChatInterface(
        fn=ChatAI,
        title="Bot",
        description="Bot for bot purposes"
    )

    try:
        ui.launch(share=False)
    finally:
        ui.close()


if __name__ == "__main__":
    main()
else:
    print("Error")
