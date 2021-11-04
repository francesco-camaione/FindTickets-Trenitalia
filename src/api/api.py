from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="src/templates/")
app.mount(
    "/templates",
    StaticFiles(directory="src/templates"),
    name="templates",
)


@app.get("/", response_class=HTMLResponse)
async def x(request: Request):
    return templates.TemplateResponse('index.html', context=({'request': request}))

