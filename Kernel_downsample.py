#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Kernel_generator.py
@Contact :   moyanxuanliu@126.com
@License :   (C)Copyright 2021-2022, ZongfangLiu

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/24 22:55   zfliu      1.0         None
'''
from scipy import ndimage


# 保证像素数可以整除
def modcrop(im, sf):
    '''
    Args:
        im: numpy array, h x w x c
        sf: scale factor
    '''
    h, w = im.shape[:2]
    return im[:h - h % sf, :w - w % sf, ]


def degradation(im_HR, scale_factor, kernel, convolve='False', padding_mode='mirror'):
    '''
    Args:
        im_HR: numpy array, h x w x c, [0, 1], float
        sf: int
        convolve: bool, if Ture convolve else correlate
        padding_mode: str, 'mirror' or 'warp'

    '''
    if im_HR.ndim == 2:
        im_HR = im_HR[:, :, None]
    im_HR = modcrop(im_HR, scale_factor)
    # blur
    if convolve:
        im_blur = ndimage.convolve(im_HR, kernel[:, :, None], mode=padding_mode)
    else:
        im_blur = ndimage.correlate(im_HR, kernel[:, :, None], mode=padding_mode)
    # downsampling
    im_LR = im_blur[0::scale_factor, 0::scale_factor, ]

    return im_LR.squeeze()