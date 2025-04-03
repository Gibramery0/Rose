import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grafik ayarları
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')
ax.set_facecolor('black')

# Çiçek için gerekli parametreler
t = np.linspace(0, 2*np.pi, 1000)
k = 8  # Yaprak sayısı

# Çiçeğin ana çizgisi
line, = ax.plot([], [], 'w-', linewidth=2)
# Çiçeğin iç kısmı
inner_circle, = ax.plot([], [], 'y-', linewidth=2)

def init():
    line.set_data([], [])
    inner_circle.set_data([], [])
    return line, inner_circle

def update(frame):
    # Dış çiçek yaprakları
    r = np.sin(k*t + frame/20) * 0.8
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # İç daire
    inner_r = 0.2 + 0.1 * np.sin(frame/10)
    inner_x = inner_r * np.cos(t)
    inner_y = inner_r * np.sin(t)
    
    # Renk değişimi
    color = plt.cm.rainbow(frame/100)
    line.set_color(color)
    inner_circle.set_color('yellow')
    
    line.set_data(x, y)
    inner_circle.set_data(inner_x, inner_y)
    
    return line, inner_circle

# Animasyon oluşturma
ani = FuncAnimation(fig, update, frames=200, init_func=init,
                    blit=True, interval=30)

# Başlık ve mesaj ekleme
plt.title('Senin İçin Özel Bir Çiçek 🌸', fontsize=20, pad=20, color='white')
plt.figtext(0.5, 0.05, '❤️ Seni Seviyorum ❤️', 
           fontsize=16, color='pink', ha='center')

plt.show() 