import cv2
from to_tree import hierarchy_to_tree
from bfs import bfs
from config import config

img_str, ksize, blocksize, C = config('6')

image = cv2.imread(img_str)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_image, ksize, 0)
thresh_image = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, blocksize, C)
contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# hierarchy[0][i][0] - shows next contour, hierarchy[0][i][1] - previous contour,
# hierarchy[0][i][2] - parent contour, hierarchy[0][i][3] - child of contour

tree = hierarchy_to_tree(hierarchy[0])

bfs_first = bfs(tree, -1)
deepest = bfs_first[-1]
bfs_second = bfs(tree, deepest)
furthest = bfs_second[-1]

if deepest == -1:
    deepest = 0
if furthest == -1:
    furthest = 0

# for i, contour in enumerate(contours):
#     cv2.drawContours(image, contour, 0, (255, 0, 0), 4)

cv2.drawContours(image, [contours[furthest]], 0, (0, 0, 255), 4)
cv2.drawContours(image, [contours[deepest]], 0, (0, 255, 0), 4)

cv2.imshow("output", cv2.resize(image, (1200, 800)))
cv2.waitKey(0)

