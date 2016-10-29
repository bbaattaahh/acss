# Structure
1. The code base and the documentation are on github.
2. Videos and images are on Dropbox

The code can find the videos and the images by the setting in the config-local.json file


## Code base
The projet contains these boundaries. Overview.

1.1. Camera calibration
1.2. Bucket identification by ORC
1.3. Recogition of asparagus: Viola–Jones object detection with opencv
1.4. Image processing of one asparagus
1.5. Classification
1.6. Display the result


### 1.1. Camera calibration
Establish the pixel millimater ratio. Later, it will be a burned variable at first. But the notion something like this:
http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

### 1.2. Bucket identification by ORC
On 0%.

### 1.3. Recogition: Viola–Jones object detection with opencv

Use Viola–Jones object detection. It is implemented in OpenCV.
No image rotationing because it is to expensive, instead we want to find even the not horizontal asparaguses.
- it should be reproducible

### 1.4. Image processing of one asparagus


### 1.5. Classification


### 1.6. Display the result
Easy: cv2.putText


# Other
## Think about / Ideas:
- Motion detection
- Histogram equlization
- camera with built-in light source
- rgb layers are examined separatly, later
- preprocessing hist exualzation, wighted by the frequency of the colours
- drop the end and the begining of the histogram if let us say it is les then the summa pixes 0,5%
- if we found the one asparagus picture part, the equalize it it, + other tricks
- preserve the fluencity of the camera mouvi
- color code to classification results
- drow analiis flow
- link together the final output image, (link, rotation, resize)
- !!!!! i know how the backgraound look like, i don`t take adventage of it!!!!!
- global testing environment
- automatize Viola–Jones generetion. It it an idividual or a global szolution
- Make it available online


## Need to buy:
- monitor?? VGA VS HMDI (both) - I will be my monitor in the bigining
- Racpberry PI VS laptop - laptop, because of the webcam


## Summary of burned constants:
- pixel-mm ratio
- threshol of the motion detection, beetween the last two images
- safety area in the detecting of the asparagus
