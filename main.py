import uvicorn
from fastapi import FastAPI, HTTPException
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


def data():
    with open("data.json") as f:
        data = json.load(f)
    return data


@app.get("/data")
def blackHoles():
    return data()


@app.get("/data/{id}")
def getByID(id):
    for i in data():
        if str(i["id"]) == id:
            return
    raise HTTPException(status_code=404, detail="Data not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1818, workers=1, reload=True)
