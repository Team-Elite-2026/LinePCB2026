import math, pcbnew



def between_two_numbers(a,b,num):
    return (min(a, b) <= num <= max(a, b))

def dist(p, center):
    distancesq = (p[0] - center[0])**2 + (p[1] - center[1])**2
    return abs(math.sqrt(distancesq))

def reverseAngle(center, outline):
    distance = math.sqrt((math.pow((center[0]-outline[0]),2)) + (math.pow((center[1]-outline[1]),2)))
    inverseX = outline[0]-center[0]
    inverseY = center[1]-outline[1]
    inverseX = inverseX/distance
    inverseY = inverseY/distance
    rVal = math.degrees(math.atan2(inverseX,inverseY))
    if(rVal < 0):
        rVal = rVal + 360
    return rVal

    
def place_circle(refdes):
    """
    Places components in a circle
    refdes: List of component references
    start_angle: Starting angle
    center: Tuple of (x, y) mils of circle center
    radius: Radius of the circle in mils
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
    """

    pcb = pcbnew.GetBoard()
    len_refdes = len(refdes)
    circles = []
    circles_sorted=[]
    lowest=0
    for d in pcb.GetDrawings():
      if d.GetLayerName() == 'Edge.Cuts' and d.GetShape() == 3:
        circles.append(d)
    len_circles = len(circles)
    for i in range(min(len_refdes, len_circles)):
       for j in range(i, min(len_refdes, len_circles)):
        if math.atan2(circles[i].GetCenter()[0]-100000000, circles[i].GetCenter()[1]-100000000)*180/math.pi > math.atan2(circles[j].GetCenter()[0]-100000000, circles[j].GetCenter()[1]-100000000)*180/math.pi:
           circles[i], circles[j] = circles[j], circles[i]
    for i in range(min(len_refdes, len_circles)):
      part = pcb.FindFootprintByReference(refdes[i])
      center = circles[i].GetCenter()
      part.SetPosition(center)

    pcbnew.Refresh()          
    print("Placement finished.")

def testing(refdes):
    """
    Places components in a circle
    refdes: List of component references
    start_angle: Starting angle
    center: Tuple of (x, y) mils of circle center
    radius: Radius of the circle in mils
    component_offset: Offset in degrees for each component to add to angle
    hide_ref: Hides the reference if true, leaves it be if None
    lock: Locks the footprint if true
    """

    pcb = pcbnew.GetBoard()
    len_refdes = len(refdes)
    circles = []
    circles_sorted=[]
    for d in pcb.GetDrawings():
      if d.GetLayerName() == 'Edge.Cuts' and d.GetShape() == 3:
        circles.append(d)
    len_circles = len(circles)
    for i in range(min(len_refdes, len_circles)):
       for j in range(i, min(len_refdes, len_circles)):
        if math.atan2(circles[i].GetCenter()[0]-100000000, circles[i].GetCenter()[1]-100000000)*180/math.pi > math.atan2(circles[j].GetCenter()[0]-100000000, circles[j].GetCenter()[1]-100000000)*180/math.pi:
           circles[i], circles[j] = circles[j], circles[i]
    for i in circles:
       print(math.atan2(i.GetCenter()[0]-100000000, i.GetCenter()[1]-100000000)*180/math.pi)
    return circles_sorted

