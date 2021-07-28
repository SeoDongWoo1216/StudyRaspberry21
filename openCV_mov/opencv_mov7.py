# 영상 녹화 openCV

import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

## 함수 선언 영역
## 영상 간의 차이나는 부분을 표시 이미지, 차이나는 픽셀 개수를 리턴해주는 함수
def get_diff_image(frame_a, frame_b, frame_c, threshold):
    # 3개 모든 프레임을 흑백으로 전환
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    # a ~ b 영상 차이값, b ~ c 영상 차이값 구하기
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray) # a ~ b는 차이가 없을꺼라 예상(초기에 찍으니까)
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray) # 차이값 없을수도 or 차이가 날수도 있음

    # 영상 차이값이 40 이상이면 값을 흰색으로 변환
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)  # a ~ b 차이 값을 찾기
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)  # b ~ c 차이 값을 찾기

    # 두 영상에서 공통된 부분은 1로 만듬
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t) 

    # 영상에서 1이 된 부분은 확장(morphology)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) # kernel 값 구하기
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt = cv2.countNonZero(diff)
    return diff, diff_cnt


# 카메라 기본 틀
# 움직임 발생시 화면 캡처
cap = cv2.VideoCapture(0)    # 웹캠 열기 -> 번호: 0부터 시작 ++
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480) # 넓이와 높이 설정(정적)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

# 나눔고딕볼드 로드(폰트 가져오기)
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)

# 영상 코덱 설정(저장하기 위해 필요)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # H263 코덱
is_record = False  # 녹화 상태를 알려줄 Flag

threshold = 40     # 영상 차이가 나는 threshold 설정
diff_max = 10      # 영상에서 차이가 나는 최대 픽셀 수(10 이상이면 캡처 하는 식으로 활용할 예정)

# 초기프레임으로 사용할 프레임 최초 저장
ret, frame_a = cap.read()
ret, frame_b = cap.read()

# 무한루프 (q를 입력할때 까지 계속 녹화함)
while True:
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H%M%S') # 영상에 보여줄 현재 시간
    fileDateTime = now.strftime('%Y%m%d_%H%M%S')   # 파일에 현재 시간 저장20210720_164725

    # 현재 영상 입력
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret True/False
    h, w, _ = frame.shape 

    if ret != True: break   # ret이 False이면 루프탈출
    
    # 현재 영상과 초기 영상 비교, 움직임 감지
    diff, diff_cnt = get_diff_image(frame_a = frame_a, frame_b = frame_b, frame_c = frame, threshold=threshold)

    # 차이나는 이미지 개수가 10개 이상이면 움직임이 발생했다고 판단하고 캡처
    if diff_cnt > diff_max:
        cv2.imwrite('./capture/img_{0}.png'.format(fileDateTime), frame)
        print('움직임 발생 : 이미지 저장 완료')

    # 움직임 결과 영상 출력
    cv2.imshow('Diff Result', diff)

    frame_a = np.array(frame_b) # 이전화면 이전
    frame_b = np.array(frame)   # 현재화면 이전

    frame = Image.fromarray(frame) # 글자 출력을 위해 변환
    draw = ImageDraw.Draw(frame) 

    # 글자 출력(실시간 웹캠 - '현재시간')
    draw.text(xy=(10, (h - 40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0,0,255))  # 글자 위치 조정, xy : 글자가 들어갈 최초 위치
    frame = np.array(frame)        # 원상태로 복귀

    # 키보드 인식 코드
    key = cv2.waitKey(1)
    if key == ord('q'): break  # q 버튼 입력시 루프 탈출(프로그램 종료)

    cv2.imshow('RealTime CAM', frame)  # 로드한 영상을 창에 띄움

cap.release()   # 웹캠 해제
cv2.destroyAllWindows()