def progress_days(miles_saturday):
    count_progress_days = 0
    lenght_miles_saturday = len(miles_saturday) - 1

    for miles in range(0, lenght_miles_saturday):
        is_progress_day = miles_saturday[miles + 1] > miles_saturday[miles]
        if is_progress_day:
            count_progress_days += 1        
    
    return count_progress_days