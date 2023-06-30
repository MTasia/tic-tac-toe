import cv2 as cv
import numpy as np


def matchTemp(img_rgb, img_rgb1, img_gray, tempCircle, tempCrosss):
    w, h = tempCrosss.shape[::-1]
    res = cv.matchTemplate(img_gray, tempCircle, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv.imwrite('res.png', img_rgb)

    res1 = cv.matchTemplate(img_gray, tempCrosss, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv.rectangle(img_rgb1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv.imwrite('res1.png', img_rgb1)


# def withSurf(img_rgb, img_gray,tempCrosss):
#     # Создание детектора и дескриптора SURF
#     surf = cv.xfeatures2d.SURF_create()
#
#     # Нахождение ключевых точек и дескрипторов на изображении и шаблоне
#     kp1, des1 = surf.detectAndCompute(img_gray, None)
#     kp2, des2 = surf.detectAndCompute(tempCrosss, None)
#
#     # Создание матчера и сопоставление дескрипторов
#     matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
#     matches = matcher.match(des1, des2)
#
#     # Выбор наилучших совпадений и фильтрация выбросов
#     good_matches = []
#     for m in matches:
#         if m.distance < 0.75 * max([match.distance for match in matches]):
#             good_matches.append(m)
#
#     # Нахождение матрицы преобразования между шаблоном и изображением
#     src_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     dst_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
#
#     # Получение размеров шаблона и его контура
#     h, w = tempCrosss.shape
#     template_contour = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#
#     # Преобразование контура шаблона с помощью матрицы преобразования
#     warped_template_contour = cv.perspectiveTransform(template_contour, M)
#
#     # Отображение контура шаблона на исходном изображении
#     img_matches = cv.drawMatches(tempCrosss, kp2, img_rgb, kp1, good_matches, None)
#     cv.imshow('img_matches', img_matches)


def main():
    img_rgb = cv.imread('../photo/tic3.jpg')
    img_rgb1 = cv.imread('../photo/tic3.jpg')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    img_gray = cv.blur(img_gray, (7, 7))


    tempCrosss = cv.imread('./temp/crossPattern.jpg', cv.IMREAD_GRAYSCALE)
    # tempCrosss = cv.blur(tempCrosss, (7, 7))

    tempCircle = cv.imread('./temp/circlePattern.jpg', cv.IMREAD_GRAYSCALE)
    # tempCircle = cv.blur(tempCircle, (7, 7))

    matchTemp(img_rgb, img_rgb1, img_gray, tempCircle, tempCrosss)
    # withSurf(img_rgb, img_gray,tempCrosss)



if __name__ == '__main__':
    main()
