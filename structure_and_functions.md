# Read in the image/video
    NOW it is just one image
    For the testing an video wuold be much better
    Later it will be a camera image
    

# Calculate the pixel millimeter ratio
    http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
Later, it will be a burned variable at first

# Image preprocessing
1. Motion detection
2. Histogram equlization

# Find the asparagus

    in-progress
    1. Dummy versoion : filter by summa, horizontally and vertically
    2. mouving avarage by the pixel posotion
    3. Get the numeric derivalt
    4. Get the min and max value of it
    5. Apply safety band
    
    ++ Handle the case when there is no asparagus on the picture 

# Classification of the found asparagus
    1. calculate the characteristic parameters, bounding box

# Print the result to the image
    1. Easy: cv2.putText
    
# Display the correc image delayed
    LATER, it is real time now
    
# Think about / Ideas:
	- olyankamera kellen amelzikenk beepitett szabalyozhato fenyforrasa van
	- rgb layerek kulon kezelese(kesobb)
	- preprocessing hist exualzation, wighted by the frequency of the colours
	- drop the end and the begining of the histogram if let us say it is les then the summa pixes 0,5%
	- if we found the one asparagus picture part, the equalize it it, + other tricks
	- usage of spared matrixis may be / it is not too good idea
	- preserve the fluencity of the camera mouvi
	- colour code to classification results
	- !!!handle that case when tehre is now asparage at all
	- analiis flow!!! 
	- link together the final output image, (link, rotation, resize)
	- !!!!! i know how the backgraound look like, i don`t take adventage of it!!!!!

# Need to buy:
	web camera - Bought
	black organic base piant - Bought
	monitor?? VGA VS HMDI (both) - I will be my monitor in the bigining
	Racpberry PI VS laptop - laptop, because of the webcam

	
# Burned constants:
	pixel-mm ratio
	threshol of the motion detection, beetween the last two images
	safety area in the detecting of the asparagus
