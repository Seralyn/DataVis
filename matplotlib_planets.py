from matplotlib import pyplot
import numpy

#print(pyplot.style.available)
pyplot.style.use("fivethirtyeight")
#if using a style, consider removing custom color, grid, and linewidth as they come built in or not according to aesthetics


planets_x = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

#x_indexes = numpy.arange(len(ages_x))


diameter_y = [4879, 12104, 12756, 6794,
            142980, 116460, 51120, 49530, 2300]

width = 0.5 #default is 0.8

barlist=pyplot.bar(planets_x, diameter_y, width=width)  
barlist[0].set_color('#5D6D7E')
barlist[1].set_color('#F4D03F')
barlist[2].set_color('#2ECC71')
barlist[3].set_color('#E74C3C')
barlist[4].set_color('#E67E22')
barlist[5].set_color('#F8C471')
barlist[6].set_color('#76D7C4')
barlist[7].set_color('#3498DB')
barlist[8].set_color('#D98880')

#pyplot.xticks(ticks=x_indexes, labels=ages_x) #corrects x asis being labled by index number
pyplot.title("Equatorial Diameter of Solar System Bodies")

#pyplot.xlabel("Planets")
pyplot.ylabel("Diameter in KM")

#pyplot.savefig("DesiredFileName")  #saves file as png, but using window click is likely better

pyplot.legend()
pyplot.grid(True)
pyplot.tight_layout()
pyplot.show()