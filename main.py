from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/XYZ")
def get_xyz():
    return {
        "name": "daho",
        "city": "fairfax"
    }