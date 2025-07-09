## 📖 Azure PDF Summarizer using RAG (Lab 10)

This project demonstrates a Retrieval-Augmented Generation (RAG) application using **Azure OpenAI**, **Azure Cognitive Search**, and **LangChain**. It allows users to upload PDF documents, index their content into Azure Cognitive Search, and ask natural language questions to retrieve context-aware answers.

---

### ✅ Features

* Upload and chunk PDF documents
* Index content into **Azure Cognitive Search**
* Use **Azure OpenAI (gpt-35-turbo)** to generate responses
* Supports multiple user queries for testing

---

### 🛠 Technologies Used

* Python 3.12
* Azure Cognitive Search
* Azure OpenAI Service
* LangChain
* Azure SDK for Python
* VS Code / nano (for development)

---

### 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd azure_lab_10
   ```

2. Create virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   pip install -r requirements.txt
   ```

3. Set environment variables in `.env` file:

   ```
   COGNITIVE_SEARCH_ENDPOINT=<your-search-endpoint>
   COGNITIVE_SEARCH_KEY=<your-search-key>
   AZURE_OPENAI_ENDPOINT=<your-openai-endpoint>
   AZURE_OPENAI_API_KEY=<your-openai-key>
   AZURE_OPENAI_DEPLOYMENT=<your-llm-deployment-name>
   INDEX_NAME=azure-rag-demo-index
   ```

4. Run the app:

   ```bash
   python app.py
   ```

---

### 🔍 Testing

Run the app and input at least 2–3 questions like:

* What are the challenges of deep learning in big data analytics?
* How does domain adaptation work in deep learning?
* What are the advantages of hierarchical learning?

---

### 📦 Folder Structure

```
azure_lab_10/
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

### 👨‍💻 Author

* **Akshay Malik**
* CST8921 Cloud Industry Trends – Lab 10
* Algonquin College

