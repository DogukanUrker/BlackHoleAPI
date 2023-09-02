import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import data, getSize, getRandomData
from random import choice

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=origins,
    allow_credentials=True,
)


@app.get("/data")
def blackHoles():
    return data()


@app.get("/data/{id}")
def getByID(id):
    for i in data():
        if str(i["id"]) == id:
            return i
    raise HTTPException(status_code=404, detail="Data not found")


@app.get("/getDataSizeKiloBytes")
def getDataSizeKiloBytes():
    return int(getSize() / 1024)


@app.get("/getDataSizeBytes")
def getDataSizeBytes():
    return getSize()


@app.get("/random")
def getRandom():
    return getRandomData()


@app.get("/randomName")
def getRandomName():
    return choice(getRandomData()["name"])


@app.get("/randomImage")
def getRandomImage():
    return getRandomData()["image"]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1818, workers=1, reload=True)
