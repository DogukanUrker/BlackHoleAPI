import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
)


@app.get("/blackholes")
def blackHoles():
    with open("data.json") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1818, workers=1, reload=True)
