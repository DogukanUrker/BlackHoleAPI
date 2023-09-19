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


@app.get("/about")
def about():
    return "This list of black holes (and stars considered probable candidates) is organized by mass (including black holes of undetermined mass); some items in this API are galaxies or star clusters that are believed to be organized around a black hole."


@app.get("/whatisablackhole")
def whatIsBlackHole():
    return "A black hole is a region of spacetime where gravity is so strong that nothing, including light or other electromagnetic waves, has enough energy to escape it. The theory of general relativity predicts that a sufficiently compact mass can deform spacetime to form a black hole. The boundary of no escape is called the event horizon. Although it has a great effect on the fate and circumstances of an object crossing it, it has no locally detectable features according to general relativity. In many ways, a black hole acts like an ideal black body, as it reflects no light. Moreover, quantum field theory in curved spacetime predicts that event horizons emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional to its mass. This temperature is of the order of billionths of a kelvin for stellar black holes, making it essentially impossible to observe directly."


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
