# Structure
1. The code base and the documentation are on github.
2. Videos and images are in Dropbox

The code can find the videos and the images by the setting in the config-local.json file


## Code base
The projet contains these boundaries:

- 1.1. Camera calibration (Done)
- 1.2. Bucket identification (Not started)
- 1.3. Detection of asparagus: Viola–Jones object detection with opencv (Done)
- 1.4. Image processing of one asparagus (In progress)
- 1.5. Classification (Done)
- 1.6. Display the result (Not started)


### 1.1. Camera calibration

#### Description:
Establish the pixel millimater and millimeter pixel ratio.
The solution based on this, without the corrections use only the chessboard detection function:
http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

#### Input:
- RGB picture about a chessboard
- the length of the square of the board in millimeter

#### Output:
- millimeter pixel ratio
- pixel millimeter ratio
- variance of the detected chessboard squers edge size (check how good is the detection, if it is high it could be rerun)


### 1.2. Bucket identification by ORC

#### Description:
It identifies the bucket based on the bucket markes. (Each bucket markered by numbers redundatnly.) Use tesseract to idenrentify numbers
Main parts:
- set every input image to the correct resolution (image, bucketmarker template, template matching)
- identify templates
- identify numbers
- get the borders

#### **Inputs:**
- RGB image about conveyor belt
- RGB images about a bucket marker

#### **Outputs**
- founded numbers
- pozition of founded numbers


### 1.3. Recogition: Viola–Jones object detection with opencv

#### Description:
Use Viola–Jones object detection. It is implemented in OpenCV. The training of the cascade file based on this tutorial serial: **missing link :D**
Image rotationing.

#### **Input:**
- Haar cascade xml file
- RGB image
- scaling ratio: before detection resize the image, because of training method and searching time
- swing angle: when run Haar cascade detection, the image is rotated because of limitation of Viola–Jones object detection algorithm

#### **Outputs:**
- image about the asparagus
- rectangle data about the image, where it can be find in the original image (be able to order the objets on the image)


### 1.4. Image processing of one asparagus

#### Description:


####**Input:**
- Output of 1.3. point
- Future: input of classification specification,

If it calculated only that properties which are recuired to do the classification it would be much more effective. Now it is not a battleneck so it can wait.

####**Output:**
- asparagus thickness (done)
- asparagus length (done)
- purple flag (not done)
- head flag (not done)
- open head flag (not done)
- piper flag (not done)


### 1.5. Classification

#### Description:
Based on the cconditions (which are coded in the JSON file). It classify the asparagus.

####  Input:
- output 1.4.
- JSON file which contains the classification parameters

#### Output
- pozition of asparagus
- classification result


### 1.6. Display the result

#### Description:
There is not final decision about this boundary.

#### Input:
- output 1.4.
- JSON file which contains the classification parameters

#### Output
- Unknown


# Other
## Think about / Ideas:
### Random thoughts
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
- !!!!! i know how the backgraound look like, i don`t take adventage of it!!!!!
- global testing environment
- automatize Viola–Jones generetion. It it an idividual or a global szolution
- Make it available online
- later axamine the curl of the asparagus


### 1.2. Bucket identification

####Ideas:
- ORC seems overkill, it is simple convolution have to be enought, ORC have several bulit in detection solution
- trasholding because the number will be very black, binary comperisom could be more effective,
- laminated numbers, same which marks the collector workers,
- gluming,
- multiple marking because of unpredictable place of the asparagus,
- ordered pockets to be able to calculate from the neighbour pockets
- if necessery this process can run parallely with the OneAsparagus analysis (It would be a pain)


#### Problems:
- waterstone :)
- cleaning process of asparagus (kefe)
- wet environment
- the edge of the conveyor balt can reach the wall of the machine
- when the convinyon belt turns back the gloming can be harmed



## Need to buy:
- monitor?? VGA VS HMDI (both) - I will be my monitor in the bigining
- Racpberry PI VS laptop - laptop, because of the webcam, and the prototiping. The prortotipe without online interface will need significant resources.
