import cv2
import numpy as np
from numpy.core.fromnumeric import shape

# 이미지 로드 기본 툴
## 영상 둘레 표시 컨투어(윤곽)
org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(dst, cont, 0, (0, 255, 0), 2)

cv2.imshow('Gray', bny)
cv2.imshow('Result', dst)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제