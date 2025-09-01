import matplotlib.pyplot as plt

#budget allocation
budget = {'Leisure': 500, 'Rent': 3500,'Internet': 550, 'Food': 2000, 'Petrol': 1200}

#Pie chat
labels = budget.keys()
sizes = budget.values()

plt.pie(sizes, labels =labels)
plt.title('Monthly Budget')
plt.axis('equal')

plt.show()
