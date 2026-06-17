import matplotlib.pyplot as plt

# Sample social media reach data
platforms = ["Instagram", "Facebook", "Twitter", "LinkedIn", "YouTube"]
reach = [12000, 9000, 7000, 5000, 15000]

# Create bar chart
plt.bar(platforms, reach)

# Title and labels
plt.title("Social Media Reach Analysis")
plt.xlabel("Social Media Platforms")
plt.ylabel("Reach")

# Display values on bars
for i, value in enumerate(reach):
    plt.text(i, value + 200, str(value), ha='center')

# Show chart
plt.show()