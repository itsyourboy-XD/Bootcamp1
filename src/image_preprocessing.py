import cv2
import numpy as np
from datasets import load_dataset
import os

ds = load_dataset("ethz/food101", split="train", streaming=True)
images = list(ds.take(5))

os.makedirs('preprocessed_samples', exist_ok=True)

for i, data in enumerate(images):
    # numpy 변환 및 크기 확인
    img_raw = np.array(data['image'])
    h, w = img_raw.shape[:2]

    # 너무 작은 이미지 제거
    if h < 100 or w < 100:
        print(f"너무 작은 이미지 {i+1} 제외")
        continue

    # OpenCV 라이브러리 순서에 맞추어 RGB를 BGR로 변경 후 grayscale
    img = cv2.cvtColor(img_raw, cv2.COLOR_RGB2BGR)
    img_gray_temp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #  너무 어두운 이미지 제거
    if np.mean(img_gray_temp) < 50:
        print(f"어두운 이미지 {i+1} 제외")
        continue
    
    # 224x224 크기 조정
    img_resized = cv2.resize(img, (224, 224))    
    # Grayscale & Normalize
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    img_norm = img_gray / 255.0   
    # 노이즈 제거
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0) 
    # 좌우 반전 및 저장
    img_flip = cv2.flip(img_blur, 1)
    cv2.imwrite(f'preprocessed_samples/sample_{i}.jpg', img_flip)
    print(f"이미지 {i+1} 처리 성공")

print("완료되었습니다.")
