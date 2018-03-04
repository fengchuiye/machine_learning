'''
test Colaboratory
https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=xqrc5C-IaA5J
'''
import tensorflow as tf
import numpy as np

#测试
print("Hello, Colaboratory!");


#测试tf，np
with tf.Session():
    input1 = tf.constant(1.0, shape=[2,3])
    input2 = tf.constant(np.reshape(np.arange(1.0, 7.0, dtype=np.float32),(2,3)))
    output = tf.add(input1,input2)
    result = output.eval()
    print(result)

#测试matplotlib
import matplotlib.pyplot as plt
x = np.arange(20)
y = list(map(lambda x: x + np.random.randn(1),x))
print(x)
print(y)
a,b = np.polyfit(x,y,1)
print(a)
print(b)
plt.plot(x,y,'o',np.arange(20),a*np.arange(20)+b,'-')

#import time

#time.sleep(10)

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2
 
x = np.linspace(0, 3, 100)
for i in range(5):
    plt.figure(1)  #❶ # 选择图表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i*x))
 
plt.show()


