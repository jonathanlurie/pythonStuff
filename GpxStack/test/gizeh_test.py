# Let's draw a red circle !
import gizeh
surface = gizeh.Surface(width=320, height=260) # in pixels
circle = gizeh.circle(r=300, xy= [40,40], fill=(1,0,0))
circle.draw(surface) # draw the circle on the surface
surface.write_to_png("circle.png") # export the surface as a PNG
