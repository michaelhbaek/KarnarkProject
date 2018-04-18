# CAVE project

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




sensorAvatar1 = vizproximity.Sensor(vizproximity.Box([3170,160,3051],center=[3123.10181, 160.43307, -7414.27441]), source=karnak)
sensorAvatar2 = vizproximity.Sensor(vizproximity.Box([749,741,1439],center=[11489.54081, 447.63779, -2581.69801]), source=karnak)
sensorAvatar3 = vizproximity.Sensor(vizproximity.Box([1400,422,1400],center=[3854.15869, 375.59055, -1661.75696]), source=karnak)
sensorAvatar4 = vizproximity.Sensor(vizproximity.Box([8555,811,6949],center=[6046.80322, 334.64569, 189.79089]), source=karnak)

# Michael's additions
TempleOfKhonsCenter = [-6856.85400, 80.60259, -5399.07031]
TempleOfKhonsBox = [2189.75,101,2746]
sensorAvatarTempleOfKhons = vizproximity.Sensor(vizproximity.Box( TempleOfKhonsBox , center= TempleOfKhonsCenter ), source=karnak)

KioskOfSethosCenter = [-1768.67249, 303.00790, 5457.22656]
KioskOfSethosBox = [942,0,888]
sensorAvatarKioskOfSethos = vizproximity.Sensor(vizproximity.Box( KioskOfSethosCenter , center= KioskOfSethosBox ), source=karnak)

GreatHallSethosRamessesCenter = [1365.27637, 1083.85828, 2679.91406]
GreatHallSethosRamessesBox = [4035, 240, 4852]
sensorAvatarGreatHallSethosRamesses = vizproximity.Sensor(vizproximity.Box( GreatHallSethosRamessesBox , center= GreatHallSethosRamessesCenter ), source=karnak)

OpetTempleCenter = [-9280.32129, 307.08664, -5449.44775]
OpetTempleBox = [939, 312, 1033]
sensorAvatarOpetTemple = vizproximity.Sensor(vizproximity.Box( OpetTempleBox  , center= OpetTempleCenter ), source=karnak)

HallOfThutmoseCenter = [8382.30859, 683.46454, -988.87549]
HallOfThutmoseBox = [2618, 170, 3373]
sensorAvaterHallOfThutmose = vizproximity.Sensor(vizproximity.Box( HallOfThutmoseBox  , center= HallOfThutmoseCenter ), source=karnak)
#end Michael's Edits

target = vizproximity.Target(viz.MainView)

manager = vizproximity.Manager()
manager.addSensor(sensorAvatar1)
manager.addSensor(sensorAvatar2)
manager.addSensor(sensorAvatar3)
manager.addSensor(sensorAvatar4)
manager.addSensor(sensorAvatarGreatHallSethosRamesses) #Michael's sensors
manager.addSensor(sensorAvatarKioskOfSethos)
manager.addSensor(sensorAvatarOpetTemple)
manager.addSensor(sensorAvatarTempleOfKhons)
manager.addSensor(sensorAvaterHallOfThutmose) # Michael's last sensor


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
		info.setText('The main temple of Amun-Re had two axes—one that went north/south and the other that extended east/west. The southern axis continued towards the temple of Luxor and was connected by an avenue of ram-headed sphinxes.')
	#Michael's additions
	elif e.sensor == sensorAvatarGreatHallSethosRamesses:
		print "We made it to the Great Hypostyle Hall of Sethos II"
		info.setText('The Great Hypostyle Hall of Sethos II spans an area of 5,000 m^2. The roof, when unfallen, was supported by 134 columns in 16 rows. It was initially designed by Hatshepsut but the Hall was built entirely by Seti I. Over the course of XXX years, Ramesses II, Ramesses III, Ramesses IV, and Ramesses VI added to this hall. ')
	elif e.sensor == sensorAvatarKioskOfSethos:
		print "We made it to the Kiosk of Sethos II"
		info.setText('Taharqa was the fourth king of the Twenty-fifth Dynasty and also king of his native Kush; located in Northern Sudan. The remains of this huge kiosk, built by 25th Dynasty pharaoh Taharqa (690-664 B.C.) originally consisted of ten twenty-one meter high papyrus columns linked by a low screening wall. Today there is only one great column still standing. It is believed that it was a barque chapel (or Station) although some Egyptologists think it may have been used in ritual activities to join with the sun')
	elif e.sensor == sensorAvatarOpetTemple:
		print "We made it to the Opet Temple "
		info.setText('In tribute to the hippopotamus goddess of fertility, Opet, the Temple of Opet was created. This building is one of the last cult buildings erected at Karnak.')
	elif e.sensor == sensorAvatarTempleOfKhons:
		print "We made it to the Temple of Khons"
		info.setText('Originally constructed by Ramesses III, the Temple of Khonsu was created for the moon god Khonsu. Khonsu was believed to have the ability to drive out evil spirits. In one instance, Rameses II sent a statue of Khonsu to a friendly Syrian king in order to cure his daughter of an illness')
	elif e.sensor == sensorAvaterHallOfThutmose:
		print "We made it to the Festival Hall of Thutmose III"
		info.setText('Thutmose III named it the “Most Splendid of Monuments”. Its entrance was originally flanked by two statues of the king wearing a festival costume. The roof is supported on the outside by thirty-two square pillars, while the inside is supported by tent pole style columns symbolising the military tent that Thutmose would have used on campaign. On the northeast end is a stairway leading to a room called the “Chamber of the Clepsydras”. Clepsydras were water clocks made from a stone vessel with a tiny hole at the bottom which allowed water to drip at a constant rate. The passage of hours could be measured from marks spaced at different levels. The priests at Karnak temple used them at night to determine the correct hour to perform religious rites.')
	#end Michael's edits
	
	
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
	#Michael's additions
	elif e.sensor == sensorAvatarGreatHallSethosRamesses:
		print "We made it to the Great Hypostyle Hall of Sethos II"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatarKioskOfSethos:
		print "We made it to the Kiosk of Sethos II"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatarOpetTemple:
		print "We made it to the Opet Temple "
		info.setText('Lets get started')
	elif e.sensor == sensorAvatarTempleOfKhons:
		print "We made it to the Temple of Khons"
		info.setText('Lets get started')
	elif e.sensor == sensorAvatarHallOfThutmose:
		print "We made it to the Festival Hall of Thutmose III"
		info.setText('Lets get started')
	#end Michael's edits
	
manager.onEnter(None,EnterProximity)
#manager.onExit(None,LeaveProximity)
viz.collision(viz.ON) #user will collide with walls and stop moving
viz.MainView.gravity(0)