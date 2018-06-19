def four():
    # Question 4
    # Write a Python code to calculate the speed for running a 10-kilometer race in 1 hours 5 minutes 42 seconds.
    # What is the average pace (time per mile in minutes and seconds)?  What is the average speed in miles per hour?

    # converting the given distance from KM to miles
    distance = 10
    miles_per_km = 0.62
    distance_miles = float(distance * miles_per_km)
    print("Distance to cover (in miles): ", distance_miles)

    # converting time into seconds
    time_seconds = 1 * 60 * 60 + 5 * 60 + 42
    time_min = (1 * 60) + 5 + (42 / 60)
    time_hour = 1 + (5 / 60) + (42 / 3600)

    # to print the average time in seconds and in minutes
    print("Average time per mile (in seconds): ", float(time_seconds / distance_miles), "seconds")
    print("Average time per mile (in minutes): ", float(time_min / distance_miles), "minutes")
    # to print the average speed (miles per hour)
    print("Average speed (in miles per hour): ", int(distance_miles / time_hour))