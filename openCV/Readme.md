# OpenCV Image 처리
1. [이미지 원본 출력](#01.-이미지-원본-출력)
2. [흑백 처리](#02.-흑백-처리)
3. [Cropped 처리](#03.-Cropped-처리)
4. [Blur 처리](04.-Blur-처리)
5. [noise 처리](#05.-nosie-처리)
6. [enhance 처리](#06.-enhance-처리)
7. [경계선 처리](#07.-경계선-처리)
-------------

### 01. 이미지 원본 출력
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img01(Original).PNG" >

```Pyhton
import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어있지 않아서 numpy

org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절

cv2.imshow('Original', dst) # 이미지를 새 창에 띄우기

cv2.waitKey(0)  # 창에서 키입력 대기
cv2.destoryAllWindows() # 메모리 해제
```

<br>

### 02. 흑백 처리
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img02(%ED%9D%91%EB%B0%B1).PNG" >

```pyhton
import cv2
import numpy as np # C#의 리스트, 행렬이 포함되어있지 않아서 numpy

org = cv2.imread('./image/manarola.jpg', cv2.IMREAD_REDUCED_COLOR_2) 
dst = cv2.resize(org, dsize=(480, 320))  # 이미지가 너무 커서 사이즈 조절
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY) # 흑백처리

h, w, c = dst.shape
print('Width:{0}, Height:{1}m Channel:{2}'.format(w, h, c))


cv2.imshow('Original', dst) # 이미지를 새창에 띄우기
cv2.imshow('Gray', gray)    # 흑백처리 사진 띄우기

cv2.waitKey(0)  # 창에서 키입력 대기
cv2.destoryAllWindows() # 메모리 해제
```

<br>

### 03. Cropped 처리
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img03(Cropped).PNG" >

```pyhton
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
```

<br>

### 04. Blur 처리
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img04(Blur).PNG" >

```pyhton
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
```

<br>

### 05. noise 
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img05(noise).PNG" >

```pyhton
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
cv2.destroyAllWindows() # 메모리 해제
```

<br>

### 06. enhance 처리
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img06(enhance).PNG" >

```pyhton
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
```

<br>

### 07. 경계선 처리
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/opencv_image/opencv_img07.PNG" >

```pyhton
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
```
