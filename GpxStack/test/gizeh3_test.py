# Let's draw a red circle !
import gizeh


surface = gizeh.Surface(width=320, height=260) # in pixels
circle = gizeh.circle(r=300, xy= [40,40], fill=(1,0,0))
circle.draw(surface) # draw the circle on the surface


points = []
point1 = [10, 10]
point2 = [20, 10]
point3 = [20, 20]
point4 = [50, 40]

points.append(point1)
points.append(point2)
points.append(point3)
points.append(point4)

polyline = gizeh.polyline(points, stroke=[0,0,0], stroke_width=1)
polyline.draw(surface)

surface.write_to_png("circle.png") # export the surface as a PNG
