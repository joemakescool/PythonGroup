

def get_bool_gear(gear):
    new_gear = gear
    new_gear = str(new_gear.lower())
    if new_gear == 'p':
        is_in_park = True

    elif new_gear == 'r' or new_gear == 'd' or new_gear == 'n' or new_gear == '1' or new_gear == '2' or new_gear == '3':
        print("Not in park, can't open doors :(")
        is_in_park = False

    else:
        print("Invalid in put :|")
        is_in_park = False

    return is_in_park


def get_bool_child_locks(CL):
    new_CL = str(CL)
    if new_CL == "1":
        print("Child locks active. Inside doors are locked :(")
        return True
    else:
        return False


def get_bool_master_unlock(ML):
    new_ML = ML
    if new_ML == "1":
        return True
    else:
        print("Master lock active. Doors locked")
        return False


def check_left_doors(LD, LO):
    LD = str(LD)
    LO = str(LO)
    if LD == '1' or LO == '1':
        is_left_open = True
    else:
        is_left_open = False
    return is_left_open


def check_right_doors(RD, RO):
    RD = str(RD)
    RO = str(RO)
    is_right_open = False
    if RD == "1" or RO == "1":
        is_right_open = True
    else:
        is_right_open = False
    return is_right_open


def check_child_lock(CL):
    if CL == '0':
        is_lock_active = True
    else:
        is_lock_active = False
    return is_lock_active


def left_inside_door(LI):
    LI = str(LI)
    if LI == '1':
        is_left_door_open = True
    else:
        is_left_door_open = False
    return is_left_door_open


def right_inside_door(RI):
    RI = str(RI)
    if RI == '1':
        is_right_door_open = True
    else:
        is_right_door_open = False
    return is_right_door_open



def get_doors_open(LD, RD, CL, ML, LI, LO, RI, RO, GS):
    #Get boolean of park
    #If true, P, then you can move on
    is_in_park = get_bool_gear(GS)
    if is_in_park and get_bool_master_unlock(ML):
        just_both_doors = False
        just_right_door = False
        just_left_door = False
        #Master locks active
        #If active both doors closed
        #Else which doors open? Right or left doors or Both doors?
        print("Masters unlock switch active and in park :)")

        #checking both doors
        left_doors = check_left_doors(LD, LO)
        right_doors = check_right_doors(RD, RO)

        #if 1, child lock is active and will NOT work
        is_child_lock_off = check_child_lock(CL)
        is_left_inside_open = left_inside_door(LI)
        is_right_inside_open = right_inside_door(RI)

        #inside Doors
        if is_child_lock_off:
            print("Child doors can open :)")
            if is_left_inside_open and is_right_inside_open:
                just_both_doors = True
            elif is_left_inside_open:
                just_left_door = True
            elif is_right_inside_open:
                just_right_door = True
        #normal doors
        if left_doors and right_doors:
            just_both_doors = True
        elif right_doors:
            just_right_door = True
        elif left_doors:
            just_left_door = True
        #which doors open
        if just_both_doors:
            print("Both doors open!")
        elif just_right_door:
            print("Right doors open :)!")
        elif just_left_door:
            print("Left doors open :)!")
        else:
            print("Doors stay closed :(!")

    else:
        print("Both doors stay closed :(")


######################################################################################
#          (LD, RD, CL, ML, LI, LO, RI, RO, GS):

instruct = "1 1 1 1 1 0 1 0 d"
door_instructions = instruct.split()


print(door_instructions)
LD = door_instructions[0]
RD = door_instructions[1]
CL = door_instructions[2]
ML = door_instructions[3]
LI = door_instructions[4]
LO = door_instructions[5]
RI = door_instructions[6]
RO = door_instructions[7]
GS = door_instructions[8]
print(GS)

get_doors_open(LD, RD, CL, ML, LI, LO, RI, RO, GS)
