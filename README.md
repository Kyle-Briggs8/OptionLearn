# OptionLearn

![OptionLearn demo](docs/demo.gif)

**OptionLearn** is a hands-on sandbox for exploring equity **options**: tweak parameters, see prices/greeks update live, and run the whole thing in a one-click Docker container.

> ⚠️ Educational purposes only — nothing here is financial advice.

---

## ✨ What’s inside

| Folder/File        | Purpose                                   |
|--------------------|-------------------------------------------|
| `option_price/`    | Core pricing logic (e.g., Black-Scholes)  |
| `streamlit_app.py` | Streamlit UI entry point                  |
| `Dockerfile`       | Containerize the app                      |
| `requirements.txt` | Reproducible Python deps                  |
| `test.py`          | Tiny CLI sanity check                     |
| `docs/demo.gif`    | The GIF demo                              |

---

## 🚀 Quickstart

### 1 · Run locally (Python)

```bash
git clone https://github.com/Kyle-Briggs8/OptionLearn.git
cd OptionLearn

# optional virtualenv
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Run with Docker

```bash 
docker build -t name . 
docker run -p 8501:8501 name 
```

## 🧮 What the app does

- **Inputs:** underlying price, strike, risk-free rate, volatility, time to expiry  
- **Outputs:** European call/put price (and optional greeks)  
- **UI:** Streamlit sliders + dynamic charts