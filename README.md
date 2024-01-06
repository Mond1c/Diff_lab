
# Анализ

Рассмотрим работу алгоритма на нескольких примерах. 

Прежде чем переходить к рассмотрению данных с шумом, стоит заметить, что в силу специфики нелинейного метода наименьших квадратов на чистых данных (без добавления шума) для вычисления точных коэффициентов достаточно трёх точек, что можно увидеть на примере экспериментов 3, 6, 9

Эксперименты 1,2 и 3 позволяют заметить, что с увеличением количества точек точность предскахания данных с шумом растёт, что полностью соответствует ожиданию, ведь большее количество данных позволяет сглаживать выбросы, порождаемые шумом, увеличивая точность предсказания.

Наиболее заметен вносимый шумом эффект в эксперименте 2. Из-за небольшого числа точек роль шума ожидаемо возрастает, серьёзно изменяя предсказываемые параметры.

Также стоит отметить, что выводы, сделанные на основе наблюдений 1, 2 и 3 не имеют отношения к специфичности значений или знаков коэффициентов, в чём легко убедиться, рассмотрев рещультаты двух следующих серий экспериментов.



# Test 1
Output:

![output](output1.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.40183227  9.56029283]

Fitted Parameters without noise:[-1.5 10. ]

# Test 2
Output:

![output](output2.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.46345385  9.85688693]

Fitted Parameters without noise:[-1.5 10. ]

# Test 3
Output:

![output](output3.png)
True parameters: [-1.5, 10]

Fitted Parameters with noise: [-1.56607609 10.35830923]

Fitted Parameters without noise:[-1.5 10. ]

# Test 4
Output:

![output](output4.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.51751566 -1.04024345]

Fitted Parameters without noise:[ 2.5 -1. ]

# Test 5
Output:

![output](output5.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.50747358 -1.01369429]

Fitted Parameters without noise:[ 2.5 -1. ]

# Test 6
Output:

![output](output6.png)
True parameters: [2.5, -1]

Fitted Parameters with noise: [ 2.48794885 -0.97420723]

Fitted Parameters without noise:[ 2.5 -1. ]

# Test 7
Output:

![output](output7.png)
True parameters: [11.12, 100]

Fitted Parameters with noise: [ 8.79582738 17.8673468 ]

Fitted Parameters without noise:[ 8.79581066 17.86731062]

# Test 8
Output:

![output](output8.png)
True parameters: [11.12, 100]

Fitted Parameters with noise: [11.11337494  5.14851556]

Fitted Parameters without noise:[11.11451091  5.04670249]

# Test 9
Output:

![output](output9.png)
True parameters: [11.12, 100]

Fitted Parameters with noise: [ 10.80325711 187.15911342]

Fitted Parameters without noise:[ 11.12 100.  ]
