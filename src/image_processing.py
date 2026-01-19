import cv2
import numpy as np
import os

# generate_depth_map 함수 적용
def generate_depth_map(image):
    if image is None:
        raise ValueError("No input image found.")
    # 그레이스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 가상의 깊이 맵 적용
    depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return depth_map, gray

# 이미지 로드
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "..", "data", "sample.jpg")

    img = cv2.imread(path)
    
    if img is not None:
        # Depth Map 
        result, gray = generate_depth_map(img)
        
        h, w = result.shape[:2]
        X, Y = np.meshgrid(np.arange(w), np.arange(h))
        Z = gray.astype(np.float32) 
        
        # 3D 좌표 생성
        points_3d = np.dstack((X, Y, Z))
        
        # 결과 저장 로직
        # 1. Depth Map 이미지를 파일로 저장 (.jpg)
        save_img_path = os.path.join(current_dir, "..", "data", "depth_result.jpg")
        cv2.imwrite(save_img_path, result)      
        # 2. 3D 좌표 데이터를 Numpy 파일로 저장 (.npy)
        save_npy_path = os.path.join(current_dir, "..", "data", "points_3d.npy")
        np.save(save_npy_path, points_3d)

        print("-" * 30)
        print(f"Image Path: {path}")
        print(f"3D Data Generated! (Shape): {points_3d.shape}")
        print(f"3D Coordinate of the First Pixel (X, Y, Z): {points_3d[0, 0]}")
        print("-" * 30)
        
        # 결과 출력
        cv2.imshow('Original', img)
        cv2.imshow('Depth Map Result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Cannot find the image. Check the path: {os.path.abspath(path)}")