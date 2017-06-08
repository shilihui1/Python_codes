import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('population')
plt.title('world population projections')
plt.yticks([0, 2, 4, 6], ['0B', '2B', '4B', '6B'])
plt.show()


# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)
plt.show()

#scatterplot
plt.scatter(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp, s = np_pop, c = col, alpha = 0.8)
plt.xscale('log') 

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

plt.show()

# Show and clear plot again
plt.show()
plt.clf()



