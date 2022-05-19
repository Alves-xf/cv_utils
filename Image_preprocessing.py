#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Image_preprocessing.py    
@Contact :   moyanxuanliu@126.com
@License :   (C)Copyright 2021-2022, ZongfangLiu

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/8 16:32   zfliu      1.0         None
'''
import numpy as np

def imadjust(img, in_range=[0, 1], out_range=[0, 1], gamma=1):
    # 默认参数和matlab中的默认参数相同

    low_in, high_in = in_range[0], in_range[1]
    low_out, high_out = out_range[0], out_range[1]
    # 百分比截断
    p1, p99 = np.percentile(img, (1, 99))
    img_out = np.clip(img, p1, p99)

    # 映射 参考https://stackoverflow.com/questions/39767612/what-is-the-equivalent-of-matlabs-imadjust-in-python
    img_out = (((img_out - low_in) / (high_in - low_in)) ** gamma) * (high_out - low_out) + low_out

    return img_out