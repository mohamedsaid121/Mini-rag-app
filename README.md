# Mini-Rag

This is a minimal implementation of the RAG model fro question answering.

## Requirements

- Python 3.8 or later

### Install Python using Miniconda

1) Download and install MiniConda from [here] https://www.anaconda.com/download/success?reg=skipped-miniconda
2) Create new environment using the folllwoing command:
``` bash
   $ conda create -n mini-rag python=3.8
```    
3) Activate the Environment:
``` bash
   $ conda activate mini-rag
```

(Optional) Setup you command line interface for better readability
``` bash
   $ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ 
```

### Installation
Install the required package
``` bash
 $ pip install -r requirements.txt
```

Setup the environment variables
``` bash
 $ cp .env.example .env
```

Set your environment variables in the .env file. Like OPENAI_API_KEY value.