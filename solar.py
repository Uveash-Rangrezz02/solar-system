import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg

# Load the background image
bg_img = mpimg.imread(r'C:\vs code\python\solar system\space_background.jpg')

# Planet data: [orbital_radius, orbital_period, color, size]
planets = {
    'Mercury': [50, 0.24, 'darkgray', 150],
    'Venus': [100, 0.62, 'gold', 200],
    'Earth': [150, 1.00, 'deepskyblue', 250],
    'Mars': [200, 1.88, 'red', 220],
    'Jupiter': [350, 11.86, 'orange', 350],
    'Saturn': [500, 29.46, 'khaki', 330],
    'Uranus': [650, 84.01, 'lightblue', 300],
    'Neptune': [800, 164.79, 'blue', 300]
}

# Create figure and background
fig = plt.figure(figsize=(14, 14))
fig.patch.set_facecolor('black')
bg_ax = fig.add_axes([0, 0, 1, 1], zorder=0)
bg_ax.imshow(bg_img, aspect='auto')
bg_ax.axis('off')

# 3D axis
ax = fig.add_subplot(111, projection='3d', zorder=1)
ax.set_facecolor('none')
ax.set_axis_off()
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
ax.set_zlim(-400, 400)

# Draw the Sun
ax.scatter(0, 0, 0, color='yellow', s=2000)

# Create planets and labels
planet_objects = {}
planet_labels = {}

for name, (radius, _, color, size) in planets.items():
    point, = ax.plot([], [], [], 'o', color=color, markersize=size / 20)
    label = ax.text(0, 0, 0, name, color='white', fontsize=10)
    planet_objects[name] = point
    planet_labels[name] = label

# Draw orbital paths
theta = np.linspace(0, 2 * np.pi, 150)
for radius, _, color, _ in planets.values():
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(theta)
    ax.plot(x, y, z, linestyle='dotted', color='white', alpha=0.2)

# Animation function
def animate(frame):
    time = frame * 0.05
    for name, (radius, period, _, _) in planets.items():
        angle = 2 * np.pi * (time / period)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = radius * 0.15 * np.sin(angle / 2)

        planet_objects[name].set_data([x], [y])
        planet_objects[name].set_3d_properties([z])

        # Update label position
        planet_labels[name].set_position((x + 20, y + 20))
        planet_labels[name].set_3d_properties(z + 20)

    ax.view_init(elev=20, azim=frame * 0.3)
    return list(planet_objects.values()) + list(planet_labels.values())

# Run the animation
ani = FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)

plt.show()
