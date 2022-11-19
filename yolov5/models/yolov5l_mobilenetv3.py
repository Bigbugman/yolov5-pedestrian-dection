"""
Reference: https://blog.csdn.net/weixin_44808161/article/details/125759652
"""

# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# Parameters
nc: 80  # number of classes
depth_multiple: 1.0  # model depth multiple
width_multiple: 1.0  # layer channel multiple
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [[-1, 1, conv_bn_hswish, [16, 2]],                 # 0-p1/2
   [-1, 1, MobileNet_Block, [16,  16, 3, 2, 1, 0]],  # 1-p2/4
   [-1, 1, MobileNet_Block, [24,  72, 3, 2, 0, 0]],  # 2-p3/8
   [-1, 1, MobileNet_Block, [24,  88, 3, 1, 0, 0]],  # 3-p3/8
   [-1, 1, MobileNet_Block, [40,  96, 5, 2, 1, 1]],  # 4-p4/16
   [-1, 1, MobileNet_Block, [40, 240, 5, 1, 1, 1]],  # 5-p4/16
   [-1, 1, MobileNet_Block, [40, 240, 5, 1, 1, 1]],  # 6-p4/16
   [-1, 1, MobileNet_Block, [48, 120, 5, 1, 1, 1]],  # 7-p4/16
   [-1, 1, MobileNet_Block, [48, 144, 5, 1, 1, 1]],  # 8-p4/16
   [-1, 1, MobileNet_Block, [96, 288, 5, 2, 1, 1]],  # 9-p5/32
   [-1, 1, MobileNet_Block, [96, 576, 5, 1, 1, 1]],  # 10-p5/32
   [-1, 1, MobileNet_Block, [96, 576, 5, 1, 1, 1]],  # 11-p5/32
  ]
 
# YOLOv5 v6.0 head
head:
  [[-1, 1, Conv, [256, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 8], 1, Concat, [1]],  # cat backbone P4
   [-1, 1, C3, [256, False]],  # 15
 
   [-1, 1, Conv, [128, 1, 1]],
   [-1, 1, nn.Upsample, [None, 2, 'nearest']],
   [[-1, 3], 1, Concat, [1]],  # cat backbone P3
   [-1, 1, C3, [128, False]],  # 19 (P3/8-small)
 
   [-1, 1, Conv, [128, 3, 2]],
   [[-1, 16], 1, Concat, [1]],  # cat head P4
   [-1, 1, C3, [256, False]],  # 22 (P4/16-medium)
 
   [-1, 1, Conv, [256, 3, 2]],
   [[-1, 12], 1, Concat, [1]],  # cat head P5
   [-1, 1, C3, [512, False]],  # 25 (P5/32-large)
 
   [[19, 22, 25], 1, Detect, [nc, anchors]],  # Detect(P3, P4, P5)
  ]
