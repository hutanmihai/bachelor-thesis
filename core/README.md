# Bachelor's Thesis

## Author

- Hutan Mihai Alexandru
- Github: [hutanmihai](https://github.com/hutanmihai)
- LinkedIn: [Mihai-Alexandru Hutan](https://www.linkedin.com/in/hutanmihai/)
- Portfolio: [mihaihutan.ro](https://mihaihutan.ro)

## How to run the project

### 1. Install required libraries using conda and pip

This is the recommended way of installing the required libraries.
You can also not use conda and install the libraries using pip, but you will have to make sure that you have the correct
version of python installed (3.11.5).

- Create environment

```bash
conda create --name core python=3.11.8
conda activate thesis
```

- Install the required libraries

```bash
pip install jupyter==1.0.0 numpy==1.26.4 matplotlib==3.8.3 opencv-python==4.9.0.80 pandas==2.2.1 pillow==10.2.0 black==24.2.0 seaborn missigno
```

- Install pytorch

```bash
# If you have a CUDA enabled GPU (Windows)
pip install torch==2.2.1+cu121 torchvision==0.17.1+cu121 --index-url https://download.pytorch.org/whl/cu121

# If you have a CUDA enabled GPU (Linux)
pip install torch==2.2.1+cu121 torchvision==0.17.1+cu121

# If you have MacOS (CPU) / Windows (CPU)
pip install torch==2.2.1 torchvision==0.17.1
```

### 2. Set the PYTHONPATH

Make sure you are in the root directory of the project.

- Windows - Powershell:

```bash
$env:PYTHONPATH='.'
```

- Windows - CMD:

```bash
set PYTHONPATH=.
```

- Linux / MacOS:

```bash
export PYTHONPATH=.
```
