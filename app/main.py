from datetime import datetime
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pandas import read_csv

from app.utils import get_metrics, get_about_model, get_prediction

templates = Jinja2Templates(directory="app/templates")
app = FastAPI()


@app.get("/")
def home_redirect() -> RedirectResponse:
    return RedirectResponse(url="/home/")


@app.get("/home/")
async def home(request: Request) -> HTMLResponse:
    metrics = await get_metrics()
    about_model = await get_about_model()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"metrics": metrics, "model_info": about_model},
    )


@app.get("/download/")
def download_template() -> FileResponse:
    return FileResponse(
        path="app/statics/files/template.csv",
        filename="hotel_cancellation_template.csv",
        media_type="applications/octet-strean",
    )


@app.post("/predict/")
async def upload_file(request: Request, file: UploadFile):
    import pandas as pd

    file_name = file.filename
    if not file_name.endswith(".csv"):
        return HTTPException(status_code=406, detail="only can accept csv files")

    UPLOAD_PATH = Path("app/uploads/") / f"{datetime.now()}_{file_name}"
    with open(UPLOAD_PATH, "wb") as upload_file:
        upload_file.write(await file.read())

    df = pd.read_csv(UPLOAD_PATH)
    prediction = get_prediction(df)
    return templates.TemplateResponse(
        request=request, name="predict.html", context={"predictions": prediction}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", port=8000, host="0.0.0.0", reload=True)
