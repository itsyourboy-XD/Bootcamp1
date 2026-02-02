import os
from datasets import load_dataset

# 현재 파일 위치 기준 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(BASE_DIR, "..", "datasets")

# 필요한 폴더 생성
for split in ['train', 'valid', 'test']:
    os.makedirs(os.path.join(base_path, split, "images"), exist_ok=True)

print("Starting Download from Hugging Face...")

try:
    # 스트리밍 모드로 데이터 로드
    ds = load_dataset("ethz/food101", split='train', streaming=True)
    
    for i, example in enumerate(ds):
        img = example['image'].convert("RGB")
        
        # 80(Train) : 10(Valid) : 10(Test) 분할
        if i < 80:
            target = "train"
        elif i < 90:
            target = "valid"
        else:
            target = "test"
            
        save_path = os.path.join(base_path, target, "images", f"food_{i}.jpg")
        img.save(save_path)
        
        if (i + 1) % 20 == 0:
            print(f"Progress: {i + 1}/100 images saved.")
            
        if i >= 99: break

    print("Success: Dataset preparation (80:10:10) is complete.")

except Exception as e:
    print(f"Error during download: {e}")