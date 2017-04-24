import pandas as pd
import datetime


class MeasurementsEvaluatorWidthHigh:
    def __init__(self,
                 minimum_repeated_measurement_number,
                 no_on_screen_frame_number_limit,
                 survive_time):

        self.minimum_repeated_measurement_number = minimum_repeated_measurement_number
        self.no_on_screen_frame_number_limit = no_on_screen_frame_number_limit
        self.survive_time = datetime.timedelta(seconds=survive_time)

        self.frame_id = 0
        self.measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])

    def add_measurement(self, bucket_number, width, high):
        self.frame_id += 1
        new_row = [self.frame_id, datetime.datetime.now(), bucket_number, width, high]

        self.measurements_feed.loc[len(self.measurements_feed)] = new_row

    def get_display_feed(self):
        self.delete_old_measurements()

        unique_bucket_numbers = self.measurements_feed.bucket_number.unique()

        for unique_bucket_number in unique_bucket_numbers:
            actual_bucket_number_measurements = \
                self.measurements_feed[self.measurements_feed.bucket_number == unique_bucket_number]

            no_on_screen_condition = \
                self.frame_id - max(actual_bucket_number_measurements.frame_id) >= self.no_on_screen_frame_number_limit

            repeated_measurement_condition = len(actual_bucket_number_measurements) >=\
                                             self.minimum_repeated_measurement_number

            if no_on_screen_condition and repeated_measurement_condition:

                avg_width = actual_bucket_number_measurements.width.mean()
                avg_high = actual_bucket_number_measurements.high.mean()
                return [unique_bucket_number, avg_width, avg_high]

        return None

    def delete_old_measurements(self):
        rows_index_to_keep = (datetime.datetime.now() - self.measurements_feed["time"]) < self.survive_time
        self.measurements_feed = self.measurements_feed[rows_index_to_keep]

    def delete_displayed_item_from_measurement_feed(self, bucket_number):
        row_index_to_keep = self.measurements_feed.bucket_number != bucket_number
        self.measurements_feed = self.measurements_feed[row_index_to_keep]