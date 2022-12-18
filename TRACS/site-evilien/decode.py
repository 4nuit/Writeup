import cv2

# read the QRCODE image
image = cv2.imread("qrcode.png",1)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
flag, bbox, straight_qrcode = detector.detectAndDecode(image)
print(flag)
