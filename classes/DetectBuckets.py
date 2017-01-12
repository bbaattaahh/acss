import cv2

from ImageResizer import ImageResizer


class DetectBuckets:

    def __init__(self,
                 image,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution):

        self.image = image
        self.bucket_marker_template = bucket_marker_template
        self.bucket_marker_template_original_resolution = bucket_marker_template_original_resolution
        self.template_matching_resolution = template_matching_resolution



    @property
    def bucket_borders(self):
        bucket_borders = []
        _, template_width, _ = self.template_on_image.shape

        for detected_template in self.detected_bucket_markers:
            actual_bucket_border = detected_template[0] + template_width/2
            bucket_borders.append(actual_bucket_border)

        return bucket_borders

    @property
    def template_on_image(self):
        template_on_image = cv2.resize(self.bucket_marker_template,
                                       None,
                                       fx=self.bucket_marker_template_on_image_scale_factors[1],
                                       fy=self.bucket_marker_template_on_image_scale_factors[0],
                                       interpolation=cv2.INTER_CUBIC)
        return template_on_image

    @property
    def bucket_marker_template_on_image_scale_factors(self):
        height, width, _ = self.image.shape

        scale_factor_y = float(height) / self.bucket_marker_template_original_resolution[0]
        scale_factor_x = float(width) / self.bucket_marker_template_original_resolution[1]

        return scale_factor_y, scale_factor_x

    @property
    def detected_bucket_markers(self):
        back_scaled_vertices = []
        image_scale_factor_y, image_scale_factor_x = self.image_scale_factors

        for rectangle_top_left_vertex in self.matching_bucket_markers:
            actual_back_scaled_x = rectangle_top_left_vertex[0]/image_scale_factor_x
            actual_back_scaled_y = rectangle_top_left_vertex[1]/image_scale_factor_y
            back_scaled_vertices.append([actual_back_scaled_x, actual_back_scaled_y])

        return back_scaled_vertices




    @property
    def resized_image(self):
        image_resizer = ImageResizer(image=self.image,
                                     target_resolution=self.template_matching_resolution)
        resized_image = image_resizer.resized_image
        return resized_image

    @property
    def image_scale_factors(self):
        target_height, target_width = self.template_matching_resolution
        height, width, _ = self.image.shape

        scale_factor_y = float(target_height) / height
        scale_factor_x = float(target_width) / width

        return scale_factor_y, scale_factor_x

    @property
    def resized_bucket_marker_template(self):
        image_resizer = ImageResizer(image=self.bucket_marker_template,
                                     target_resolution=self.template_matching_resolution,
                                     parent_image_resolution=self.bucket_marker_template_original_resolution)
        resized_bucket_marker_template = image_resizer.resized_image
        return resized_bucket_marker_template

    # TODO Not tested
    @property
    def resized_middle_bucket_marker_template(self):
        image_resizer = ImageResizer(image=self.always_seen_middle_template,
                                     target_resolution=self.template_matching_resolution,
                                     parent_image_resolution=self.bucket_marker_template_original_resolution)
        resized_middle_bucket_marker_template = image_resizer.resized_image
        return resized_middle_bucket_marker_template
