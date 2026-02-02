Bootcamp1: AI 모델 학습 및 이미지 처리 통합 프로젝트
# 환경 설정
pip install ultralytics opencv-python datasets torch

# 주차별 수행 내역

# 1주차: Git 활용 및 이미지 처리 실습
# 주요 과제: HSV 색 공간을 활용한 Red Filter 추출
1. Red Filter 추출: HSV 색 공간을 활용하여 이미지 내 특정 영역(빨간색) 필터링 수행
2. 구조 최적화: 멘토님 피드백에 따라 src/, data/, docs/ 폴더로 리팩토링 진행
3. 환경 격리: .gitignore 설정을 통해 불필요한 파일 관리 제외

# 2주차: 3D 데이터 변환 및 매핑
# 주요 과제: 2D 이미지의 밝기 데이터를 활용한 3D 시각화
1. Grayscale 변환을 통한 Depth Map 생성
2. 픽셀 밝기 값을 Z축 데이터로 매핑하여 포인트 클라우드 구축
3. 분석 데이터 보존을 위해 .npy 포맷으로 3D 좌표 데이터셋 저장

# 3주차: AI 모델링 및 객체 탐지 (Inference & Filtering)

데이터셋: Hugging Face Food101 샘플 이미지 (100장)
사전 학습 모델: yolov8n.pt (YOLOv8 Nano 모델)
2. 실행 방법 (순서대로)
데이터 준비: python AI-model_OpenCV/src/samples_datasets.py
모델 학습: 최상위 폴더에서 아래 명령어를 실행하여 학습을 진행합니다.
python AI-model_OpenCV/src/train_model.py
결과 확인: 학습이 끝나면 bash에서 경로를 확인하고 best.pt 파일을 찾아 아래 명령어를 실행합니다.
python AI-model_OpenCV/src/detect.py

# 4주차: 희망하는 제품/SW 선정 및 개발 프로젝트 수행
# 주요 내용: 배치 시스템 구축 및 사람 객체 탐지 실습
1. 수동으로 하나씩 사진을 돌리는 것이 아니라, input/ 폴더에 사진을 넣으면 자동으로 전체를 분석하여 output/으로 결과물을 내보내는 자동화 파이프라인 구축.
프로젝트 구조 확립
- input/: 분석할 원본 사진
- output/: 탐지 결과가 그려진 이미지 저장
- reports/: 학습 및 분석 결과 보고서 보관
- src/: 실행 스크립트 관리
# 사람(Person) 객체 탐지 실습 - 사람 이미지를 활용하여 모델이 인물을 얼마나 정확하게 찾아내는지 테스트하고 분석하고 csv 파일로 결과를 기록함.

# 필수 라이브러리: ultralytics, opencv-python, datasets, torch
# 참고 데이터셋: Hugging Face Food101, Roboflow Hard Hats