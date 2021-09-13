from main import handsFree
import cv2
import time
from argparse import ArgumentParser
import sys


parser = ArgumentParser(description="import videos")
if len(sys.argv) > 1:
    parser.add_argument("-v", "--video",
                        nargs = "?",
                        help = "path to video dir")
    args = parser.parse_args()
    vid = cv2.VideoCapture(args.video)

else:
    vid = cv2.VideoCapture(0)
i = 0
m = 0
arr = []
true = ['Human Is sitting', 'Left Arm with True Direction', 'Right Arm with True Direction', 'Body is straight', 'Left leg is straight', 'Right leg is straight']
true.sort()
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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1
    arr.sort()
    if true == arr:
        print("Process Done")
        count += 1
    if count == 1:
        break

vid.release()
cv2.destroyAllWindows()