

def find_veg(grill):
    veggie, non_veggie = 0, 0 
    contain_meet = 'x'
    for skewer in grill:
        is_veggie = contain_meet not in skewer
        if is_veggie:
            veggie+=1
        else:
            non_veggie+=1 
    result = [veggie, non_veggie]

    return result