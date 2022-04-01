import cv2

window_name = "Detected Objects in webcam"
video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    whitechecker_classifier = cv2.CascadeClassifier(r"C:\Users\karva\Documents\KOOL\UT\pildid ja kaskaadid\praktika pildid\valgekabend\classifier\vkabend.xml")
    blackchecker_classifier = cv2.CascadeClassifier(r"C:\Users\karva\Documents\KOOL\UT\pildid ja kaskaadid\praktika pildid\mustkabend\classifier\mkabend.xml")
    checkerboard_classifier = cv2.CascadeClassifier(r"C:\Users\karva\Documents\KOOL\UT\pildid ja kaskaadid\praktika pildid\kabelaud\classifier\kabelaud.xml")

    detected_whitecheckers = whitechecker_classifier.detectMultiScale(image, minSize=(50, 50))
    detected_blackcheckers = blackchecker_classifier.detectMultiScale(image, minSize=(50, 50))
    detected_checkerboards = checkerboard_classifier.detectMultiScale(image, minSize=(50, 50))

    if len(detected_whitecheckers) != 0:
        for (x, y, width, height) in detected_whitecheckers:
            cv2.rectangle(frame, (x, y), (x + height, y + width), (255, 0, 0), 2)
        
    if len(detected_blackcheckers) != 0:
        for (x, y, width, height) in detected_blackcheckers:
            cv2.rectangle(frame, (x, y), (x + height, y + width), (0, 0, 255), 2)
            
    if len(detected_checkerboards) != 0:
        for (x, y, width, height) in detected_checkerboards:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
    
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()