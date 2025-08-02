# 🧠 CodeScan – Source Code Analysis using OpenAI

CodeScan is a Streamlit-based application that analyzes source code from a public GitHub repository using OpenAI models. It indexes the code into a vector database and allows you to ask natural language questions about the code.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CodeScan.git
cd CodeScan
```
### 2. Create and Activate a Virtual Environment
using conda
``` bash
conda create -n codescan-env python=3.10
conda activate codescan-env
```
or using venv:
```bash
python -m venv codescan-env
codescan-env\Scripts\activate      # On Windows
source codescan-env/bin/activate  # On Linux/macOS
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Set up Environment Variable
Create a .env file in the root directory with your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. 🚀 Running the App
Start the Streamlit app:
```bash
streamlit run app.py
```

Once running, you can:
- Enter a public GitHub repository URL.
- Ask questions about the codebase in natural language.
- Get context-aware responses based on code embeddings