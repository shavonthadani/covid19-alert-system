import cv2, time

video = cv2.VideoCapture(0)
mask_cascade=cv2.CascadeClassifier("haarcascade_mask2.xml")
while True:
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    video.set(10, cameraBrightness)


    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    objects = mask_cascade.detectMultiScale(gray,1.2,5)

    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(frame, 'Mask On', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
            roi_color = frame[y:y + h, x:x + w]

    cv2.imshow('capturing',frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
