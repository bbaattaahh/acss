# Structure
1. The code base and the documentation are on github.
2. Videos and images are on Dropbox

The code can find the videos and the images by the setting in the config-local.json file


## Code base
The projet contains these boundaries. Overview.

1.1. Camera calibration
1.2. Bucket identification by ORC
1.3. Detection of asparagus: Viola–Jones object detection with opencv
1.4. Image processing of one asparagus
1.5. Classification
1.6. Display the result


### 1.1. Camera calibration
Establish the pixel millimater ratio.

The solution based on this, without the corrections use only the chessboard detection function:
http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
**Input:**
- RGB picture about a chessboard
- the length of the square of the board in millimeter

**Output:**
- millimeter pixel ratio
- pixel millimeter ratio
- variance of the detected chessboard squers edge size (check how good is the detection, if it is high it could be rerun)

### 1.2. Bucket identification by ORC
On 0%.

### 1.3. Recogition: Viola–Jones object detection with opencv

Use Viola–Jones object detection. It is implemented in OpenCV.
Image rotationing.
**Input:**
- Haar cascade xml file
- RGB image
- scaling ratio: before detection resize the image, because of theching method and seaching tim
- swing angle: when run Haar cascade detection, the image is rotated because of limitation of Viola–Jones object detection algorithm

**Outputs:**
- image about the asparagus
- rectangle data about the image, where it can be find in the original image (be able to order the objets on the image)

### 1.4. Image processing of one asparagus
**Input:**
- Output of 1.3. point

**Output:**
- asparagus thickness (done)
- asparagus length (done)
- purple flag (not done)
- head flag (not done)
- open head flag (not done)
- piper flag (not done)

### 1.5. Classification
**Input:**
- output 1.4.
- JSON file which contains the classification parameters

**Output**
- Unknown

### 1.6. Display the result

**Input:**
- output 1.4.
- JSON file which contains the classification parameters

**Output**
- Unknown


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
