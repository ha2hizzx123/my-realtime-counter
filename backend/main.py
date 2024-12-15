from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요한 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 이미지 폴더 경로
image_folder = "/path/to/frontend/images"

# 카운트 값
count = 0

@app.get("/count")
async def get_count():
    return {"count": count}

@app.post("/count/increment")
async def increment_count():
    global count
    count += 1
    return {"count": count}

@app.post("/count/decrement")
async def decrement_count():
    global count
    count -= 1
    return {"count": count}

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    # 이미지 파일 경로
    image_path = os.path.join(image_folder, image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}
