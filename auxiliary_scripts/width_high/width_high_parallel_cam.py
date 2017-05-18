from moviepy.editor import *
import cv2
import json
import numpy as np
import datetime
import multiprocessing as mp
import sqlite3
import time

from MeasurementsEvaulatorWidthHigh import MeasurementsEvaluatorWidthHigh
from DisplayClassification import DisplayClassification
from OneFrameWidthHighProcessor import OneFrameWidthHighProcessor


def evaluate_frame(process_instance, frame, queue):
    bucket_asparagus_pairs = process_instance.process_frame(frame)
    queue.put(bucket_asparagus_pairs)

if __name__ == '__main__':

    with open('./auxiliary_scripts/width_high/config_width_high.json') as data_file:
        config = json.load(data_file)

    measurements_evaluator = MeasurementsEvaluatorWidthHigh(
                                    config["measurements_evaluator_width_high"]["minimum_repeated_measurement_number"],
                                    config["measurements_evaluator_width_high"]["no_on_screen_time_before_display"],
                                    config["measurements_evaluator_width_high"]["survive_time"])

    processor = OneFrameWidthHighProcessor(config_file='./auxiliary_scripts/width_high/config_width_high.json')


    q = mp.Queue(maxsize=2)

    displayer = DisplayClassification(image_size=tuple(config["display"]["image_size"]),
                                      letter_pixel_high=config["display"]["letter_pixel_high"])

    conn = sqlite3.connect(config["local_db_path"])
    c = conn.cursor()

    cap = cv2.VideoCapture(0)
    cap.set(3, config["web_camera_distribution"][0])
    cap.set(4, config["web_camera_distribution"][1])

    while True:

        _, frame = cap.read()

        frame = np.array(np.rot90(frame, config["rotation_factor"]))

        p = mp.Process(target=evaluate_frame, args=(processor, frame, q))
        p.start()


        small = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
        cv2.imshow('frame', small)

        if not q.empty():
            bucket_asparagus_pairs = q.get()
            if bucket_asparagus_pairs:
                print(bucket_asparagus_pairs)
                for bucket_asparagus_pair in bucket_asparagus_pairs:
                    measurements_evaluator.add_measurement(bucket_number=bucket_asparagus_pair[0],
                                                           width=bucket_asparagus_pair[1][0],
                                                           high=bucket_asparagus_pair[1][1])


        actual_raw_feed = measurements_evaluator.get_display_feed()

        if actual_raw_feed:
            # print(actual_raw_feed)
            timestamp = int(time.time())
            c.execute("INSERT INTO measurements VALUES (?, ?, ?, ?)",
                      (timestamp, actual_raw_feed[1], actual_raw_feed[2], actual_raw_feed[0]))
            conn.commit()
            width_high_data = str(actual_raw_feed[1]) + "    " + str(actual_raw_feed[2])
            displayer.add_new_result(actual_raw_feed[0], width_high_data)

        displayer.display_actual()


        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        end_1 = datetime.datetime.now()
        #print("Loop time:")
        #print(end_1 - start_1)

    cv2.destroyAllWindows()
    end = datetime.datetime.now()
    cap.release()

    displayer.kill()


    conn.close()
    print("the end")