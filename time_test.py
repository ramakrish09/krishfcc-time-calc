def add_time(start, duration, weekday=None):
  print(start, duration, weekday)
  days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
  hrs = start.split(':')
  startTime = int(hrs[0])
  minute = hrs[1].split()
  startMinutes = int(minute[0])

  splitDuration = duration.split(':')
  durationMinutes = int(splitDuration[0]) * 60 + int(splitDuration[1])

  ampm = minute[1]
 
  #print(hours2)
  startTime %= 12
  if ampm == 'PM':
    startTime += 12

  tim = startTime * 60 + startMinutes + durationMinutes
  newHrs, newMin = divmod(tim, 60)
  noDays = int(newHrs / 24)
  
  newHrs %= 24
  #print("newHrs = ", newHrs)
  newAmPm = "AM"
  if newHrs >= 12:
    newAmPm = "PM"

  #print("newAmPm=", newAmPm)
  
  newHrs %= 12
  if newHrs == 0:
    newHrs = 12

  if newMin <= 9:
    newMinutes = '0' + str(newMin)
  else:
    newMinutes = str(newMin)
  
  #print("newMinutes=",newMinutes)

  daysLower = [x.lower() for x in days]

  if weekday != None:
    normNoDay = noDays % 7
    #print("normNoDay", normNoDay)
    ind = daysLower.index(weekday.lower())
    print("ind", ind)

    if ((ind + normNoDay) > 6):# out of bounds
      rem = (6 - ind)
      newIndex = normNoDay - rem - 1
    else:
      newIndex = ind + normNoDay
    #print("newIndex", newIndex)
    #print("index=", newIndex)

  out_time = str(newHrs) + ":" + newMinutes + " " + newAmPm
  if weekday != None:
    out_time += "," + " " + days[newIndex]

  if noDays == 1:
    out_time += " "+ "(next day)"
  elif noDays > 1:
    out_time += " " + "(" + str(noDays) + " " + "days later)"

  #print(newHrs, newMin, newAmPm, noDays)
  print(out_time)
  #print(startTime, startMinutes, durationMinutes, ampm)
  #print("time =", tim)
  return out_time
