#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  #### Date Formatting ####
  print(now.strftime("the year is %Y"))
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("%a, %d %B, %y"))
  

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  # print(now.strftime("locale date ad time %c"))
  # print(now.strftime("locale date ad time %x"))
  # print(now.strftime("locale date ad time %X"))

  #### Time Formatting ####
  print(now.strftime("curreent time %I:%M:%S %p"))
  print(now.strftime("curreent time %H: %M"))

  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM



if __name__ == "__main__":
  main();
