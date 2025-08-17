import pcbnew
pcb = pcbnew.GetBoard()
# To Find all Sensors
refdes_sensor = []
for i in range(1,49):
    for j in range(1,len(pcb.GetFootprints())):
        footprint = pcb.FindFootprintByReference("D" + str(j))
        if footprint is not None:
            
            for pad in footprint.Pads():
                netcode = pad.GetNet().GetNetname()
                if netcode == "Ch" + str(i):
                    refdes_sensor.append("D" + str(j))

# To Find all sensor resistors
refdes_sensorRes = []
for i in range(1,49):
    for j in range(1,len(pcb.GetFootprints())):
        footprint = pcb.FindFootprintByReference("R" + str(j))
        if footprint is not None:
            
            for pad in footprint.Pads():
                netcode = pad.GetNet().GetNetname()
                if netcode == "Ch" + str(i):
                    refdes_sensorRes.append("R" + str(j))

# To Find all LEDs
refdes_led = []
for j in range(1,len(pcb.GetFootprints())):
    footprint = pcb.FindFootprintByReference("D" + str(j))
    if footprint is not None:
        
        for pad in footprint.Pads():
            netcode = pad.GetNet().GetNetname()
            if netcode.find("D"+str(j)) != -1:
                refdes_led.append("D" + str(j))
            
# To Find all LED Resistors
### Must run LEDs search first before running this
refdes_ledRes = []
for j in range(1,len(pcb.GetFootprints())):
    footprint = pcb.FindFootprintByReference("R" + str(j))
    for i in refdes_led:
      if footprint is not None:
          for pad in footprint.Pads():
              netcode = pad.GetNet().GetNetname()
              if netcode.find(i) != -1:
                  refdes_ledRes.append("R" + str(j))