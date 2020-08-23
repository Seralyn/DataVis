from matplotlib import pyplot
import numpy

#print(pyplot.style.available)
pyplot.style.use("bmh")
#if using a style, consider removing custom color, grid, and linewidth as they come built in or not according to aesthetics


planets_x = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

#x_indexes = numpy.arange(len(ages_x))


diameter_y = [4879, 12104, 12756, 6794,
            142980, 116460, 51120, 49530, 2300]

width = 0.25 #default is 0.8
pyplot.bar(planets_x, diameter_y, width=width, label="Planetary Diameters")  


#pyplot.xticks(ticks=x_indexes, labels=ages_x) #corrects x asis being labled by index number
pyplot.title("Equatorial Diameter of Solar System Bodies")
pyplot.xlabel("Planets")
pyplot.ylabel("Diameter")

#pyplot.savefig("DesiredFileName")  #saves file as png, but using window click is likely better

pyplot.legend()
pyplot.grid(True)
pyplot.tight_layout()
pyplot.show()