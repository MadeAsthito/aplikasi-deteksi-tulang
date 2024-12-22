# LIBRARY
from ultralytics import YOLO
from PIL import Image
from dotenv import load_dotenv
from cloudinary.utils import cloudinary_url
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import cloudinary
import cloudinary.uploader
import sys
import os


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FUNCTION
def load_model(path):
    model = YOLO(path)
    return model

def load_image(path):
    image = Image.open(path)
    return image

def load_image_bytes(image_bytes):
    image = Image.open(BytesIO(image_bytes))
    return image

def upload_image(image):
    load_dotenv()

    cloudinary.config( 
        cloud_name = os.getenv('CLOUD_NAME'), 
        api_key = os.getenv('API_KEY'), 
        api_secret = os.getenv('API_SECRET'),
        secure=True
    )
    result_upload = cloudinary.uploader.upload(image)
    return result_upload['secure_url']

# MAIN
def detect_fracture(image: Image):
    MODEL_PATH = "./model.pt"
    OUTPUT_PATH = "./output.jpg"

    # LOAD MODEL
    model = load_model(MODEL_PATH)

    if model is None:
        return {
            "status": "error", 
            "message": "Model not found!"
        }
    
    results = model.predict(source=image) 

    for result in results:
        result.save(filename="output.jpg")

        url = upload_image(OUTPUT_PATH)
    
    return {
        "status": "success", 
        "message": "Detection is successfull", 
        "data": {
            "image_url" : url
        }
    }
    
@app.get("/")
def get_index():
    return {
        "status": "success", 
        "message": "Server is working"
    }

@app.post("/detect/fracture")
async def post_fracture(image: UploadFile = File(...)):
    image_bytes = await image.read()

    input_image = load_image_bytes(image_bytes)

    result = detect_fracture(input_image)

    return result