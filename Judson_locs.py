firstPylonSensor = vizproximity.Sensor(vizproximity.Box([1500,2500,1500],center=[-3107.70850, 0, 4795.99219]), source=karnak)
secondPylonSensor = vizproximity.Sensor(vizproximity.Box([1500,1500,1500],center=[181.26595, 1118.89758, 3177.29199]), source=karnak)
thirdPylonSensor = vizproximity.Sensor(vizproximity.Box([1500,3500,1500],center=[2536.80151, 1118.66260, 1955.30249]), source=karnak)
fourthPylonSensor = vizproximity.Sensor(vizproximity.Box([750,3500,750],center=[3540.21777, 501.35898, 1503.57483]), source=karnak)



manager.addSensor(firstPylonSensor)
manager.addSensor(secondPylonSensor)
manager.addSensor(thirdPylonSensor)
manager.addSensor(fourthPylonSensor)

elif e.sensor == firstPylonSensor or e.sensor == secondPylonSensor or e.sensor == thirdPylonSensor or e.sensor == fourthPylonSensor:
		print('First pylon!')
		info.setText('The pylons, or gateways in the temple represent the horizon, and as one moves further into the temple, the floor rises until it reaches the sanctuary of the god, giving the impression of a rising mound, like that during creation. The temple roof represented the sky and was often decorated with stars and birds. The columns were designed with lotus, papyrus, and palm plants in order to reflect the marsh-like environment of creation.')
		
		
		
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
	