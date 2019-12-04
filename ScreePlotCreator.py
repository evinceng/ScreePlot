# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

#hard code the number of components and the eigenvalues.
numberOfComponents = 13
eigenValues = [16.701, 4.654, 2.546, 1.927, 1.844, 1.684, 1.503, 1.400, 1.288, 1.198, 1.104, 1.059 , 1.020]
                              

fig = plt.figure(figsize=(8,5))
componentArray = np.arange(numberOfComponents) + 1
plt.plot(componentArray, eigenValues, 'bo-', linewidth=2)
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"
#plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Eigenvalue')

leg = plt.legend(['Eigenvalues from FA'], loc='best', borderpad=0.3, 
                 shadow=False, prop=matplotlib.font_manager.FontProperties(size='small', family='Times New Roman'),
                 markerscale=0.4)
leg.get_frame().set_alpha(0.4)
plt.show()
#save figure
currentTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
fig.savefig("Figs\\" + currentTime + "_ScreePlot.pdf")
