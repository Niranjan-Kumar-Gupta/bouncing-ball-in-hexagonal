from visual import*
import numpy as np

scene.background = color.white

r=2
hexa_list = []
dtheta = np.pi/3
theta = 0

while(theta<=2*np.pi):
    hexa_list.append(vector(r*cos(theta),r*sin(theta),0))
    theta += dtheta

print(hexa_list)

hexa_curve = curve(pos=hexa_list,color = color.red)

sphere1 = sphere(pos=vector(0,0,0),radius=0.03,color=color.red)
sphere2 = sphere(pos=vector(1,0,0),radius=0.03,color=color.red,make_trail=True,retain=0)

hit_direction = vector(0.4,0.9,0)


dt = 0.009

while(True):
    rate(500)
    
    magnitude = mag(sphere2.pos)
    
    m = degrees(math.atan(hit_direction.y/hit_direction.x))
    n = (((r*np.cos(np.pi/6)-1)*np.sin(m))**2 + (r*np.cos(np.pi/6))**2)**0.5
    
    if magnitude + sphere2.radius >= n:
        hit_direction -= 2*sphere2.pos*dot(sphere2.pos,hit_direction)/magnitude**2
    sphere2.pos += hit_direction*dt
    


