import cv2
from ultralytics import YOLO
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = YOLO("yolov8n.pt") 

# 멘토님이 지정한 3가지 클래스만 필터링
MY_CLASSES = ['apple_pie', 'hamburger', 'pizza']

test_dir = os.path.join(BASE_DIR, "..", "datasets", "test", "images")

if not os.path.exists(test_dir):
    print("Error: 'datasets/test/images' folder not found!")
else:
    image_files = [f for f in os.listdir(test_dir) if f.endswith(".jpg")]
    
    if image_files:
        random_image = random.choice(image_files)
        image_path = os.path.join(test_dir, random_image)
        print(f"Selected Image: {random_image}")

        image = cv2.imread(image_path)
        results = model(image, conf=0.25)

        for result in results:
            for box in result.boxes:
                label = result.names[int(box.cls[0])]
                
                # 사전 학습된 모델의 80개 지식 중 3개만 골라내기
                if label in MY_CLASSES:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, label, (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Detection Result (Filtered)", image)
        print("Closing in 5 seconds or press any key.")
        cv2.waitKey(5000)
        cv2.destroyAllWindows()