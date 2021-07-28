import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어있지 않아서 numpy

# 이미지 로드 기본툴
# 이미지 흐리게 하기(Blur 블러)
## 선명하게
org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # 흑백처리
blur = cv2.blur(dst, (5, 5))              # 2,2 보다 5, 5이 훨씬 흐릿해짐
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # 이미지 선명하게 바꿔줌
sharp = cv2.filter2D(dst, -1, kernel)


cv2.imshow('Original', dst) # 이미지를 새 창에 띄우기
cv2.imshow('Blur', blur)    # 흐리게 변경한 이미지 띄우기
cv2.imshow('Sharp', sharp)  # 선명한 이미지 띄우기

cv2.waitKey(0)  # 창에서 키입력 대기
cv2.destoryAllWindows() # 메모리 해제

