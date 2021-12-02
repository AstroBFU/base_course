import matplotlib.pyplot as pt

square = pt.Rectangle((1,1), 4, 4, fc = 'g', ec = 'black')
pt.gca().add_patch(square)
pt.axis('scaled')
pt.show()
