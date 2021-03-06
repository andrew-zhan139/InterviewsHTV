import boto3
from botocore.client import Config
import os
import random

#here = os.path.dirname(os.path.abspath(__file__))

#filename = os.path.join(here, 'example.jpg')

ACCESS_KEY = 'AWS_ACCESS_KEY'
SECRET_KEY = 'AWS_SECRET_KEY'
bucketname = 'hack-the-valley-photo'
#data = open(filename, 'rb')

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

import cv2, time
def getImage(timer):
    video = cv2.VideoCapture(0)
    a = 0
    while a < timer:
        a = a + 1
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'example.jpg')
        data = open(filename, 'rb')
        check, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gener = random.randint(1, 100000000000000000000000000000000000000000000000000000000000)
        if a % 10 == 0:
            cv2.imwrite(filename, frame)

            s3.Bucket(bucketname).put_object(Key="{}.jpg".format(gener), Body=data)
