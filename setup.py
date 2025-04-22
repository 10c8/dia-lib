from setuptools import Command, find_packages, setup

_deps = [
    "descript-audio-codec>=1.0.0",
    "huggingface-hub>=0.30.2",
    "numpy>=2.2.4",
    "pydantic>=2.11.3",
    "soundfile>=0.13.1",
    "torch>=2.6.0",
    "torchaudio>=2.6.0",
]

setup(
    name="dia",
    version="0.0.1",
    author="Nari Labs",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    keywords="",
    license="",
    url="https://github.com/nari-labs/dia",
    package_dir={"": "src"},
    packages=find_packages("src"),
    zip_safe=True,
    python_requires=">=3.11",
    install_requires=_deps,
    classifiers=[],
)
