
## 1. 환경 설정 (Environment)
본 프로젝트는 **Python 3.8+** 환경에서 최적화되었으며, 아래 라이브러리 설치가 필수적입니다.
```bash
pip install opencv-python numpy matplotlib ultralytics datasets torch
```

## 2. 주차별 수행 내역 (Weekly Milestone)

### **#1-2주차: 이미지 전처리 및 3D 데이터 매핑**
* **HSV 색 공간 활용**: 특정 영역(Red Filter) 추출 및 이미지 정제 기술 습득
* **Grayscale 변환을 통한 Depth Map 생성**
* **데이터 정량화**: 픽셀 데이터를 Z축 좌표로 변환하여 **.npy 포맷의 3D 포인트 클라우드** 구축
* **구조화**: 프로젝트 이식성 향상을 위해 `src/`, `data/`, `docs/` 폴더 리팩토링 및 `.gitignore` 적용

### **#3주차: AI 모델링 기초 및 데이터 파이프라인**
* **데이터 자동 분할**: Hugging Face Food101 데이터를 **train(80), valid(10), test(10)** 비율로 분할하는 로직 구현
* **상대 경로 최적화**: `os.path`를 활용하여 실행 환경 의존성을 완전히 제거(피드백 반영)
* **추론 필터링**: 사전 학습 모델(`yolov8n.pt`)의 오검출 클래스를 제어하고 특정 객체만 출력하는 커스텀 로직 적용

### **#4주차: 배치 시스템 구축 및 결과 데이터 구조화 (핵심)**
* **Batch Inference 파이프라인**: `input/` 폴더 내 대량 이미지를 일괄 처리하여 `output/`으로 자동 저장하는 시스템 구축
* **결과 리포팅 (CSV)**: 탐지된 객체의 종류, 신뢰도(Confidence), 좌표를 **CSV 형식으로 자동 기록**하여 정량적 분석 기반 마련
* **표준 디렉토리 구조**: `input`, `output`, `reports`, `src`로 이어지는 데이터 흐름 표준화