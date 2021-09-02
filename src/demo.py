from main import handsFree
import cv2
import time

vid = cv2.VideoCapture(0)
i = 0
m = 0
while vid.isOpened():
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    if i % 30 == 0:
        t = time.time()
        res = handsFree(frame)

        if res == True:
            m += 1
        else:
            m = 0
        #print("prediction time: " + str(time.time() - t))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1

vid.release()
cv2.destroyAllWindows()