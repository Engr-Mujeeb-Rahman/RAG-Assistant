# Akbar RAG Assistant

**Akbar RAG Assistant** is a Document-based Question Answering AI system.  
It allows users to ask questions from text documents and get accurate answers using **Retrieval-Augmented Generation (RAG)**.

---

## Features

- Ask questions from any text document (`data.txt`)  
- Uses **LangChain** for building the RAG pipeline  
- Uses **HuggingFace embeddings** (`all-MiniLM-L6-v2`) and **FAISS** vector store  
- Powered by **Google Gemini LLM** (`gemini-2.5-flash`)  
- **Streamlit frontend** with styled sidebar, buttons, and background  
- Secure API key handling using `.env`  

---

## Project Structure

RAG_Project/<br>
├── backend.py # RAG pipeline code<br>
├── frontend.py # Streamlit frontend<br>
├── background.jpg # Background image for app<br>
├── logo2.png # Logo image for sidebar<br>
├── data.txt # Document to query<br>

---


---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Akbar-RAG-Assistant.git
cd Akbar-RAG-Assistant

2. Create a virtual environment (recommended):

```bash
python -m venv myenv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3. Install dependencies:

```bash
pip install -r requirements.txt

4. Create a .env file in the project root:

```bash
GOOGLE_API_KEY=your_google_gemini_api_key

5. Run the Streamlit app:

```bash
streamlit run frontend.py
