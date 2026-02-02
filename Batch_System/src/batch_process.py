import os
import csv
import cv2
from ultralytics import YOLO

# 기본 폴더 구조
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 폴더 없다면 자동 생성
for folder in [INPUT_DIR, OUTPUT_DIR, REPORT_DIR]:
    os.makedirs(folder, exist_ok=True)

def start_batch():
    # 1. 모델 준비
    model = YOLO("yolov8n.pt") 
    results_list = []
    
    # 2. 사진들 가져오기
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not files:
        print(f"[{INPUT_DIR}] 사진이 발견되지 않았습니다.")
        return

    print(f"{len(files)}장 분석을 시작합니다. ")

    for name in files:
        path = os.path.join(INPUT_DIR, name)
        img = cv2.imread(path)
        
        # 3. AI로 사물 찾기
        prediction = model(img, conf=0.25)
        found_stuff = []
        
        for res in prediction:
            # 상자 그린 이미지 저장 준비
            labeled_img = res.plot()
            for box in res.boxes:
                name_tag = res.names[int(box.cls[0])]
                score = float(box.conf[0])
                found_stuff.append(f"{name_tag}({score:.2f})")
        
        # 4. 결과물 사진 저장
        out_path = os.path.join(OUTPUT_DIR, f"result_{name}")
        cv2.imwrite(out_path, labeled_img)
        
        # 5. 데이터 쌓기
        results_list.append({
            "파일명": name,
            "찾은물건": ", ".join(found_stuff),
            "개수": len(found_stuff)
        })
        print(f"성공: {name} 처리 완료")

    # 6. 배치 결과 저장
    csv_path = os.path.join(REPORT_DIR, "final_report.csv")
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=["파일명", "발견된 객체", "수"])
        writer.writeheader()
        writer.writerows(results_list)

    print(f"\n 작업 종료, output, reports 폴더를 확인해 주세요.")

if __name__ == "__main__":
    start_batch()