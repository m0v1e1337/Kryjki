import pandas as pd
import matplotlib.pyplot as plt

# Загрузить датасет из файла
dataset = pd.read_csv(r'C:\Users\Dmitrii Tihonov\PycharmProjects\Kryjki\.venv\Lib\Dota2 Heroes by MMR Bracket.csv')

# Линейный график
plt.plot(dataset['Heroes'], label='Heroes 1')
plt.plot(dataset['(<2K MMR) PickRate(%)'], label='(<2K MMR) PickRate(%) 2')
plt.plot(dataset['(<2K MMR) WinRate(%)'], label='(<2K MMR) WinRate(%) 3')
plt.xlabel('Временная ось')
plt.ylabel('Значения')
plt.title('Линейные графики')
plt.legend()
plt.show()

# Столбчатая диаграмма
plt.bar(dataset['(2K-3K MMR) PickRate(%)'], dataset['(2K-3K MMR) WinRate(%)'], label='(2K-3K MMR) WinRate(%) 5')
plt.bar(dataset['(3K-4K MMR) PickRate(%)'], dataset['(3K-4K MMR) WinRate(%)'], label='(3K-4K MMR) WinRate(%) 7')
plt.bar(dataset['(4K-5K MMR) PickRate(%)'], dataset['(4K-5K MMR) WinRate(%)'], label='(4K-5K MMR) WinRate(%) 9')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.title('Столбчатые диаграммы')
plt.legend()
plt.show()

# Круговая диаграмма
plt.pie(dataset['(>5K MMR) PickRate(%)'], labels=dataset['(>5K MMR) WinRate(%)'], autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.show()

# Диаграмма рассеяния
plt.scatter(dataset['Heroes'], dataset['(>2K MMR) KDA Ratio'])
plt.xlabel('Heroes 12')
plt.ylabel('(>2K MMR) KDA Ratio 13')
plt.title('Диаграмма рассеяния')
plt.show()

# Гистограмма
plt.hist(dataset['(>2K MMR) Avg Match'], bins=10)
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.show()

# Вывод и описание каждого графика
print("1. Линейные графики:")
# Опишите, что изображено на графиках и сделайте выводы

print("2. Столбчатые диаграммы:")
# Опишите, что изображено на диаграммах и сделайте выводы

print("3. Круговые диаграммы:")
# Опишите, что изображено на диаграммах и сделайте выводы

print("4. Диаграммы рассеяния:")
# Опишите, что изображено на диаграммах и сделайте выводы

print("5. Гистограммы:")
# Опишите, что изображено на гистограммах и сделайте выводы
