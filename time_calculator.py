DAYS_OF_WEEK = 7

def add_time(start, duration, day_of_week = ""):
    
    hours, minutes = get_real_time(start) 
    time_to_add = duration.split(":")

    hours, minutes, extra_days = add_times(hours, minutes, int(time_to_add[0]), int(time_to_add[1]))

    return convert_time_to_string(hours, minutes, extra_days, day_of_week)


def get_real_time(time):
  split_formatted_time = time.split()
  split_time = split_formatted_time[0].split(":")

  hours = int(split_time[0])
  minutes = int(split_time[1])

  if split_formatted_time[1] == "PM":
    hours += 12

  return hours, minutes

def add_times(hours, minutes, hours_2_add, minutes_2_add):
  res_minutes = minutes + minutes_2_add
  res_hours = hours + hours_2_add
  extra_days = 0

  if res_minutes//60 > 0:
    res_hours+=1
    res_minutes = res_minutes%60

  if res_hours//24 > 0:
    extra_days = res_hours//24
    res_hours %= 24

  return res_hours, res_minutes, extra_days

def convert_time_to_string(hours, minutes, extra_days, day_of_week):
  
  hour_format = "AM"

  if hours >= 12:
    hours -= 12
    hour_format = "PM"

  if hours == 0:
      hours = 12

  day = get_correct_day_of_week(day_of_week, extra_days)

  common_date = str(hours) + ":" + str(minutes).rjust(2, "0") + " " + hour_format + day

  if extra_days == 0:
    return common_date
  elif extra_days == 1:
    return common_date + " " + "(next day)"
  else:
    return common_date + " (" + str(extra_days) + " days later)"


def get_correct_day_of_week(day_of_week, extra_days):

  days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  res = ""

  for i, day in enumerate(days_of_week):
    if day.lower() == day_of_week.lower():
      res = ", " + days_of_week[(i+extra_days)%DAYS_OF_WEEK]

  return res


