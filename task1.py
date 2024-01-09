# Поиск ДУ по значениям наблюдений (симулированных данных с шумом и без):
# (10) Нахождение параметров (значений коэффициентов) 
# линейного дифференциального уравнения с постоянными коэффициентами при известных значениях в ряде точек. 

# 1.1 10 баллов Корнилович Михаил (М3236) и Забейворота Кирилл (М3236)
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

README_STANDARD = """
# Анализ

Рассмотрим работу алгоритма на нескольких примерах.

Прежде чем переходить к рассмотрению данных с шумом, стоит заметить, что в силу специфики нелинейного метода наименьших квадратов на чистых данных (без добавления шума) для вычисления точных коэффициентов в большинстве случаев достаточно трёх точек, что можно увидеть на примере экспериментов 1, 4, 7

Проведённые эксперименты позволяют предположить, что хотя модель и весьма неплохо справляется с предложенной задачей, наиболее эффективное число точек для предсказания может разниться в силу зависимости вносимого шумом эффекта от значений коэффициентов. Так, в экспериментах 7, 8, 9 с ростом числа точек точность предсказания на данных с шумом, согласно введённой метрике, падала, что можно объяснить ростом абсолютных значений шума с ростом значений функции, также немаловажным может являться большая разница в абсолютных значениях коэффициентов.

В экспериментах 1, 2 и 3 с ростом числа точек точность лишь возрастала, а в серии 4, 5, 6 упала на последнем эксперименте, что опять-таки можно связать с возросшим влиянием шума.

Наиболее заметен вносимый шумом эффект в эксперименте 9
"""

with open("README.md", "w") as file:
    file.write(README_STANDARD)


def r_squared(true_parameters, predict_parameters):
    y_mean = np.mean(0.5 * (true_parameters + predict_parameters))
    return 1 - ((true_parameters[0] - predict_parameters[0]) ** 2 + (true_parameters[1] - predict_parameters[1]) ** 2) / ((true_parameters[0] - y_mean) ** 2 + (true_parameters[1] - y_mean) ** 2)


def differential_eqn(y, t, a, b):
    dydt = a * y + b
    return dydt

def fit_differential_eqn(t, a, b):
    y_fit = odeint(differential_eqn, y0=1.0, t=t, args=(a, b))
    return y_fit.flatten()


def generate(t_simulated, true_parameters, visible_points_count, output_png, testNum, start_range, end_range):
    np.random.seed(42)
    y_simulated_solution = odeint(differential_eqn, y0=1.0, t=t_simulated, args=tuple(true_parameters)).flatten()

    noise = np.random.normal(0, np.abs(y_simulated_solution * 1.02 - y_simulated_solution), len(t_simulated))
    y_simulated = y_simulated_solution + noise

    initial_guess = [1.0, 1.0]  # Начальное предположение для параметров
    # нелинейный метод наименьших квадратов
    params_with_noise, covariance = curve_fit(fit_differential_eqn, t_simulated, y_simulated, p0=initial_guess)
    params_without_noise, covariance2 = curve_fit(fit_differential_eqn, t_simulated, y_simulated_solution, p0=initial_guess)
    print("True Parameters:", true_parameters)
    print("Fitted Parameters with noise:", params_with_noise)
    print("Fitted Parameters without noise:", params_without_noise)
    loss = r_squared(true_parameters, params_with_noise)
    print("R squared: ", loss)
    t_more_points = np.linspace(start_range, end_range, visible_points_count)
    t_more_points2 = np.linspace(start_range, end_range, 100)
    y1 = odeint(differential_eqn, y0=1.0, t=t_more_points, args=tuple(params_without_noise)).flatten()
    noise = np.random.normal(0, np.abs(y1 * 1.02 - y1), len(t_more_points))
    y1 += noise
    y2 = odeint(differential_eqn, y0=1.0, t=t_more_points2, args=tuple(params_without_noise)).flatten()
    y_true = odeint(differential_eqn, y0=1.0, t=t_more_points2, args=tuple(true_parameters)).flatten()
    
    plt.figure(figsize=(8, 6))
    plt.scatter(t_more_points, y1, label='Симулированные данные с шумом')
    plt.scatter(t_simulated, y_simulated, label='Входные данные')
    plt.plot(t_more_points2, y2, label='Симулированные данные без шума ', color='red')
    plt.plot(t_more_points2, y_true, label='Истинные данные', color="green")
    plt.plot(t_more_points2, fit_differential_eqn(t_more_points2, *params_with_noise), label='Аппроксимированная кривая', color="yellow")
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.legend()
    plt.show()
    plt.savefig(output_png)
    start_output = """
# Test """ + str(testNum) + """
Output:

![output](""" + output_png + ")\n"
    with open("README.md", "a") as file:
        file.write(start_output)
        file.write("True parameters: " + str(true_parameters) + "\n\n")
        file.write("Fitted Parameters with noise: " + str(params_with_noise) + "\n\n")
        file.write("Fitted Parameters without noise:" + str(params_without_noise) + "\n\n")
        file.write("R squared: " + str(loss) + "\n")

# Входные данные
visible_points_count = 20
t_simulated = np.linspace(0, 2, 3, endpoint=True)
true_parameters = [-1.5, 10]
generate(t_simulated, true_parameters, visible_points_count, "output1.png", 1, 0, 10)
t_simulated = np.linspace(0, 10, 10, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output2.png", 2, 0, 10)
t_simulated = np.linspace(0, 10, 50, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output3.png", 3, 0, 10)

t_simulated = np.linspace(0, 2, 3, endpoint=True)
true_parameters = [2.5, -1]
generate(t_simulated, true_parameters, visible_points_count, "output4.png", 4, 0, 2)
t_simulated = np.linspace(0, 2, 10, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output5.png", 5, 0, 2)
t_simulated = np.linspace(0, 2, 50, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output6.png", 6, 0, 2)

t_simulated = np.linspace(0, 2, 3, endpoint=True)
true_parameters = [5.12, 100]
generate(t_simulated, true_parameters, visible_points_count, "output7.png", 7, 0, 2)
t_simulated = np.linspace(0, 2, 10, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output8.png", 8, 0, 2)
t_simulated = np.linspace(0, 2, 50, endpoint=True)
generate(t_simulated, true_parameters, visible_points_count, "output9.png", 9, 0, 2)