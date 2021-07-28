import cv2
import numpy as np

# 카메라 기본 틀
cap = cv2.VideoCapture(0) # 번호 0부터 +1 웹캠 열기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 수동설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한루프 (q를 입력할때까지)
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False

    if ret != True: break # ret이 False면 루프탈출

    # h, w, c = frame.shape  # 영상 h, w, c 정보알아오기
    # print('Width : {0}, Height: {1}, Channel: {2}'.format(w, h, c))

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움

    if cv2.waitKey(1) == ord('q'): #q를 입력하면 루프탈출
        break

cap.release() # 웹캠 해제
cv2.destroyAllWindows()