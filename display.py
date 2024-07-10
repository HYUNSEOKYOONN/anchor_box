import cv2
import numpy as np

"""
#Edge detection

img = cv2.imread("2.PNG")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(img_gray, (5, 5), 0)

edges = cv2.Canny(blurred_image, 30, 100)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    crack_area = cv2.contourArea(contour)
    if crack_area > 50:  # 크랙 크기에 따른 임계값 설정
        print("Crack detected")
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

cv2.imshow("Display Image", img)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""


#Bright
# 이미지 불러오기
img = cv2.imread('7.PNG')

# 이미지 전처리
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray',img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 segmentation 수행
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 작은 영역을 제거할 최소 크기 지정
min_area = 100

# 작은 영역 제거
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area:
        filtered_contours.append(contour)

contours = filtered_contours

label_image = np.zeros_like(img)

mean_values = []

for i, contour in enumerate(contours):
    # 객체가 포함된 영역의 경계선 추출
    x, y, w, h = cv2.boundingRect(contour)
    # 객체가 포함된 영역의 밝기 값을 계산
    roi = img_gray[y:y+h, x:x+w]
    mean = cv2.mean(roi)[0]
    mean_values.append(mean)
    # 밝기 값
    print(f'Object {i}: mean={mean}')
    # 평균 밝기와 threshold 비교
    threshold = sum(mean_values) / len(mean_values)
    if ((mean - threshold > 30) or (mean - threshold < -30)):
        result = 'NO'
    else:
        result = 'OK'
    
    # 레이블링 결과에 불량 여부 표시 (Segmentation 이미지)
    cv2.drawContours(label_image, contours, i, (0, 0, 255), -1)
    cv2.putText(label_image, result, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 레이블링 결과에 불량 여부 표시 (그레이 이미지)
    cv2.putText(img_gray, result, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128), 2)

print(f'threshold: {threshold}')




dst = cv2.Canny(img_gray, threshold-30, threshold+30 )
cv2.imshow('gray',img_gray)
cv2.imshow('labe',label_image)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

