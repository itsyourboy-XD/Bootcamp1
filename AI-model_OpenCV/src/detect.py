import cv2
from ultralytics import YOLO
import os

# 1. YOLO 모델 로드
model = YOLO("yolov8n.pt") 

# 2. 이미지 경로 설정 (test 폴더에 실제 있는 파일명 하나만 지정)
# 현재 test 폴더에 있는 이미지 파일명을 확인 후 수정.
image_path = r"C:\Bootcamp1\AI-model_OpenCV\datasets\test\images\food_29.jpg" 

if not os.path.exists(image_path):
    print(f"에러: {image_path} 경로에 사진이 없습니다. 파일명을 확인해주세요!")
else:
    image = cv2.imread(image_path)

    # 3. 객체 탐지 실행 (conf=0.25 옵션으로 적절한 결과 유도)
    # 이미지 속 물체를 찾아 좌표와 이름을 계산합니다.
    results = model(image, conf=0.25)

    # 4. 탐지된 결과가 있는지 확인 후 시각화
    if len(results[0].boxes) == 0:
        print("물체를 찾지 못했습니다. 다른 사진으로 시도해보세요.")
    else:
        for result in results:
            for box in result.boxes:
                # 좌표값 추출 및 정수 변환
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])] # 물체 이름
                conf = box.conf[0]                   # 신뢰도(확률)

                # OpenCV를 이용한 시각화 (초록색 상자와 텍스트)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 5. 결과 화면 출력
    cv2.imshow("YOLO Object Detection", image)
    print("아무 키나 누르면 창이 닫힙니다.")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()