#Recognize innacurate pose
def features_analysis(features):
    '''Determine which corrections are needed from features'''
    inaccurates = []


    if features['norm_dist__right_waist__right_foot'] < 0.05:
        if features['angle__left_thigh__left_calf'] < 90 :
            print('Human Is sitting')
            if features['angle__left_hand__left_shoulder'] < 60:
                print('Wrong Direction')
            elif features['angle__right_hand__right_shoulder'] < 60:
                print('Wrong Direction')
            else:
                print('True Direction')


    if features['angle__left_thigh__left_calf'] < 170:
        print('Left leg is not straight')
    elif features['angle__left_upper__left_lower'] < 160:
        print('Body is not straight')


    if features['angle__right_thigh__right_calf'] < 170:
      print('Right leg is not straight')
    elif features['angle__right_upper__right_lower'] < 160:
      print('Body is not straight')

    
    return inaccurates