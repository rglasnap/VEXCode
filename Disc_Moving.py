myVariable = 0
distance_horizontal = 0
disc_found = False
search_start = [0 for x in range(2)]
curPosition = [0 for x in range(2)]
derpTesting = [0 for x in range(2)]

def return_to_search():
    global myVariable, distance_horizontal, disc_found, search_start, curPosition, derpTesting
    derpTesting[1 - 1] = curPosition[1 - 1] - search_start[1 - 1]
    derpTesting[2 - 1] = curPosition[2 - 1] - search_start[2 - 1]
    wait(1, SECONDS)
    if curPosition[2 - 1] - search_start[2 - 1] < 0:
        drivetrain.turn_to_heading(0, DEGREES)
    elif curPosition[2 - 1] - search_start[2 - 1] > 0:
        drivetrain.turn_to_heading(180, DEGREES)
    else:
        pass
    if not curPosition[2 - 1] - search_start[2 - 1] == 0:
        drivetrain.drive_for(FORWARD, math.fabs(curPosition[2 - 1] - search_start[2 - 1]), MM)
    if curPosition[1 - 1] - search_start[1 - 1] < 0:
        drivetrain.turn_to_heading(90, DEGREES)
    elif curPosition[1 - 1] - search_start[1 - 1] > 0:
        drivetrain.turn_to_heading(270, DEGREES)
    else:
        wait(1, SECONDS)
    if not curPosition[1 - 1] - search_start[1 - 1] == 0:
        drivetrain.drive_for(FORWARD, math.fabs(curPosition[1 - 1] - search_start[1 - 1]), MM)

def pickup_disc():
    global myVariable, distance_horizontal, disc_found, search_start, curPosition, derpTesting
    magnet.energize(BOOST)
    return_to_search()
    curPosition[1 - 1] = location.position(X, MM)
    curPosition[2 - 1] = location.position(Y, MM)
    return_to_search()
    curPosition[1 - 1] = location.position(X, MM)
    curPosition[2 - 1] = location.position(Y, MM)
    return_to_search()

def search_for_discs():
    global myVariable, distance_horizontal, disc_found, search_start, curPosition, derpTesting
    drivetrain.turn_to_heading(270, DEGREES)
    while not disc_found:
        drivetrain.drive_for(FORWARD, 25, MM)
        if down_eye.detect(RED):
            disc_found = True
        if down_eye.detect(GREEN):
            disc_found = True
        if down_eye.detect(BLUE):
            disc_found = True
        curPosition[1 - 1] = location.position(X, MM)
        curPosition[2 - 1] = location.position(Y, MM)
        wait(5, MSEC)
    pickup_disc()

def when_started1():
    global myVariable, distance_horizontal, disc_found, search_start, curPosition, derpTesting
    drivetrain.drive_for(FORWARD, 700, MM)
    search_start[1 - 1] = location.position(X, MM)
    search_start[2 - 1] = location.position(Y, MM)
    search_for_discs()

vr_thread(when_started1)
