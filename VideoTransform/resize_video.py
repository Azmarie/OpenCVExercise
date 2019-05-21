test_video = cv2.VideoCapture("firework.mp4")
background = cv2.resize(test_video, (1280, 720))
cv2.imshow("video", test_video)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('firework_output.mp4',fourcc, 5, (1280,720))

while True:
    ret_2, frame = test_video.read()
    if ret_2 == True:
        b = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        out.write(b)
    else:
        break