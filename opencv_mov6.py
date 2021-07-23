# 영상 녹화 openCV
# r : 녹화시작
# t : 녹화종료
# c : 지금 화면 캡처
# q : 프로그램 종료

import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
# 영상 캡쳐, 녹화
cap = cv2.VideoCapture(0)    # 웹캠 열기 -> 번호: 0부터 시작 ++
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔 고딕 볼드 로드(폰트 가져오기)
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)

# 영상 코덱 설정(저장하기 위해 필요)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # H263 코덱
is_record = False

# 무한루프 (q를 입력할때 까지)
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    h, w, _ = frame.shape  
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H%M%S')  # 영상에 보여줄 현재 시간
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') # 파일에 현재 시간 저장20210720_164725

    if ret != True: break   # ret이 False이면 루프탈출
    
    frame = Image.fromarray(frame) # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame) 

    # 글자 출력(실시간 웹캠 - '현재시간')
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0,0,255))  # 글자 위치 조정, xy : 글자가 들어갈 최초 위치
    frame = np.array(frame)        # 원상태로 복귀

    cv2.imshow('RealTime CAM', frame)   # 로드한 영상을 창에 띄움

    # 키보드 인식 코드
    key = cv2.waitKey(1)
    if key == ord('q'): break  # q 버튼 입력시 루프 탈출(프로그램 종료)

    elif key == ord('c'):      # c 버튼 누르면 화면캡처
        cv2.imwrite('./capture/img_{0}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')

    elif key == ord('r'):  # r 버튼 누르면 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./capture/record_{0}.avi'.format(fileDateTime), fourcc, 20, (w, h)) # width, height 순으로넣음
        print('녹화 시작')

    elif key == ord('t'):  # t 버튼 누르면 레코드 종료
        is_record = False
        video.release()  # 비디오 객체 해제(메모리 할당 해제)
        print('녹화 완료')

    if is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius = 5, color=(0,0,255), thickness = 3)

    cv2.imshow('RealTime CAM', frame)  # 로드한 영상을 창에 띄움

cap.release()   # 웹캠 해제
cv2.destroyAllWindows()