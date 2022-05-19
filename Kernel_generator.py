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

import os
import numpy as np
from scipy import io as sio


def gaussian_2d(muu=0.0, sigma=1, start=-2, end=2, num=15, sf_x=1, sf_y=1, save=True, path=os.path.dirname(__file__), kname="kernel_default.mat"):
    """
    :param muu: Mean of gaussian.
    :param sigma: Standard deviation of gaussian.
    :param start: Start value for np.linespace().
    :param end: End value for np.linespace().
    :param num: Number of samples to generate. Default is 15. Must be non-negative.
    :param sf_x: Scale factor of downsampling to creat anisotropic gaussian.
    :param sf_y: Scale factor of downsampling to creat anisotropic gaussian.
    :param save: If True, save the kernel. Otherwise, not.
    :param path: Path to save dir "Kernels" and .mat file.
    :param kname: Name of generated kernel.
    :return: Generated kernel
    """
    x, y = np.meshgrid(np.linspace(start, end, num), np.linspace(start, end, num))
    dst = np.sqrt(x * x + y * y)
    # Calculating Gaussian array
    kernel = np.exp(-((dst - muu) ** 2 / (2.0 * sigma ** 2)))[::sf_x, ::sf_y]
    if save:
        if "Kernels" not in os.listdir(path):
            os.mkdir(os.path.join(path, "Kernels"))
        path = os.path.join(path, "Kernels")
        sio.savemat(os.path.join(path, kname), {"Kernel": kernel})

    return kernel
