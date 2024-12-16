import cv2
img = cv2.imread("image.jpg")
img = cv2.resize(img, (740,480))
cv2.imshow("Result Image", img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
gray_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow("Result Image", gray_img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
invert_img = cv2.bitwise_not(src=gray_img)
cv2.imshow("Result Image", invert_img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
smooth_img = cv2.medianBlur(src=invert_img, ksize=37)
cv2.imshow("Result Image", smooth_img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
invt_smooth_img = cv2.bitwise_not(smooth_img)
cv2.imshow("Result Image", invt_smooth_img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
sketch_img = cv2.divide(gray_img, invt_smooth_img, scale=220)
cv2.imshow("Result Image", sketch_img)
# Press any key to exit
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("result.jpg", sketch_img)