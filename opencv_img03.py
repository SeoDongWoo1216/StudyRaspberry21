import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어있지 않아서 numpy

org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # 흑백처리

h,w,c = dst.shape

cropped = gray[:, :int(w/2)]  # 이미지 넓이 반 줄이기
#cropped = gray[:int(w/2), :]  # 이미지 높이 반 줄이기

cv2.imshow('Original', dst) # 이미지를 새 창에 띄우기
cv2.imshow('Cropped', cropped)  # 반으로 자른 이미지

cv2.waitKey(0)  # 창에서 키입력 대기
cv2.destoryAllWindows() # 메모리 해제

