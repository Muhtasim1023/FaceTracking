# FaceTracking

*This is a face tracking robot meant to point a light at your face during zoom calls in order to provide optimal lighting for your face.*

In order to track the face and extract positional data from the camera Python's OpenCV library. Additionally, Python's Serial communication library was used to send the position data to an Arduino via the Serial Port. Now the method in which we converted the 2 dimentional Cartisian coordinates into two angular coordinates is we multiply it by a scale factor equal to (180 / Max hight or width of window). This will in turn limit the Serial data to the angular range of the Servo motor of (0 deg - 180 deg).

## Explaination of the Scale Factor 

<<insert images of cartisian to angular coordinates>>
<<also explain changes to range of>>
  



