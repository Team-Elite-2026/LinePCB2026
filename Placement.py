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
    for d in pcb.GetDrawings():
      if d.GetLayerName() == 'Edge.Cuts' and d.GetShape() == 3:
        circles.append(d)
    len_circles = len(circles)
    for i in range(min(len_refdes, len_circles)):
       print(circles[i].getCenter())
    for i in range(min(len_refdes, len_circles)):
      part = pcb.FindFootprintByReference(refdes[i])
      center = circles[i].GetCenter()
      part.SetPosition(center)

    pcbnew.Refresh()          
    print("Placement finished.")


def testing(refdes):
    pcb = pcbnew.GetBoard()
    len_refdes = len(refdes)
    circles = []
    circles_sorted=[]
    
    for d in pcb.GetDrawings():
      if d.GetLayerName() == 'Edge.Cuts' and d.GetShape() == 3:
        circles.append(d)
    len_circles = len(circles)
    shortest=circles[0]
    shortest_length=0
    sortedList=[circles[0]]
    for i in range(min(len_refdes, len_circles)):
       if dist(shortest.GetCenter(), circles[i])
