import dice, pandas as pd

def get_modifier_subtotal(reflex,skill,other):
    return reflex+skill+other

def get_hit_locations(hit_num):
    hit_table = {1:"Head",
                 2:"Torso",
                 3:"Torso",
                 4:"Torso",
                 5:"R.Arm",
                 6:"L.Arm",
                 7:"R.Leg",
                 8:"R.Leg",
                 9:"L.Leg",
                 10:"L.Leg"}
    
    hit_locations = []
    
    for i in range(hit_num):
        hit_loc_roll = sum(dice.roll('1d10'))
        hit_location = hit_table[hit_loc_roll]
        hit_locations.append(hit_location)
                
    return hit_locations

def get_to_hit(distance):
    to_hit = {"Point Blank":10,
              "Close":15,
              "Medium":20,
              "Long":25,
              "Extreme":30}
    hit_num = to_hit[distance]
    return hit_num

def get_base_dmgs(weapon,hit_num):
    #weapon_dmg = weapon.dmg
    weapon_dmg = '5d6'
    dmgs = []
    
    for i in range(hit_num):
        dmg = sum(dice.roll(weapon_dmg))
        dmgs.append(dmg)
    return dmgs

def get_single_fire_hits(rounds,distance,modifier_sum):
    print("Firing {0} rounds at {1} range with modifier {2}".format(distance.lower(),modifier_sum))
    to_hit = get_to_hit(distance)
    hit_num = 0
    for i in range(rounds):
        hit_score = sum(dice.roll('1d10'))
        if hit_score == 1:
            hit_num = 0
        elif hit_score == 10:
            hit_score += sum(dice.roll('1d10'))
        else:
            hit_score += modifier_sum
            if hit_score >= to_hit:
                hit_num += 1
            else:
                pass
    print("Hit {0} rounds".format(hit_num))
    return hit_num

def get_three_round_burst_hits(rounds,distance,modifier_sum):
    print("Firing 3-round burst at {1} range with modifier {2}".format(rounds,distance.lower(),modifier_sum))
    if distance == "Long" or distance == "Extreme":
        pass
    else:
        modifier_sum += 3
    to_hit = get_to_hit(distance)
    hit_score = sum(dice.roll('1d10'))
    if hit_score == 1:
        hit_num = 0
    elif hit_score == 10:
        hit_score += sum(dice.roll('1d10'))
    else:
        hit_score += modifier_sum
        if hit_score >= to_hit:
            hit_num = sum(dice.roll('1d3'))
        else:
            hit_num = 0
    print("Hit {0} rounds".format(hit_num))
    return hit_num
        
def get_automatic_fire_hits(rounds,distance,modifier_sum):
    print("Firing {0} rounds full-auto at {1} range with modifier {2}".format(rounds,distance.lower(),modifier_sum))
    if distance == "Close" or distance == "Point Blank":
        modifier_sum += int(rounds/10)
    else:
        modifier_sum += -int(rounds/10)
    to_hit = get_to_hit(distance)
    hit_score = sum(dice.roll('1d10'))
    print("Rolled a "+str(hit_score))
    if hit_score == 1:
        hit_num = 0
    elif hit_score == 10:
        hit_score += sum(dice.roll('1d10'))
    else:
        hit_score += modifier_sum
        hit_num = hit_score - to_hit
        hit_num_bounded = lambda x, l, u: l if x < l else u if x > u else x
        hit_num = hit_num_bounded(hit_num,0,rounds)
    print("Hit {0} rounds".format(hit_num))
    return hit_num
    
 def get_suppressive_fire_hits(weapon,rounds,fire_zone_area,suppress_save_modifier):
    print("Suppressing a {0}-meter area with {1} rounds".format(fire_zone_area,rounds))
    suppression_save_check = rounds / fire_zone
    save_roll = sum(dice.roll(1d10))
    print("Rolled a "+str(save_roll)))
    save_roll += suppress_save_modifier
    if save_roll >= suppression_save_check:
        hit_num = 0
    else:
        hit_num = sum(dice.roll(1d10))
    print("Hit {0} rounds".format(hit_num))
    return hit_num
    
def attack(weapon,firing_mode,rounds,distance,modifier_subtotal="0",aim="No",suppress_save_modifier="0",fire_zone_area="2"):
    #modifier_subtotal += weapon.wa
    
    if aim=="No":
        modifier_sum = modifier_subtotal
    else:
        modifier_sum = modifier_subtotal - 4
        
    if firing_mode == "Automatic":
        hit_num = get_automatic_fire_hits(rounds,distance,modifier_sum)
    elif firing_mode == "Burst":
        hit_num = get_three_round_burst_hits(rounds,distance,modifier_sum)
    elif firing_mode == "Single":
        hit_num = get_single_fire_hits(rounds,distance,modifier_sum)
    elif firing_mode == "Suppress":
        hit_num = get_suppressive_fire_hits(rounds,fire_zone_area,suppress_save_modifier)
        
    if aim=="No":
        hit_locations = get_hit_locations(hit_num)
    else:
        hit_locations = [aim for i in distance(hit_num)]
        
    base_dmgs = get_base_dmgs(weapon,hit_num)
    
    hit_list = []
    
    for i in range(hit_num):
        hit = (hit_locations[i],base_dmgs[i])
        hit_list.append(hit)
        print("{0} dmg to {1}".format(hit[1],hit[0]))
        
    return hit_list