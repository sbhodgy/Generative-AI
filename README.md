# Generative AI

## Overview

This repository focuses on Generative AI, exploring concepts, techniques, and tools used to create AI models capable of generating content. It includes resources, code examples, and experiments related to text, image, and other generative tasks. The goal is to provide a foundation for understanding and building generative AI systems.

### Creating a Virtual Environment and Installing Dependencies

1. **Create a Virtual Environment**:
    ```bash
    py -3.12 -m venv .venv
    ```

2. **Activate the Virtual Environment**:
      ```bash
      .venv\Scripts\activate
      ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Launching Simple LLM Application

LangServe helps developers deploy LangChain chains as a REST API. To launch the example app, run the following command in the terminal:

```bash 
python serve_simple_llm.py
```
To access an interactive playground:

```http://localhost:8000/chain/playground```




