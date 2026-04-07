# XYZ API (FastAPI sample)

Simple Python backend API that returns sample JSON.

Endpoint:

```
GET /XYZ
```

Response:

```json
{ "name": "daho", "city": "fairfax" }
```

---

## 1. Create project

```bash
mkdir med
cd med
```

---

## 2. Create virtual environment

```bash
python -m venv .venv
```

Activate venv

### Windows PowerShell

```bash
.\.venv\Scripts\Activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
python -m pip install fastapi uvicorn
```

Optional freeze versions:

```bash
pip freeze > requirements.txt
```

---

## 4. Create API file

Create `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/XYZ")
def get_xyz():
    return {
        "name": "daho",
        "city": "fairfax"
    }
```

---

## 5. Run server

```bash
python -m uvicorn main:app --reload
python -m uvicorn main:app --reload --port 3000
```

Server runs at:

```
http://localhost:3000
```

---

## 6. Test API

Open in browser:

```
http://localhost:3000/XYZ
```

Expected result:

```json
{
  "name": "daho",
  "city": "fairfax"
}
```

---

## CLI Quick Start (copy/paste)

```bash
python -m venv .venv
.\.venv\Scripts\Activate
pip install fastapi uvicorn
uvicorn main:app --reload --port 3000
```

---

## Optional: requirements.txt install

```bash
pip install -r requirements.txt
```

---

## Notes

* Port 3000 used to simulate frontend calling API
* Works with Angular, React, or any FE app
* FastAPI auto docs available at:

```
http://localhost:3000/docs
```
