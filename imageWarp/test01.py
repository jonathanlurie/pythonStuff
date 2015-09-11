from PIL import Image


nyc = Image.open("grid.png")
print(nyc.format, nyc.size, nyc.mode)

mesh = []


q1S = (0, 0, 0, 500, 600, 600, 500, 0)
q1T = (0, 0, 600, 600)

q2S = (500, 0, 500, 500, 1000, 500, 1000, 0)
q2T = (500, 0, 1000, 500)

q3S = (0, 500, 0, 1000, 500, 1000, 500, 500)
q3T = (0, 500, 500, 1000)

q4S = (500, 500, 500, 1000, 1000, 1000, 1000, 500)
q4T = (400, 500, 1000, 1000)


mesh.append((q1T, q1S))
#mesh.append((q2T, q2S))
#mesh.append((q3T, q3S))
#mesh.append((q4T, q4S))



biliFilter = Image.BILINEAR
bicuFilter = Image.BICUBIC

warpedNYC = nyc.transform( nyc.size, Image.MESH, mesh, bicuFilter)


warpedNYC.save("grid_out.png")


'''
mesh.append(

((x0, y0, x1, y1), (last_projected_x, last_projected_y,x0, y1,x1, y1,projected_x, projected_y,),)

            )


            last_projected_x, last_projected_y = projected_x, projected_y
'''
