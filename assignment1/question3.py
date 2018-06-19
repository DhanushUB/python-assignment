def three():
    # Question 3
    # I have started walking to home at 7:30 AM for the first mile at slow step (8 min:15 sec per mile), then 3 miles at
    # speed(7 min:12 sec per mile), what time do I get home for breakfast? (format output in hh: min).

    # taking miles, minutes and seconds as separate variables
    first_mile_min = 8
    first_mile_sec = 15
    next_miles_min = 7
    next_miles_sec = 12
    remaining_miles = 3
    start_hour = 7
    start_min = 30

    # first mile time, converting into seconds
    fm_time = (first_mile_min * 60) + first_mile_sec

    # converting the time into seconds for time taken to cover 3 miles,
    next_time = remaining_miles * ((next_miles_min * 60) + next_miles_sec)

    # total time take to reach home
    total_time_min = int((fm_time + next_time) / 60)
    total_time = float(total_time_min / 60)

    # printing the total time taken to reach home and time in hh:mm format
    print("Total time taken to reach home will be: ", total_time, " hours or ", total_time_min, " minutes")
    print("You will reach at: ", int(total_time + start_hour), ":", total_time_min + start_min)