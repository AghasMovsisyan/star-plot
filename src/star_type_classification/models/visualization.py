# modals/visualization.py
import matplotlib.pyplot as plt

def plot_hr_diagram(data):
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Temperature (K)'], data['Absolute magnitude(Mv)'], c=data['Star type'])
    plt.xlabel('Temperature (K)')
    plt.ylabel('Absolute Magnitude')
    plt.title('HR Diagram')
    plt.colorbar(label='Star Type')
    plt.savefig('../output/hr_diagram.png')
    plt.show()
