import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Grafik ayarları
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')
ax.set_facecolor('#1a1a1a')

# Çiçek için gerekli parametreler
t = np.linspace(0, 2*np.pi, 1000)
k = 12  # Yaprak sayısı

# Çiçeğin ana çizgisi
line, = ax.plot([], [], 'w-', linewidth=3)
# Çiçeğin iç kısmı
inner_circle, = ax.plot([], [], 'y-', linewidth=2)
# Çiçeğin dış halkası
outer_circle, = ax.plot([], [], 'w-', linewidth=1, alpha=0.5)

def init():
    line.set_data([], [])
    inner_circle.set_data([], [])
    outer_circle.set_data([], [])
    return line, inner_circle, outer_circle

def update(frame):
    # Ana yapraklar
    r = np.sin(k*t + frame/30) * 1.2
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    # İç daire (pistil)
    inner_r = 0.3 + 0.15 * np.sin(frame/15)
    inner_x = inner_r * np.cos(t)
    inner_y = inner_r * np.sin(t)
    
    # Dış halka
    outer_r = 1.5 + 0.1 * np.sin(frame/20)
    outer_x = outer_r * np.cos(t)
    outer_y = outer_r * np.sin(t)
    
    # Renk değişimi
    color = plt.cm.rainbow(frame/150)
    line.set_color(color)
    inner_circle.set_color('#FFD700')  # Altın sarısı
    outer_circle.set_color('#FF69B4')  # Açık pembe
    
    line.set_data(x, y)
    inner_circle.set_data(inner_x, inner_y)
    outer_circle.set_data(outer_x, outer_y)
    
    # Yıldız efektleri
    if frame % 5 == 0:
        star_x = np.random.uniform(-2.5, 2.5)
        star_y = np.random.uniform(-2.5, 2.5)
        star = patches.RegularPolygon((star_x, star_y), 5, 0.1, 
                                    color='white', alpha=0.7)
        ax.add_patch(star)
    
    return line, inner_circle, outer_circle

# Animasyon oluşturma
ani = FuncAnimation(fig, update, frames=300, init_func=init,
                    blit=True, interval=40)

# Başlık ve mesaj ekleme
plt.title('Senin İçin Özel Bir Çiçek 🌺', fontsize=24, pad=20, color='white')
plt.figtext(0.5, 0.05, '❤️ Seni Seviyorum ❤️', 
           fontsize=18, color='#FF69B4', ha='center')

# Arka plana yıldızlar ekleme
for _ in range(50):
    x = np.random.uniform(-3, 3)
    y = np.random.uniform(-3, 3)
    size = np.random.uniform(0.05, 0.2)
    star = patches.RegularPolygon((x, y), 5, size, 
                                color='white', alpha=0.5)
    ax.add_patch(star)

plt.show() 