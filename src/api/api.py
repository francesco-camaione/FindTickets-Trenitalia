import grequests
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from script.script import calendar_bestprices
from service import trains_of_day_x
from service.train_service import availabl_trains


app = FastAPI()
templates = Jinja2Templates(directory="src/html/")
app.mount("/html", StaticFiles(directory="src/html"), name="html")
app.mount("/img", StaticFiles(directory="src/img"), name="img")
app.mount("/js", StaticFiles(directory="src/js"), name="js")
app.mount("/css", StaticFiles(directory="src/css"), name="css")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


@app.post("/")
def prices(origin: str, destination: str, month: int, year: int, n_adult: int, n_baby: int, atime):
    date = f"01/{month}/{year}"
    calend_prices = calendar_bestprices(availabl_trains(origin.strip(), destination.strip(), date, n_adult, n_baby, atime))
    json = jsonable_encoder(calend_prices)
    return JSONResponse(content=json)


@app.post("/trains")
def trains(origin, destination, day, month, year, n_adult, n_baby):
    trains_per_day = trains_of_day_x.Tr_Dayx(origin, destination, day, month, year, n_adult, n_baby).get_data()
    return trains_per_day
