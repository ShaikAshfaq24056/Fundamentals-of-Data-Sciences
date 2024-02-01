import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
percent_fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
data = pd.DataFrame({'Age': age, '%Fat': percent_fat})
mean_age = data['Age'].mean()
median_age = data['Age'].median()
std_age = data['Age'].std()
mean_fat = data['%Fat'].mean()
median_fat = data['%Fat'].median()
std_fat = data['%Fat'].std()
print("Age: Mean =", mean_age, "Median =", median_age, "Standard Deviation =", std_age)
print("%Fat: Mean =", mean_fat, "Median =", median_fat, "Standard Deviation =", std_fat)
data.boxplot(column=['Age', '%Fat'])
plt.title("Boxplots for Age and %Fat")
plt.show()
plt.scatter(data['Age'], data['%Fat'])
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.title('Scatter Plot')
plt.show()
plt.figure()
stats.probplot(data['%Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot for %Fat')
plt.show()
