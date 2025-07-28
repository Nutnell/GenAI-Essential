# Environment Setup

## Create an environment

```bash
conda create --name project1 python=3.13.5 -y
```

## Activate the environment

```bash
conda activate project1
```

## Install the requirements

```bash
conda install -c conda-forge pandas
```

```bash
pip install -r requirements.txt
```

## jupyter notebook necessities

If you get a missing module error trying to run jupyter, try 
```bash
conda install -c conda-forge ipykernel
```

## Install jupyterlab

```bash
conda install -c conda-forge jupyterlab
```

## Install jupyterlab extensions

```bash
conda install -c conda-forge jupyterlab-git
```

```bash
conda install -c conda-forge catppuccin-jupyterlab
```

## Run jupyterlab

```bash
jupyter lab --no-browser --allow-root --ip 0.0.0.0
```

## For working with AWS Bedrock

```bash
pip install boto3
```

## Requirements for Hugging Face

```bash
conda install -c conda-forge sentencepiece
```

```bash
pip install sacremoses
```

```bash
pip install hf_xet
```

## Llamafile
After downloading the file, add .exe to the end before working with it on windows.

## Llama.cpp

```bash
pip install llama-cpp-python
```

```bash
winget install llama.cpp
```

Download a model via:
https://huggingface.co/lmstudio-community/Llama-3.2-1B-Instruct-GGUF/tree/main

Then run in terminal:

```bash
llama-cli --hf-repo lmstudio-community/Llama-3.2-1B-Instruct-GGUF \
--hf-file Llama-3.2-1B-Instruct-Q3_K_L.gguf \
-p "You are a helpful assistant" -cnv
```

## Running linktree-clone

```bash
go mod init genai-essential
```

```bash
cd github-copilot\linktree-clone
```

```bash
go mod download github.com/gin-gonic/gin
go mod download github.com/joho/godotenv
go mod download gorm.io/driver/sqlite
go mod download gorm.io/gorm
```

```bash
go mod tidy
```

```bash
go build -o linktree-clone
```

```bash
set CGO_ENABLED=1
```

```bash
go run main.go
```