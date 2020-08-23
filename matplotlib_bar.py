from matplotlib import pyplot
import numpy

#print(pyplot.style.available)
pyplot.style.use("bmh")
#if using a style, consider removing custom color, grid, and linewidth as they come built in or not according to aesthetics


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = numpy.arange(len(ages_x))
width = 0.25 #default is 0.8

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

pyplot.bar(x_indexes - width, dev_y, width=width, color="#444444", label="All Devs")  
pyplot.bar(x_indexes, py_dev_y, width=width, color="#5a7d9a", label="Python Devs")
pyplot.bar(x_indexes + width, js_dev_y, width=width, color="#adad3b", label="Javascript Devs")

pyplot.xticks(ticks=x_indexes, labels=ages_x) #corrects x asis being labled by index number
pyplot.title("Average Developer Salary by Age")
pyplot.xlabel("Ages")
pyplot.ylabel("Median Salary")

#pyplot.savefig("DesiredFileName")  #saves file as png, but using window click is likely better

pyplot.legend()
pyplot.grid(True)
pyplot.tight_layout()
pyplot.show()