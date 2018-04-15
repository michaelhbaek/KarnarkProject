# CAVE project

import viz
import vizshape
vizshape.addAxes()

viz.setMultiSample(4)
env = viz.addEnvironmentMap('sky.jpg')
viz.clearcolor(viz.SKYBLUE)

viz.go()

karnark = viz.addChild('KarnakFBX.fbx')

viz.mouse.setScale( 100, 2) # 100x movement speed, 2x rotation speed
viz.move([10,10,10]) # i think this sets the starting position to 10,10,10
plant = viz.addChild('plant.osgb') # just wanted to see if we can see this - i cant but maybe you guys can?
plant.setPosition([4,0,4])
viz.collision(viz.ON) #user will collide with walls and stop moving