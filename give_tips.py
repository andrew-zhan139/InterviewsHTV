import numpy.random
import json

numpy.random.seed(0)

def givetips(data):

    #smile, roll, pitch, yaw, good
    smile = data['smile']
    roll = data['pose_roll']
    pitch = data['pose_pitch']
    yaw = data['pose_yaw']
    good = data['good_emotion']
    tips = []
    rand = 0
    if (smile <= -0.5):
        rand = numpy.random.randint(0,3)
        if (rand == 0):
            tips.append("Try to smile more!")
        elif (rand == 1):
            tips.append("Show those teeth!")
        elif (rand == 2):
            tips.append("Smiling makes you appear friendlier!")
        else:
            tips.append("Try to loosen up!")
    if (roll > 30 or pitch > 30 or yaw > 30):
        tips.append("Make sure you face the interviewer!")
    if (good < 0):
        tips.append("Relax a little bit, you look stressed!")
    return json.dumps(tips)

