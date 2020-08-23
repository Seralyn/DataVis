from matplotlib import pyplot

#print(pyplot.style.available)
pyplot.style.use("bmh")
#if using a style, consider removing custom color, grid, and linewidth as they come built in or not according to aesthetics


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

pyplot.plot(ages_x, dev_y, color="#444444", linestyle="--", marker=".", label="All Devs")  
pyplot.plot(ages_x, py_dev_y, color="#5a7d9a", linewidth=2, label="Python Devs")
pyplot.plot(ages_x, js_dev_y, color="#adad3b", linewidth=2, label="Javascript Devs")


pyplot.title("Average Developer Salary by Age")
pyplot.xlabel("Ages")
pyplot.ylabel("Median Salary")

#pyplot.savefig("DesiredFileName")  #saves file as png, but using window click is likely better

pyplot.legend()
pyplot.grid(True)
pyplot.tight_layout()
pyplot.show()