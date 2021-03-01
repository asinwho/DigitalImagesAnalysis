# -*- coding: utf-8 -*-
"""l2_imkhasina.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nibc5_ADkuafVx8AsXGXtS8UYFPrRPRB
"""
import numpy as np
from PIL import Image
import itertools  
import matplotlib.pyplot as plt
%matplotlib inline

#Считывание изображения
img = Image.open('1.jpg')
img = img.convert('RGB')
colors = img.getcolors(maxcolors=1000000)
colors=sorted(colors, reverse=True)
#Три самых используемых цвета в изображении
a=colors[:3]
f,s,t =a
for amount, color in a:
  print(f'{color} RGB repeats {amount} times (as pixels)')
print('')
#Для вывода палитры (топ-3 самых используемых)
f1,f2=f
s1,s2=s
t1,t2=t
print('Palette:')
palette=[f2,s2,t2]
palette = np.array(palette)[np.newaxis, :, :]
plt.imshow(palette);
plt.axis('off');
plt.show();
####
#Output:
#(63, 138, 169) RGB repeats 386699 times (as pixels)
#(245, 191, 155) RGB repeats 229549 times (as pixels)
#(86, 24, 25) RGB repeats 208538 times (as pixels)
####

#Вариант 2 с попиксельным проходом вручную (вместо метода getcolors())
#Проблема с тем что некоторые цвета могут разбиваться(?) и неправильно считаться

import numpy as np
from PIL import Image
import itertools  
import matplotlib.pyplot as plt
%matplotlib inline
from collections import defaultdict

img = Image.open('1.jpg')
img = img.convert('RGB')
by_color = defaultdict(int)
for pixel in img.getdata():
  by_color[pixel] += 1
out = (dict(itertools.islice(by_color.items(), 3)))
f,s,t=(out)
print(f, s, t)
palette=[f,s,t]
palette = np.array(palette)[np.newaxis, :, :]
plt.imshow(palette);
plt.axis('off');
plt.show();
