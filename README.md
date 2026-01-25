## 주차별 수행 내역

## #1주차 전처리 과정 및 피드백 반영
1. **Red Filter 추출**: HSV 색 공간을 활용하여 이미지 내 특정 영역(빨간색) 필터링 수행
2. **구조 최적화**: 멘토님 피드백에 따라 `src/`, `data/`, `docs/` 폴더로 리팩토링 진행
3. **환경 격리**: `.gitignore` 설정을 통해 불필요한 파일 관리 제외

## #2주차 과정 설명 [구조 설계 및 3D 변환]
1. **이미지 전처리**: Grayscale 변환 및 시각화용 Depth Map 생성
2. **좌표 변환**: 픽셀 밝기 값을 Z축 데이터로 매핑하여 3D 포인트 클라우드 데이터셋 구축
3. **결과 저장**: Depth Map(`jpg`) 및 3D 좌표셋(`.npy`) 보존

## #3주차 과정 설명 [AI 모델링 및 OpenCV 시각화]

본 프로젝트는 YOLOv8 모델을 활용하여 이미지 내 객체를 탐지하고, OpenCV를 통해 시각화 결과를 도출하는 것을 목적으로 합니다.

### 1. 환경 설정
* **라이브러리**: `ultralytics`, `opencv-python`, `datasets`, `torch`
* **데이터셋**: Hugging Face `Food101` 샘플 이미지 (100장)
* **사전 학습 모델**: `yolov8n.pt` (YOLOv8 Nano 모델)

### 2. 실행 방법 (순서대로)
1. **데이터 준비**: `datasets/` 폴더 내에 이미지들을 `train(70)`, `valid(20)`, `test(10)` 비율로 분할 배치합니다.
2. **모델 학습**: 최상위 폴더에서 아래 명령어를 실행하여 학습을 진행합니다.
   ```bash
   python AI-model_OpenCV/src/train_model.py
3. **결과 확인**: 학습이 끝나면 bash에서 경로를 확인하고 best.pt 파일을 찾아 아래 명령어를 실행합니다.
   ```bash
   python AI-model_OpenCV/src/detect.py