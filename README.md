# Computer Vision Project - Week 2

## Project Overview
이 프로젝트는 OpenCV를 활용하여 2D 이미지를 분석하고, 픽셀 단위의 데이터를 3D 좌표계로 변환하는 과정을 포함합니다. 1차 과제의 피드백을 반영하여 코드의 모듈화(함수화) 및 폴더 구조 최적화를 진행하였습니다.

## Folder Structure
* **src/**: 이미지 전처리 로직 및 단위 테스트 코드 (`image_processing.py`, `image_preprocessing.py` `test_3d_processing.py`)
* **data/**: 실습용 원본 이미지 파일 (`sample.jpg`)

## Key Features
1. **Red Color Filtering**: HSV 색 공간을 활용한 특정 객체 추출
2. **Depth Map Generation**: Grayscale 변환 후 `COLORMAP_JET`을 적용한 가상 깊이 맵 생성
3. **3D Point Cloud Conversion (Advanced)**: 픽셀의 밝기 값을 Z축(Depth)으로 활용하여 (X, Y, Z) 좌표 데이터 생성
4. **Unit Testing**: `pytest`를 통한 이미지 처리 함수의 안정성 검증 (Input 예외 처리 등)

##  How to Run
### 1. Requirements
```bash
pip install numpy opencv-python pytest