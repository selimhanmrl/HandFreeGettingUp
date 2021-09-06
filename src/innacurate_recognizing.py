#Recognize innacurate pose
def features_analysis(features,array):
    '''Determine which corrections are needed from features'''

    if features['norm_dist__right_waist__right_foot'] < 0.05 :
        if features['angle__left_thigh__left_calf'] < 90 :
            if 'Human Is sitting' not in array:
                array.append('Human Is sitting')



            if features['angle__left_hand__left_shoulder'] > 60 :
                if 'Left Arm with True Direction' not in array:
                    if 'Wrong Direction' in array:
                        array.remove('Wrong Direction')
                    array.append('Left Arm with True Direction')


            if features['angle__right_hand__right_shoulder'] > 60:
                if 'Right Arm with True Direction' not in array:
                    if 'Wrong Direction' in array:
                        array.remove('Wrong Direction')
                    array.append('Right Arm with True Direction')


    if features['angle__left_thigh__left_calf'] > 170:
        if 'Left leg is straight' not in array:
            if 'Human Is sitting' in array:
                array.append('Left leg is straight')
    elif features['angle__left_upper__left_lower'] > 160:
        if 'Body is straight' not in array:
            if 'Human Is sitting' in array:
                array.append('Body is straight')

    if features['angle__right_thigh__right_calf'] > 170:
        if 'Right leg is straight' not in array:
            if 'Human Is sitting' in array:
                array.append('Right leg is straight')
    elif features['angle__right_upper__right_lower'] > 160:
        if 'Body is straight' not in array:
            if 'Human Is sitting' in array:
                array.append('Body is straight')

    
    return array