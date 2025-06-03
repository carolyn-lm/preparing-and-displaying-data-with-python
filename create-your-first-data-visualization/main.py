# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
# Let's rank some of our favorite snacks
snack_scores = [3, 2, 1]
slice_labels = ["popcorn", "chips", "nuts"]
colors = ["#D496A7", "#5D576B", "#6CD4FF"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels, colors=colors)

# Give your pie chart a title in the quotes
plt.title("Favorite Snacks", fontsize=22)

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("snack_pie_chart.png")
