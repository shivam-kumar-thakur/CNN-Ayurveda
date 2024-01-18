import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
import requests
import uvicorn

app = FastAPI()

MODEL1 = tf.keras.models.load_model(r"D:\Ayurveda\models\splitdataset1.h5")
MODEL2 = tf.keras.models.load_model(r"D:\Ayurveda\models\splitdataset2_1.h5")

CLASS_NAMES1 = ['Aloevera', 'Amla Fruit', 'Amruthaballi', 'Ashoka flower', 'Balloon_Vine', 'Betel', 'Bhrami',
               'Bohera', 'Caricature', 'Castor', 'Chakte', 'Coffee', 'Common rue', 'Devilbackbone',
               'Fenugreek seed', 'Haritoki', 'Nayontara', 'Neem', 'Pathorkuchi', 'Pipal', 'Thankuni', 'Tulsi',
               'Zenora', 'turmeric']

CLASS_NAMES2 = ['Amla Leaves', 'Ashwagandha', 'Astma_weed', 'Badipala', 'Bringaraja', 'Giloy', 'ashoka leaves',
                'citron lime fruit']

plants_with_similar_properties = {}  # Define your dictionaries here
identification = {}
toxicity = {}
varied_names = {}
season = {}
herbal_uses = {}

def read_file_as_resized_image(data, target_size=(256, 256)) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize(target_size)  # Resize the image to the target size
    image = np.array(image)
    return image

def mod1(model, image, class_names):
    img_batch = np.expand_dims(image, 0)
    predictions = model.predict(img_batch)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    return [predicted_class, confidence]

@app.get("/ping")
async def ping():
    return "hello"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(image_url: str):
    try:
        # Download image from the URL
        response = requests.get(image_url)
        image = read_file_as_resized_image(response.content)

        # Resize the image to the target size before making predictions
        target_size = (256, 256)
        image = Image.fromarray(image)
        image = image.resize(target_size)
        image = np.array(image)

        # Choose the appropriate model and class names based on your requirements
        predict1 = mod1(MODEL1, image, CLASS_NAMES1)
        predict2 = mod1(MODEL2, image, CLASS_NAMES2)

        return {
            "class1": predict1[0],
            "confidence1": predict1[1],
            "class2": predict2[0],
            "confidence2": predict2[1],
        }
    except Exception as e:
        return JSONResponse(content={"error": str("Error processing the image.")}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
