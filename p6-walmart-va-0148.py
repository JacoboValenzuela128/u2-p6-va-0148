import matplotlib.pyplot as plt 
import numpy as np 
#Arath Valenzuela NC:0148 (27/10/26)

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos, precio)
plt.show()

# Personalizar grafica 
plt.plot(cant_productos, precio,
         color = 'red', 
         marker = 'o',
         linestyle = 'dashed',
         linewidth = 2,
         markersize = 12)
plt.title("Ventas de Walmart (NC:0148)")
plt.xlabel("Precios")
plt.ylabel("Cant de productos")

plt.show()
