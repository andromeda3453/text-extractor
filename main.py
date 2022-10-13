from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import shutil
from extractor import extract

app = FastAPI()
my_path = "/Users/Sikandar/Documents/Python/text-extractor"


# #path parameters
# @app.get('/home/{id}')
# def home(id:int):
#     return {"Data": id}

# #query parameters
# @app.get('/get-name')
# def home(name:str):
#     return name

@app.get('/file')
def file():
    file_path = os.path.join(my_path, "ANTI HCV.pdf")
    if os.path.exists(file_path):
        return FileResponse(file_path)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    result = ""
    if file.content_type == "application/pdf":
        path_to_file = os.path.join(os.getcwd(), file.filename)
        try:
            with open(path_to_file, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            result = extract(path_to_file)

        finally:
            file.file.close()
    else:
        result = "Please provide a pdf file"

    return {"text": result}



