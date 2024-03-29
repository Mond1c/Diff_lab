
# Анализ

Рассмотрим работу алгоритма на нескольких примерах.

Прежде чем переходить к рассмотрению данных с шумом, стоит заметить, что в силу специфики нелинейного метода наименьших квадратов на чистых данных (без добавления шума) для вычисления точных коэффициентов в большинстве случаев достаточно трёх точек, что можно увидеть на примере экспериментов 1, 4, 7

Проведённые эксперименты позволяют предположить, что хотя модель и весьма неплохо справляется с предложенной задачей, наиболее эффективное число точек для предсказания может разниться в силу зависимости вносимого шумом эффекта от значений коэффициентов. Так, в экспериментах 7, 8, 9 с ростом числа точек точность предсказания на данных с шумом, согласно введённой метрике, падала, что можно объяснить ростом абсолютных значений шума с ростом значений функции, также немаловажным может являться большая разница в абсолютных значениях коэффициентов.

В экспериментах 1, 2 и 3 с ростом числа точек точность лишь возрастала, а в серии 4, 5, 6 упала на последнем эксперименте, что опять-таки можно связать с возросшим влиянием шума.

Наиболее заметен вносимый шумом эффект в эксперименте 9

# Test 1
Output:

![output](output1.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.40183227  9.56029283]

Fitted Parameters without noise:[-1.5 10. ]

R squared: 0.9969310465574567

# Test 2
Output:

![output](output2.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.46345385  9.85688693]

Fitted Parameters without noise:[-1.5 10. ]

R squared: 0.9996700717686523

# Test 3
Output:

![output](output3.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.56607609 10.35830923]

Fitted Parameters without noise:[-1.5 10. ]

R squared: 0.9979927390836498

# Test 4
Output:

![output](output4.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.51751566 -1.04024345]

Fitted Parameters without noise:[ 2.5 -1. ]

R squared: 0.999685499932401

# Test 5
Output:

![output](output5.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.50747358 -1.01369429]

Fitted Parameters without noise:[ 2.5 -1. ]

R squared: 0.9999602632200101

# Test 6
Output:

![output](output6.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.48794885 -0.97420723]

Fitted Parameters without noise:[ 2.5 -1. ]

R squared: 0.9998676743953355

# Test 7
Output:

![output](output7.png)
True parameters: [5.12, 100]

Fitted Parameters with noise: [ 5.13573328 98.36448288]

Fitted Parameters without noise:[  5.12 100.  ]

R squared: 0.999405708691196

# Test 8
Output:

![output](output8.png)
True parameters: [5.12, 100]

Fitted Parameters with noise: [ 5.1740009  91.17320456]

Fitted Parameters without noise:[  5.12 100.  ]

R squared: 0.9827266810211707

# Test 9
Output:

![output](output9.png)
True parameters: [5.12, 100]

Fitted Parameters with noise: [  5.06069761 110.13839553]

Fitted Parameters without noise:[  5.12 100.  ]

R squared: 0.9772275132909239
