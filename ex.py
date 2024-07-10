import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 검은 배경 이미지를 생성합니다.
image = np.zeros((200, 200, 3))

# anchor box의 정의 (width, height)
anchor_boxes = {
    "P3/8": [(1, 3), (6, 13), (9, 16)],
    "P4/16": [(30, 61), (62, 45), (59, 119)],
}

# Anchor box의 시작점 (xmin, ymin)
start_point = (0, 0)

# 이미지와 anchor box를 시각화합니다.
fig, ax = plt.subplots(1)
ax.imshow(image)

# 각 anchor box를 이미지 위에 그립니다.
for scale, boxes in anchor_boxes.items():
    for (width, height) in boxes:
        rect = patches.Rectangle(start_point, width, height, linewidth=1, edgecolor='r', facecolor='none', label=f'{scale} {width}x{height}')
        ax.add_patch(rect)

# 중복된 범례 제거
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# 그래프를 보여줍니다.
plt.show()
plt.show()