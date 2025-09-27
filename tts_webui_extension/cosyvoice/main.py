import gradio as gr


def extension__tts_generation_webui():
    cosyvoice_ui()
    return {
        "package_name": "tts_webui_extension.cosyvoice",
        "name": "CosyVoice [Unstable]",
        "requirements": "git+https://github.com/rsxdalv/tts_webui_extension.cosyvoice@main",
        "description": "CosyVoice: High-quality text-to-speech synthesis.",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "rsxdalv",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/FunAudioLLM/CosyVoice",
        "extension_website": "https://github.com/rsxdalv/tts_webui_extension.cosyvoice",
        "extension_platform_version": "0.0.1",
    }


def cosyvoice_ui():
    from .gradio_app import ui_core

    ui_core()


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        extension__tts_generation_webui()
    demo.launch(
        server_port=7770,
    )
