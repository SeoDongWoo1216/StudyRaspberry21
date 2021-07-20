# 글꼴 출력
import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상에 글자 출력
cap = cv2.VideoCapture(0)    # 웹캠 열기 -> 번호: 0부터 시작 ++
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔 고딕 볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)

# 무한루프 (q를 입력할때 까지)
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    h, _, _ = frame.shape  # Width, Channel은 불필요
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')


    if ret != True: break   # ret이 False이면 루프탈출
    
    frame = Image.fromarray(frame) # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame)    

    # 글자 출력(실시간 웹캠 - '현재시간')
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0,0,255))  # 글자 위치 조정, xy : 글자가 들어갈 최초 위치
    frame = np.array(frame)        # 원상태로 복귀

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움
    if cv2.waitKey(1) == ord('q'): break    # q입력시 루프 탈출

cap.release()   # 웹캠 해제
cv2.destroyAllWindows()