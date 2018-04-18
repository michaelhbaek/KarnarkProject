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
		