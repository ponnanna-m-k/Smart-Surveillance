import cv2
import winsound
import time
import playsound

count = 0
# count2 = 0
hog = cv2.HOGDescriptor()

hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
try:
    # cap = cv2.VideoCapture("http://192.168.43.122:8080/video")
    # cap = cv2.VideoCapture( "Violation_of_Helmet/Video1/video1.mp4" )
    cap = cv2.VideoCapture( "Violation_of_Helmet/video1_Trim.mp4" )
except:
    print("Video not found")

while True:
    start_time = time.time()
    r, frame = cap.read()

    if r:

        # start_time = time.time()

        frame = cv2.resize( frame, (480, 360) )  # Downscale to improve frame rate
        gray_frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )  # HOG needs a grayscale image

        rects, weights = hog.detectMultiScale( gray_frame )

        # Measure elapsed time for detection

        # end_time = time.time()
        # print( "Elapsed time:", end_time - start_time )
        print( count )
        if (count > 100):
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 2000  # Set Duration To 1000 ms == 1 second
            winsound.Beep( frequency, duration )
            # playsound("buzzer.mp3")

        for i, (x, y, w, h) in enumerate( rects ):

            if weights[i] < 0.7:
                continue

            cv2.rectangle( frame, (x, y), (x + w, y + h), (0, 255, 0), 2 )
            count += 1
        # end_time = time.time()
        # print( "Elapsed time:",round(start_time/1000, 3))
        cv2.imshow( "preview", frame )

    k = cv2.waitKey( 1 )

    if k & 0xFF == ord( "q" ):
        break