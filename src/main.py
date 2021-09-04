from extract_featues import calculate_angle, calculate_distance, extract_features_from_pose
from innacurate_recognizing import features_analysis
from extract_pose import pose_to_points
from argparse import ArgumentParser
import mediapipe as mp
import math
import cv2



def handsFree(img,array) -> bool:
    #img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_pose_detect = mp.solutions.pose.Pose()
    pose = mp_pose_detect.process(img)
    points = pose_to_points(img, pose)
    title = ""
    if len(points) > 0:
        features = extract_features_from_pose(points)
        inaccurates = features_analysis(features,array)

        if len(inaccurates) > 0:
            title = tuple(inaccurates)
            print(title)
        else:
            return True

    else:
        title = ('Can not detect pose')
        return False

    return False




