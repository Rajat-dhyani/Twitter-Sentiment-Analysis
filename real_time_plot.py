import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('ggplot')



fig = plt.figure()
axs = fig.add_subplot(1,1,1)

    
def animate(i):
    data = open("aadhar_data.csv","r").read()
    lines = data.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0
    
    for line in lines[-100:-1]:
        x += 1
        polarity = line.split(',')[2]
        print ('polarity:', polarity)
        
    
        if polarity != ' ':
            point = float(polarity)
            print(point)

            if (point>0.0):
                y += point
            elif (point < 0.0):
                y -= abs(point)
            else:
                y = 0
            xar.append(x)
            yar.append(y)
    axs.clear()
    axs.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
    
















            
