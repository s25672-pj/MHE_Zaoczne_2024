# 3-Partition problem

Opis problemu:
Problem 3-partycji jest silnie NP-zupełnym problemem w informatyce. Problem polega na zdecydowaniu, czy dany multizbiór liczb całkowitych może zostać podzielony na trójki, które wszystkie mają tę samą sumę. Dokładniej:

Wejście: multizbiór S zawierający n dodatnich elementów całkowitych.
Warunki: S musi być podzielny na m trójek, S1, S2, …, Sm, gdzie n = 3m. Te trójki dzielą S w tym sensie, że są rozłączne i pokrywają S. Wartość docelowa T jest obliczana przez wzięcie sumy wszystkich elementów w S, a następnie podzielenie przez m.
Wyjście: czy istnieje partycja S taka, że dla wszystkich trójek suma elementów w każdej trójce równa się T.

Przykład:
Zbiór S = {20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 22, 19} może zostać podzielony na cztery zbiory {20, 25, 45}, {23, 27, 40}, {49, 22, 19}, {30, 30, 30}, z których każdy sumuje się do T = 90
(żródło: https://en.wikipedia.org/wiki/3-partition_problem)

Zastosowane algorytmy:
