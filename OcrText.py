import cv2
import numpy as np
import requests
import io
import json

img=cv2.imread("hf.jpg")
height, width, _ =img.shape
print(img)
print(img.shape)
#cutting image
roi=img[0:height,0:width]

url_api = "https://api.ocr.space/parse/image"
_,compressedimage=cv2.imencode(".jpg",roi,[1,90])
file_bytes=io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"hf.jpg": file_bytes},
              data = {"apikey": "bb0f4dac0388957",
                      "language": "eng"})
result=result.content.decode()
#print(result)
print(type(result))
result=json.loads(result)
#print(type(result))

text_detected=result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)
cv2.imshow("roi",roi)
#cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()