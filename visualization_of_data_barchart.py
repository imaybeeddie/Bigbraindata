
import matplotlib.pyplot as plt
product = ["BMW x5", "Toyota", "Lexus 360", "Mercedes Benz", "Ferrari", "Audi 550"]
revenues = [86.4, 250, 38, 72, 39.1, 40.5]
colors = ['red', 'blue', 'black', 'cyan', 'grey', 'green']

plt.figure(figsize=(10, 10))
bars = plt.bar(product, revenues, color=colors, edgecolor='white')

plt.xlabel('Car Model', fontsize=10)
plt.ylabel('Total Revenue(Millions)')
plt.title('Revenue Chart')

plt.gca().set_facecolor('lightgrey')

for bar, revenues in zip(bars, revenues):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{revenues}M', ha='center', color='white')
plt.legend(bars, product, loc='center')
plt.show()