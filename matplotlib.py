from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x =[4,2,3]
y=[1,5,6]
x1=[1,5,7]
y1=[3,5,1]
plt.bar(x,y,label='first',color='g')
plt.bar(x1,y1,label='second',color='r')
plt.xlabel("numbers")
plt.ylabel("frequency")
plt.title("experiment")
plt.legend()
plt.grid(True,color='k')
plt.show()
plt.close()