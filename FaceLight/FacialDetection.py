import serial
import cv2



faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
winWidth = 800
winHeight = 600

def XY_to_Angle(x,y):
    theta,phi = 0,0
    kx,ky = 180/winWidth, 180/winWidth
    theta = x*kx 
    phi = y*ky
    return theta,phi

data = "X{X:},Y{Y:}"
    
while True:
    ret,frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # turn image into grayscale
    frame = cv2.flip(frame, 1)    # vertically flip image
    frame = cv2.resize(frame, (winWidth,winHeight))
    
    faces = faceCascade.detectMultiScale(frame,1.1,4)
    
    for (x, y , w ,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0 , 255), 3)
        #print(data.format(X = XY_to_Angle(x,y)[0],Y = XY_to_Angle(x,y)[1]))
        ser.write(data.format(X = XY_to_Angle(x,y)[0],Y = 180 - XY_to_Angle(x,y)[1]).encode())
        
    cv2.imshow('Capture',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


