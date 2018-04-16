# CAVE projectM

import viz
import vizshape
import vizinput
import vizinfo
import vizproximity

env = viz.addEnvironmentMap('sky.jpg')
viz.clearcolor(viz.SKYBLUE)

viz.mouse.setScale( 100, 2) # 100x movement speed, 2x rotation speed
viz.move([10,10,10]) # i think this sets the starting position to 10,10,10

karnak = viz.addChild('KarnakFBX.fbx')
viz.setMultiSample(4)
viz.go()
vizshape.addAxes()
info = vizinfo.InfoPanel("Let get started")




sensorAvatar1 = vizproximity.Sensor(vizproximity.Box([150,200,200],center=[3032.49878, 462.99207, -7990.59961]), source=karnak)
sensorAvatar2 = vizproximity.Sensor(vizproximity.Box([150,200,200],center=[11496.70117, 578.93695, -2284.39844]), source=karnak)
sensorAvatar3 = vizproximity.Sensor(vizproximity.Box([150,200,200],center=[4090.52271, 375.59061, -1435.92212]), source=karnak)
sensorAvatar4 = vizproximity.Sensor(vizproximity.Box([150,200,200],center=[6657.56494, 504.16730, -1794.23059]), source=karnak)

target = vizproximity.Target(viz.MainView)

manager = vizproximity.Manager()
manager.addSensor(sensorAvatar1)
manager.addSensor(sensorAvatar2)
manager.addSensor(sensorAvatar3)
manager.addSensor(sensorAvatar4)

manager.addTarget(target)

#Toggle debug shapes with keypress
vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

def EnterProximity(e):
	"""@args vizproximity.ProximityEvent()"""
	
	if e.sensor == sensorAvatar1:
		print "We made it to the stores!"
		info.setText('Stores')
	elif e.sensor == sensorAvatar2:
		print "We made it to Ramesses"
		info.setText('ramesses')
	elif e.sensor == sensorAvatar3:
		print "We made it to Taharqa!"
		info.setText('taharqa')
	elif e.sensor == sensorAvatar4:
		print "we made it to Amun!"
		info.setText('amun')
		
manager.onEnter(None,EnterProximity)

viz.collision(viz.ON) #user will collide with walls and stop moving
viz.MainView.gravity(0)
