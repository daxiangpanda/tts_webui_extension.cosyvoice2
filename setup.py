import setuptools

setuptools.setup(
    name="tts_webui_extension.cosyvoice",
    packages=setuptools.find_namespace_packages(),
    version="0.1.7",
    author="rsxdalv",
    description="CosyVoice: A TTS solution for fluent and natural speech synthesis.",
    url="https://github.com/rsxdalv/tts_webui_extension.cosyvoice",
    project_urls={},
    scripts=[],
    install_requires=[
        "gradio",
        "cosyvoice @ git+https://github.com/rsxdalv/CosyVoice@main",
        "modelscope>=1.25.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
