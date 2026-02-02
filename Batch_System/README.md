# 이미지 배치 프로세싱

# 실행 방법
1. `pip install -r requirements.txt` 실행
2. `input/` 폴더에 분석할 이미지 넣기
3. `python src/batch_process.py` 실행

# 결과 확인
- `output/` : 분석된 이미지가 저장되고 직사각형 모양으로 객체가 탐지됩니다.
- `reports/` : CSV 결과 보고서 저장됩니다.

현재는 시스템의 안정성과 로직의 무결성을 검증하기 위해, 로컬 환경에서 엄선된 테스트셋을 직접 입력(Manual Input)하는 방식을 채택했습니다. 
향후 Roboflow API나 다른 스토리지 등과 연계하여 데이터셋을 가져오는 것부터 AI가 분석하고 결과를 내는 것까지 자동화할 계획입니다.