import cv2

cam = cv2.VideoCapture(0)  # 기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # 창

while True: 
    ret, frame = cam.read()  # 웹캠 읽기

    if ret:
        cv2.imshow('Original Video', frame) # 카메라 영상 제목에 ' ' 이름으로 창에 띄움

        key = cv2.waitKey(1)
        if key == ord('q'):  # q를 입력받으면
            break
        elif key == ord('c'):
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지 캡처 완료')

cam.release()
cv2.destroyAllWindows