import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import data, getSize, getRandomData


app = FastAPI(
    title="BlackHolesAPI",
    version="1.0.0",
    contact={
        "name": "Dogukan Urker",
        "url": "https://dogukanurker.com",
        "email": "dogukanurker@icloud.com",
    },
)

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
        match str(i["id"]) == id:
            case True:
                return [i]
    raise HTTPException(status_code=404, detail="Data not found.")


@app.get("/getDataSizeKiloBytes")
def getDataSizeKiloBytes():
    return int(getSize() / 1024)


@app.get("/getDataSizeBytes")
def getDataSizeBytes():
    return getSize()


@app.get("/random")
def getRandom():
    return [getRandomData()]


@app.get("/randomValue/{value}")
def getRandomValue(value: str):
    match value in getRandomData():
        case True:
            return getRandomData()[value]
    raise HTTPException(status_code=404, detail="Data not found.")


@app.get("/getValueByID/{value}/{id}")
def getValueByID(value, id: int):
    id -= 1
    match len(data()) > id:
        case True:
            match value in data()[id]:
                case True:
                    return data()[id][value]
    raise HTTPException(status_code=404, detail="Data not found.")


@app.get("/getRandomDatas/{dataCount}")
def getRandomDatas(dataCount: int):
    match len(data()) > dataCount:
        case True:
            output = []
            for _ in range(dataCount):
                output.append(getRandomData())
            return output
    raise HTTPException(status_code=404, detail="Too much data is requested.")


@app.get("/getAll/{value}")
def getAll(value: str):
    output = []
    for i in data():
        try:
            output.append(i[value])
        except:
            raise HTTPException(status_code=404, detail="Data not found.")
    return output


@app.get("/getAllWithID/{value}")
def getAllWithID(value: str):
    output = []
    for i in data():
        try:
            blackhole = []
            blackhole.append(i["id"])
            blackhole.append(i[value])
            output.append(blackhole)
        except:
            raise HTTPException(status_code=404, detail="Data not found.")
    return output


match __name__ == "__main__":
    case True:
        uvicorn.run("main:app", host="192.168.1.129", port=1818, workers=1, reload=True)
