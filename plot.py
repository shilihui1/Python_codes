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

# Show and clear plot again
plt.show()
plt.clf()



