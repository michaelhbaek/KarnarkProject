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
info = vizinfo.InfoPanel("Let's get started")




sensorAvatar1 = vizproximity.Sensor(vizproximity.Box([3170,160,3051],center=[3123.10181, 160.43307, -7414.27441]), source=karnak)
sensorAvatar2 = vizproximity.Sensor(vizproximity.Box([749,741,1439],center=[11489.54081, 447.63779, -2581.69801]), source=karnak)
sensorAvatar3 = vizproximity.Sensor(vizproximity.Box([1400,422,1400],center=[3854.15869, 375.59055, -1661.75696]), source=karnak)
sensorAvatar4 = vizproximity.Sensor(vizproximity.Box([8555,811,6949],center=[6046.80322, 334.64569, 189.79089]), source=karnak)
firstPylonSensor = vizproximity.Sensor(vizproximity.Box([8555,811,6949],center=[6046.80322, 334.64569, 189.79089]), source=karnak)
#[-3107.70850, 1130.22156, 4795.99219]
#secondPylonSensor: [181.26595, 1118.89758, 3177.29199]
#third: [2536.80151, 1118.66260, 1955.30249]
#fourth: [3540.21777, 501.35898, 1503.57483]


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
		info.setText('Ramesses II built a small temple called "Amun-Ra, Ramesses II, who-hears-prayers," just east of the unique obelisk. The presence of reused column drums of Thutmose III in the temple suggests\nthat he rebuilt a Thutmoside shrine on the same area. The temple at this time consisted of a small mud brick gateway leading into a pillared hall. The rear of the hall had two doorways and a central false door.\nThe doorways led out into a covered portico at the base of the unique obelisk. \nhe small temple may have functioned similarly to the Contra Temple of Thutmose III in that average Egyptians could enter the temple complex here and pray to Amun-Ra.')
	elif e.sensor == sensorAvatar3:
		print "We made it to Taharqa!"
		info.setText('This structure looks not unlike an almost square mastaba style tomb with a torus at each corner but no doors on any of its outer walls. A study of the east wall which is composed of blocks that are at times scored and sometimes\n unfinished, suggests that there existed at this location an access ramp that lead to the terrace of the structure. Therefore, one would have had to cross the terrace from east to west to reach a staircase that then descended into the\nchambers located in the northwest corner of the monument. The direction of the walk from east to west would be in conformity with that of the king represented on the north facade of the building, but opposite to the general advance\nof the king inside the temple.'
						'On the outside northern facade of this building we find several interesting scenes. Here, the king is purified by a double stream made up of the ankh and the was (Life and Power) that falls\nin a dome around him. His two open hands show the palm of one and the back side of the other. Two falcons cross their wings over the kings chest under his three-row user necklace.\nAs is the Nubian style, the musculature of the kings legs is prominent. Here, the cartouche of Taharqa has been etched out and replaced by that of Psamtik II.')
	elif e.sensor == sensorAvatar4:
		print "we made it to Amun!"
		info.setText('The main temple of Amun-Re had two axes, one that went north/south and the other that extended east/west. The southern axis continued towards the temple of Luxor and was connected by an avenue of ram-headed sphinxes.')
		
def LeaveProximity(e):
	"""@args vizproximity.ProximityEvent()"""
	
	if e.sensor == sensorAvatar1:
		print "We made it to the stores!"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatar2:
		print "We made it to Ramesses"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatar3:
		print "We made it to Taharqa!"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatar4:
		print "we made it to Amun!"
		info.setText('Lets get started')
		
manager.onEnter(None,EnterProximity)
#manager.onExit(None,LeaveProximity)
viz.collision(viz.ON) #user will collide with walls and stop moving
viz.MainView.gravity(0)
