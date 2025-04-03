import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Çiçeğin parametreleri
t = np.linspace(0, 2*np.pi, 1000)
k = 5  # Yaprak sayısı

# Grafik ayarları
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Çiçeğin çizimi
line, = ax.plot([], [], 'r-', linewidth=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    # Çiçeğin animasyonlu hareketi
    r = np.sin(k*t + frame/10)
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # Renk değişimi
    color = plt.cm.hsv(frame/100)
    line.set_color(color)
    line.set_data(x, y)
    return line,

# Animasyon oluşturma
ani = FuncAnimation(fig, update, frames=100, init_func=init,
                    blit=True, interval=50)

# Başlık ekleme
plt.title('Senin İçin Bir Çiçek ❤️', fontsize=16, pad=20)

plt.show() 