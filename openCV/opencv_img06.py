import cv2
import numpy as np
from numpy.core.fromnumeric import shape

# 이미지 로드 기본 툴
org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절

gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

#cv2.imshow('Origin', dst) # v2 새창알림
cv2.imshow('Gray', gray)
cv2.imshow('Noise', enhanced) 

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제