import cv2

image = cv2.imread("images.png",cv2.IMREAD_COLOR) ## 컬러 이미지 불러오기
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  ## 이미지를 흑백으로 변환

cv2.imshow("color", image) ## 컬러이미지 보여주기
cv2.imshow("Gray", gray_image) ##이미지를 흑백이미지로 변환해서 보여주기
cv2.waitKey()
cv2.destroyAllWindows()
