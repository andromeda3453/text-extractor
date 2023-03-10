from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import shutil
from extractor import extract
import json
from fastapi.middleware.cors import CORSMiddleware
import pikepdfuvi

app = FastAPI()

app.add_middleware(
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    middleware_class=CORSMiddleware
)



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):


    if file.content_type == "application/pdf":
        path_to_file = os.path.join(os.getcwd(), file.filename)
        try:
            
            with open(path_to_file, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            with pikepdf.Pdf.open(path_to_file, allow_overwriting_input=True) as pdf:
                pdf.save(path_to_file)
                
            result = extract(path_to_file)
            os.remove(path_to_file)
                
            
        finally:
            file.file.close()
    else:
        result = "Please provide a pdf file"
    
    print(result)
    return result


