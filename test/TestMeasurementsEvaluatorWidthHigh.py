import unittest
import pandas as pd
import datetime
import time

from pandas.util.testing import assert_frame_equal

from MeasurementsEvaulatorWidthHigh import MeasurementsEvaluatorWidthHigh


class TestMeasurementsEvaluatorWidthHigh(unittest.TestCase):
    def test_add_measurement_working(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=2,
            survive_time=1)

        expected_measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])
        expected_measurements_feed.loc[0] = [0, datetime.datetime.now(), "001", 6784, 6784]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        actual_measurements_feed = measurement_evaluator_width_high.measurements_feed

        # that
        assert_frame_equal(actual_measurements_feed[["frame_id", "bucket_number", "width", "high"]],
                           expected_measurements_feed[["frame_id", "bucket_number", "width", "high"]])
        self.assertAlmostEqual(actual_measurements_feed.loc[0, "time"],
                               expected_measurements_feed.loc[0, "time"],
                               delta=datetime.timedelta(milliseconds=300))

    def test_get_display_feed_working(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=1,
            survive_time=10)

        expected_display_feed = ["001", 6784.0, 6784.0]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        time.sleep(1)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)

        actual_display_feed = measurement_evaluator_width_high.get_display_feed()

        self.assertEqual(actual_display_feed, expected_display_feed)

    def test_get_display_feed__measurements_feed_changes(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=1,
            survive_time=10)

        expected_measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])
        expected_measurements_feed.loc[2] = [2, datetime.datetime.now(), "002", 6785, 6785]
        expected_measurements_feed.loc[3] = [3, datetime.datetime.now(), "002", 6785, 6785]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        time.sleep(1)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)

        measurement_evaluator_width_high.get_display_feed()

        actual_measurements_feed = measurement_evaluator_width_high.measurements_feed

        # that
        assert_frame_equal(actual_measurements_feed[["frame_id", "bucket_number", "width", "high"]],
                           expected_measurements_feed[["frame_id", "bucket_number", "width", "high"]])

    def test_delete_old_measurements_working(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=2,
            survive_time=1)

        expected_measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])
        expected_measurements_feed.loc[1] = [1.0, datetime.datetime.now(), "002", 6785, 6785]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        time.sleep(1)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)
        measurement_evaluator_width_high.delete_old_measurements()
        actual_measurements_feed = measurement_evaluator_width_high.measurements_feed

        # that
        assert_frame_equal(actual_measurements_feed[["frame_id", "bucket_number", "width", "high"]],
                           expected_measurements_feed[["frame_id", "bucket_number", "width", "high"]])
        self.assertAlmostEqual(actual_measurements_feed.loc[1, "time"],
                               expected_measurements_feed.loc[1, "time"],
                               delta=datetime.timedelta(milliseconds=1300))

    def test_delete_displayed_item_from_measurement_feed_working(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=2,
            survive_time=1)

        expected_measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])
        expected_measurements_feed.loc[1] = [1.0, datetime.datetime.now(), "002", 6785, 6785]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)
        measurement_evaluator_width_high.delete_displayed_item_from_measurement_feed("001")
        actual_measurements_feed = measurement_evaluator_width_high.measurements_feed

        # that
        assert_frame_equal(actual_measurements_feed[["frame_id", "bucket_number", "width", "high"]],
                           expected_measurements_feed[["frame_id", "bucket_number", "width", "high"]])
        self.assertAlmostEqual(actual_measurements_feed.loc[1, "time"],
                               expected_measurements_feed.loc[1, "time"],
                               delta=datetime.timedelta(milliseconds=300))

    def test_double_to_display_feed(self):
        # given
        measurement_evaluator_width_high = MeasurementsEvaluatorWidthHigh(
            minimum_repeated_measurement_number=2,
            no_on_screen_time_before_display=1,
            survive_time=5)

        expected_measurements_feed = pd.DataFrame(columns=["frame_id", "time", "bucket_number", "width", "high"])
        expected_measurements_feed.loc[3] = [3, datetime.datetime.now(), "002", 6785, 6785]

        # when
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        measurement_evaluator_width_high.add_measurement(bucket_number="001", width=6784, high=6784)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)
        time.sleep(5)
        measurement_evaluator_width_high.add_measurement(bucket_number="002", width=6785, high=6785)

        x = measurement_evaluator_width_high.get_display_feed()

        actual_measurements_feed = measurement_evaluator_width_high.measurements_feed

        # that
        assert_frame_equal(actual_measurements_feed[["frame_id", "bucket_number", "width", "high"]],
                           expected_measurements_feed[["frame_id", "bucket_number", "width", "high"]])


if __name__ == '__main__':
    unittest.main()
