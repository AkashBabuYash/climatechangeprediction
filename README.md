# ClimateSense AI 🌡️


## 🚀 Overview

**ClimateSense AI** is a full-stack web application that combines **Machine Learning** for temperature prediction and **Generative AI** for climate-related conversations. 

**Key Features:**
- 🔥 **Temperature Prediction**: Predict daily mean temperature using weather parameters (Random Forest model trained on historical data)
- 💬 **AI Chatbot**: Interactive chatbot powered by Llama-3.1-8B (HuggingFace) for climate/weather queries
- 📱 **Modern React UI**: Responsive design with prediction forms, use-case showcases, and persistent chatbot
- ⚡ **Real-time APIs**: FastAPI backends for ML predictions and LLM responses
- 🎯 **Production-ready**: CORS-enabled, model metrics, Gradio demo included

## ✨ Features

- **ML Model**: RandomForestRegressor (R², MAE, RMSE metrics displayed)
  - Inputs: Year, Month, Day, Humidity, Wind Speed, Mean Pressure, Rainfall
  - Output: Predicted Mean Temperature (°C)
- **AI Chatbot**: LangChain + Llama-3.1-8B for natural conversations about climate
- **Interactive UI**: 
  - Home: Prediction form with popup results
  - Application: Real-world use cases (Agriculture, Disaster Management, Smart Cities, etc.)
  - Persistent floating chatbot
- **Demo UIs**: Gradio interface for ML model testing

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React 19+, React Router, CSS Modules |
| **Backend (ML)** | FastAPI, scikit-learn, pandas, Gradio |
| **Backend (AI)** | FastAPI, LangChain, HuggingFace Transformers |
| **ML Model** | RandomForestRegressor (500 estimators) |

| **Dataset** | Historical weather data (`train.csv`) |

## 📁 Project Structure

```
pdproject/
├── backend/          # ML Prediction API (port 8000)
│   ├── app.py
│   └── train.csv
├── agent/            # AI Chatbot API (port 8001)
│   └── agent.py
├── fronted/          # React Frontend (port 3000)
│   ├── src/
│   │   └── components/
│   └── package.json
├── README.md
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **HuggingFace Account** (for Llama model access → get API token)

### 1. Clone & Setup

```bash
# Project already cloned at: c:/Users/Shyam Babu/OneDrive/Desktop/pdproject
cd "c:/Users/Shyam Babu/OneDrive/Desktop/pdproject"
```

### 2. Backend - ML Prediction Server

```bash
cd backend
# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn scikit-learn pandas numpy gradio

# Run server (port 8000)
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

**Test:** `curl http://localhost:8000/` → Model metrics

### 3. Agent - AI Chatbot Server

**Terminal 2:**
```bash
cd agent
# Reuse backend venv or create new
pip install fastapi uvicorn langchain-huggingface huggingface_hub

# Set HF token (get from https://huggingface.co/settings/tokens)
set HUGGINGFACEHUB_API_TOKEN=your_token_here

# Run server (port 8001)
uvicorn agent:app --host 0.0.0.0 --port 8001 --reload
```

### 4. Frontend - React App

**Terminal 3:**
```bash
cd fronted
npm install
npm start
```

**Open:** http://localhost:3000

## 🔗 API Endpoints

### ML Backend (`http://localhost:8000`)
- `GET /` → Model stats (R², MAE, RMSE)
- `POST /predict` 
  ```json
  {
    "year": 2024, "month": 7, "day": 15,
    "humidity": 65.5, "wind_speed": 12.3,
    "meanpressure": 1015.2, "rainfall": 5.1
  }
  ```
  → `{"predicted_temperature": 23.45}`

### AI Backend (`http://localhost:8001`)
- `GET /` → \"Climate AI Chatbot API running\"
- `POST /chat`
  ```json
  {"question": "What causes global warming?"}
  ```
  → `{"answer": "Detailed response..."}`

## 🖼️ Screenshots

<!-- Add screenshots here -->
1. **Home - Prediction Form**
2. **Prediction Result Popup**
3. **AI Chatbot Interface**
4. **Applications Page**
5. **Gradio ML Demo** (run `python backend/app.py` standalone)

## 📈 Model Performance

- **R² Score**: ~0.95+ (high accuracy)
- **MAE**: Low error margin
- **RMSE**: Excellent prediction quality

## 🔒 Environment Variables

```
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

## 🤝 Contributing

1. Fork the repo
2. Create feature branch
3. Submit PR

## 📄 License

MIT License - see [LICENSE](LICENSE) (create if needed)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [HuggingFace](https://huggingface.co/)
- [scikit-learn](https://scikit-learn.org/)

---

⭐ **Star this repo if you found it useful!**

