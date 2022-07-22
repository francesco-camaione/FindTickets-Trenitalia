import grequests
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from main.main import calendar_bestprices
from service import trains_of_day_x
from service.train_service import availabl_trains
from utils import utils

app = FastAPI()
templates = Jinja2Templates(directory="resources/html/")
app.mount("/html", StaticFiles(directory="resources/html"), name="html")
app.mount("/img", StaticFiles(directory="resources/img"), name="img")
app.mount("/js", StaticFiles(directory="resources/js"), name="js")
app.mount("/css", StaticFiles(directory="resources/css"), name="css")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


@app.get("/get-calendar")
def prices(origin: str, destination: str, month: int, year: int, n_adult: int, n_baby: int, atime, frecce: str):
    date = f"01/{month}/{year}"
    response = availabl_trains(
        origin.strip(), destination.strip(), date, n_adult, n_baby, atime, frecce)
    calend_prices = calendar_bestprices(response)
    json = jsonable_encoder(calend_prices)
    return JSONResponse(content=json)


@app.get("/trains")
def trains(origin, destination, day, month, year, n_adult, n_baby, atime, frecce):
    trains_per_day = trains_of_day_x.Tr_Dayx(
        origin, destination, day, month, year, n_adult, n_baby, atime, frecce).get_data()
    return trains_per_day


@app.get("/stations")
def stations(letter: str):
    res = utils.stations(letter)
    return res
