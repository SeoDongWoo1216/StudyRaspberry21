import cv2
import numpy as np
from numpy.core.fromnumeric import shape

# 이미지 로드 기본 툴
org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) #color or 흑백 및 사이즈 조전 
dst = cv2.resize(org, dsize=(480, 320)) # 이미지가 너무 커서 사이즈 조절

h, w, c = dst.shape
noise = np.uint8(np.random.normal(loc=0, scale=80, size=[h, w, c]))
noised_img = cv2.add(dst, noise) # 원본 이미지에 노이즈 추가

cv2.imshow('Origin', dst) #cv2 새창알림
cv2.imshow('Noise', noised_img)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제