from main import handsFree
import cv2
import time

vid = cv2.VideoCapture(0)
i = 0
m = 0
arr = []
true = ['Human Is sitting', 'Left Arm with True Direction', 'Right Arm with True Direction', 'Body is straight', 'Left leg is straight', 'Right leg is straight']
count = 0
lenght = 0
while vid.isOpened():
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    if i % 30 == 0:
        t = time.time()
        res = handsFree(frame,arr)


        if res == True:
            m += 1
        else:
            m = 0
        #print("prediction time: " + str(time.time() - t))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1

    if true == arr:
        print("Process Done")
        count += 1
    if count == 1:
        break

vid.release()
cv2.destroyAllWindows()