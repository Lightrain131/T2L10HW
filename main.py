# Import modules
import matplotlib.pyplot as p

# Input the values
xValues = ([1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
yValues = ([14.23, 14.35, 14.22, 14.42, 14.54, 14.36, 14.33, 14.45, 14.51, 14.52, 14.48, 14.55, 14.50, 14.49, 14.41, 14.50, 14.56, 14.43, 14.48, 14.52, 14.59])

# Adjust the size of windows
p.figure(figsize=(12, 6))

# Title and label
p.title("Global mean temperature from 1994 to 2014")
p.xlabel("Years")
p.ylabel("Temp / °C")

# Plot and add the grid
p.plot(xValues, yValues, marker='o')
p.grid()

# Make the year on x-axis be integers
p.xticks(xValues)

# Show!
p.show()

# QUIT
quit()
