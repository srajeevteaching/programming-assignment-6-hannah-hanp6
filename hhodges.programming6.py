# Hannah Hodges
# CS 151, Dr. Rajeev
# Programming 6
# 12/ 7/ 2021

# main function to run the program
def main():
   file_read()
   list = file_read("crime.csv")
   print(list)
   user_input = input("Choose option to see data:" )
# if/ else statements to allow user to choose from menu
   if user_input == '1':
      change_in_crime(list)
   if user_input == '2':
      juvi_arrest_rate_average(list)
   if user_input == '3':
      gun_violence(list)
   else:
      if user_input == 'end':
         print ("Thank you!")


# function to find file
def file_read(filename):
   list = []
   with open(filename) as op:
      for line in op.readlines():
         list.append(line.split(","))
   return list

#change in crime function to find the change
def change_in_crime(list):
   print ("Enter neighborhood")
   user_input = input()
   data = neighborhood_name(name.in.filename, '')
   if user_input == neighborhood_data:
      print (data)

#function to find average of juvi rate
def juvi_arrest_rate_average(list):
   print("Enter neighborhood to see juvi arrest rate:")
   user_input = input()
   city_data = neighborhood.name(name. in.filename, '')
   juvi = (filename, "arrest")
   count_juvi = []
   index = 0
   count = 0
   while count_juvi > 0:
      count = count + juvi[index]
      index += 1
   print ("Average number of juvi arrests:",(count / len(juvi)) )


# function of my choosing question
# used to find narco rate from file 
def gun_violence(list):
   print("Enter neighborhood to see gun rate:")
   user_input = input()
   city_data = neighborhood_name(name. in.filename, '')
   gunRate = (filename, "gun")
   with open(filename) as op:
      for line in op.readlines():
         print (gunRate)


main()

