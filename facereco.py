import cv2
cascPath=r"C:\Users\adity\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascPath)
video_capture=cv2.VideoCapture(0)
while True:
    #capture the videofeed
    ret,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=faceCascade.detectMultiScale(
        gray,scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE)

    #draw the rectangle around the detected face in the image
    
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(125,255,125),2)
    
    #display the video with bounded rectangular box around the face
    
    cv2.imshow('video',frame)
    if cv2.waitKey(1)&0xff==ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()