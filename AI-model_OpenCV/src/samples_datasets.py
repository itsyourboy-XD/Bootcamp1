import os
from datasets import load_dataset
# 3차 업무용 사진 다운로드
ds = load_dataset("ethz/food101", split='train', streaming=True)
base_path = "datasets" # 요청서 기준 폴더명

for split in ['train', 'valid']:
    os.makedirs(f"{base_path}/{split}/images", exist_ok=True)

print("데이터 확보 중...")
for i, example in enumerate(ds):
    example['image'].convert("RGB").save(f"{base_path}/train/images/food_{i}.jpg")
    if i >= 99: break
print("데이터 준비 완료!")