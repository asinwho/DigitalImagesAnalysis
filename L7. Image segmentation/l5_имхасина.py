# -*- coding: utf-8 -*-
"""L5_Имхасина.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WU-OqcQzEHkROeBJt3eO7YynOshY-9vd
"""

import numpy as np
import scipy
import cv2
import matplotlib.pyplot as plt
from pandas import Series
from google.colab.patches import cv2_imshow
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import skimage
from skimage import io

def image_show(image, nrows=1, ncols=1):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols)
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

def uS(img):
  k,l=img.shape
  u=np.ndarray(img.shape)
  for i in range(k-1):
    for j in range(l-1):
      u[i][j]=max(img[i][j]+1,max(img[i-1][j],img[i][j-1],img[i+1][j],img[i][j+1]))
  return u

def bS(img):
  k,l=img.shape
  b=np.ndarray(img.shape)
  for i in range(k-1):
    for j in range(l-1):
      b[i][j]=min(img[i][j]-1,min(img[i-1][j],img[i][j-1],img[i+1][j],img[i][j+1]))
  return b

def getVol(u,b):
  k,l=u.shape
  vol=0.0
  for i in range(k):
    for j in range(l):
      vol=vol+u[i][j]-b[i][j]
  return vol

def getA(gImage):
  u1=uS(gImage)
  u2=uS(u1)

  b1=bS(gImage)
  b2=bS(b1)

  vol1=getVol(u1,b1)
  vol2=getVol(u2,b2)

#формула 22
  A_2=(vol2-vol1)/(2)
  return A_2

# used for finding out A border
def calc_stats(l):
    s = Series(A_s)
    return s.describe()

def segm(img):
    segmented_img = np.full(img.shape, 255)

    A_s = []

    for i in range(0, img.shape[0], 5):
        for j in range(0, img.shape[1], 5):
            A = getA(img[i:i + 5, j: j + 5])
            A_s.append(A)
            if A >= 1000:
                segmented_img[i:i + 5,
                j:j + 5].fill(0)

    cv2.imwrite('Result_3.png', segmented_img)


originalImage = cv2.imread('3.png')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
segm(grayImage)
text = io.imread('Result_3.png')
image_show(text)
