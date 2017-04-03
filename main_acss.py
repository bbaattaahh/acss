__author__ = 'Henrik'

import cv2
import json

with open('./config/config-local.json') as data_file:
    config = json.load(data_file)

cap = cv2.VideoCapture(0)
cap.set(3, config["web_camera_distribution"][0])
cap.set(4, config["web_camera_distribution"][1])
