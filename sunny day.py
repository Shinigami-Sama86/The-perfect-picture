from pylab import *

# Arrays
Grass = array ( [ 0 , 0.1 , 0 , 0.1 , 0 , 0.1 , 0 , 0.1 , 0 , 0.1 ] ) # Grass array
Mouintains = np . random . uniform ( 0.2 , np . random . normal ( loc = 0.7 , scale = 0.15 , size = 10 )  , 10 ) # random array generator arround mean values for mouintains
x = linspace ( 0 , 9 , 10 ) # X-axis 
XBirds = np . random . uniform ( 0 , 3 , 30 )
Birds = np . random . uniform ( (max ( Mouintains) + 0.05 ) , 1.3 , 30 ) # Birds, randomly generated with the the max value of mountains as min + 0.07  

# Plots
close ( "all" ) # close any open graphs to provent over writting 
plot ( x , Grass , "g-" ) # Grass
plot ( x , Mouintains , "b" ) # Mouintains
scatter ( 8 , 1.2 , marker = "o" , c = "y" , s = 2000 ) # Sun
scatter ( XBirds , Birds , marker = ( 3 , 2 , 180 ) , s = 10 , c = "k" ) # Birds,  Marker using 3 sided astrix rotated through 180 degrees

# Graph
ylim ( 0 , 1.4 ) # scale on y-axis
xlim ( 0 , 9 ) # Scale on x-axis