import mediapipe as mp
import math

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

def calculate_distance(x1, y1, x2, y2):
    '''Calculate distance between 2 points in 2D space'''
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def calculate_angle(x1, y1, x2, y2, x3, y3):
    '''Calculate angel between 3 points in 2D space'''
    ux, uy = x2 - x1, y2 - y1
    vx, vy = x2 - x3, y2 - y3
    cos = (ux * vx + uy * vy) / (math.sqrt(ux*ux + uy*uy) * math.sqrt(vx*vx + vy*vy))
    return math.degrees(math.acos(cos))



def extract_features_from_pose(points):
    '''Extract features based on relative positions of body parts'''
    # Because the body size in images are different, we use the total length of the pose connection
    # path to normalize the distance between body parts.
    pose_connections_length = 0
    for con in mp_pose.POSE_CONNECTIONS:
        pose_connections_length += calculate_distance(points[con[0]][0], points[con[0]][1],
                                                      points[con[1]][0], points[con[1]][1])

    # Distance between right side of waist  and right foot  (for sitting position)
    dist__right_waist__right_foot = calculate_distance(points[mp_pose.PoseLandmark.RIGHT_HIP][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_HIP][1],
                                                     points[mp_pose.PoseLandmark.RIGHT_HEEL][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_HEEL][1])
    norm_dist__right_waist__right_foot = dist__right_waist__right_foot / pose_connections_length

    # Distance between left side of waist and left foot (for sitting position)
    dist__left_waist__left_foot = calculate_distance(points[mp_pose.PoseLandmark.LEFT_HIP][0],
                                                     points[mp_pose.PoseLandmark.LEFT_HIP][1],
                                                     points[mp_pose.PoseLandmark.LEFT_HEEL][0],
                                                     points[mp_pose.PoseLandmark.LEFT_HEEL][1])
    norm_dist__left_waist__left_foot = dist__left_waist__left_foot / pose_connections_length


    # Distance between left knee and left hand (For getting up)
    dist__left_hip__left_hand = calculate_distance(points[mp_pose.PoseLandmark.LEFT_KNEE][0],
                                                    points[mp_pose.PoseLandmark.LEFT_KNEE][1],
                                                    points[mp_pose.PoseLandmark.LEFT_PINKY][0],
                                                    points[mp_pose.PoseLandmark.LEFT_PINKY][1])
    norm_dist__left_hip__left_hand = dist__left_hip__left_hand / pose_connections_length

    # Distance between right knee and right hand  (For getting up)
    dist__right_hip__right_hand = calculate_distance(points[mp_pose.PoseLandmark.RIGHT_KNEE][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_KNEE][1],
                                                     points[mp_pose.PoseLandmark.RIGHT_PINKY][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_PINKY][1])
    norm_dist__right_hip__right_hand = dist__right_hip__right_hand / pose_connections_length

    # Angle left shoulder for calculate arm direction
    angle__left_hand__left_shoulder = calculate_angle(points[mp_pose.PoseLandmark.LEFT_PINKY][0],
                                                   points[mp_pose.PoseLandmark.LEFT_PINKY][1],
                                                   points[mp_pose.PoseLandmark.LEFT_SHOULDER][0],
                                                   points[mp_pose.PoseLandmark.LEFT_SHOULDER][1],
                                                   points[mp_pose.PoseLandmark.LEFT_HIP][0],
                                                   points[mp_pose.PoseLandmark.LEFT_HIP][1])

    # Angle right shoulder for calculate arm direction
    angle__right_hand__right_shoulder = calculate_angle(points[mp_pose.PoseLandmark.RIGHT_PINKY][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_PINKY][1],
                                                      points[mp_pose.PoseLandmark.RIGHT_SHOULDER][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_SHOULDER][1],
                                                      points[mp_pose.PoseLandmark.RIGHT_HIP][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_HIP][1])



    # Angle of left leg (to determine leg is straight or not)
    angle__left_thigh__left_calf = calculate_angle(points[mp_pose.PoseLandmark.LEFT_ANKLE][0],
                                                          points[mp_pose.PoseLandmark.LEFT_ANKLE][1],
                                                          points[mp_pose.PoseLandmark.LEFT_KNEE][0],
                                                          points[mp_pose.PoseLandmark.LEFT_KNEE][1],
                                                          points[mp_pose.PoseLandmark.LEFT_HIP][0],
                                                          points[mp_pose.PoseLandmark.LEFT_HIP][1])

    # Angle of right leg (to determine leg is straight or not)
    angle__right_thigh__right_calf = calculate_angle(points[mp_pose.PoseLandmark.RIGHT_ANKLE][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_ANKLE][1],
                                                     points[mp_pose.PoseLandmark.RIGHT_KNEE][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_KNEE][1],
                                                     points[mp_pose.PoseLandmark.RIGHT_HIP][0],
                                                     points[mp_pose.PoseLandmark.RIGHT_HIP][1])


    # Angle of left upper body and left lower body (to determine the body is straight or not)
    angle__left_upper__left_lower = calculate_angle(points[mp_pose.PoseLandmark.LEFT_ANKLE][0],
                                                    points[mp_pose.PoseLandmark.LEFT_ANKLE][1],
                                                    points[mp_pose.PoseLandmark.LEFT_HIP][0],
                                                    points[mp_pose.PoseLandmark.LEFT_HIP][1],
                                                    points[mp_pose.PoseLandmark.LEFT_SHOULDER][0],
                                                    points[mp_pose.PoseLandmark.LEFT_SHOULDER][1])

    # Angle of right upper body and right lower body (to determine the body is straight or not)
    angle__right_upper__right_lower = calculate_angle(points[mp_pose.PoseLandmark.RIGHT_ANKLE][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_ANKLE][1],
                                                      points[mp_pose.PoseLandmark.RIGHT_HIP][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_HIP][1],
                                                      points[mp_pose.PoseLandmark.RIGHT_SHOULDER][0],
                                                      points[mp_pose.PoseLandmark.RIGHT_SHOULDER][1])

    return {
        'norm_dist__right_waist__right_foot': norm_dist__right_waist__right_foot,
        'norm_dist__left_waist__left_foot': norm_dist__left_waist__left_foot,
        'norm_dist__left_hip__left_hand': norm_dist__left_hip__left_hand,
        'norm_dist__right_hip__right_hand': norm_dist__right_hip__right_hand,
        'angle__left_thigh__left_calf': angle__left_thigh__left_calf,
        'angle__right_thigh__right_calf': angle__right_thigh__right_calf,
        'angle__left_upper__left_lower': angle__left_upper__left_lower,
        'angle__right_upper__right_lower': angle__right_upper__right_lower,
        'angle__left_hand__left_shoulder': angle__left_hand__left_shoulder,
        'angle__right_hand__right_shoulder': angle__right_hand__right_shoulder

    }
