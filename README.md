# Python AI Chatbot with Azure Integration

## 📌 Project Overview
A sophisticated AI-driven chatbot developed using **Python** and **Azure AI Services**. This project demonstrates the integration of cloud-based Natural Language Processing (NLP) into a local development environment, focusing on secure API management and efficient data flow.

## 🚀 Key Features
* **Azure Integration:** Leverages Azure AI for advanced language understanding and response generation.
* **Environment Security:** Utilizes `.env` files and `python-dotenv` to manage sensitive API keys and endpoints securely.
* **Asynchronous Processing:** Designed to handle real-time user inputs with optimized response times.
* **Error Handling:** Implemented robust try-except blocks to manage API timeouts and connectivity issues.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Cloud Services:** Azure AI Services (Language/OpenAI)
* **Libraries:** `requests`, `python-dotenv`, `json`
* **IDE:** PyCharm / VS Code

## 📁 Project Structure
* `app.py`: The main entry point for the chatbot logic.
* `config.py`: Handles environment variable loading and configuration settings.
* `.env.example`: A template file showing required environment variables (API keys, Endpoints).
* `requirements.txt`: List of dependencies for easy environment replication.

## ⚙️ Setup & Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment Variables:**
    * Create a `.env` file in the root directory.
    * Add your `AZURE_AI_KEY` and `AZURE_AI_ENDPOINT`.
4.  **Run the application:**
    ```bash
    python app.py
    ```

## 📈 Future Enhancements
* [ ] Implement a GUI using Streamlit or Flask.
* [ ] Integrate SQL database logging to track conversation history for sentiment analysis.
* [ ] Expand NLP capabilities to support multi-language translation.

---
Developed by **[Your Name]** as part of a transition into Software Engineering.
