from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="src/templates/")
app.mount(
    "/templates",
    StaticFiles(directory="src/templates"),
    name="templates",
)


@app.get("/", response_class=HTMLResponse)
def x(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})
