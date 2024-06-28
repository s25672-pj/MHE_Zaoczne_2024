# 3-Partition problem

Opis problemu:
Problem 3-partycji jest silnie NP-zupełnym problemem w informatyce. Problem polega na zdecydowaniu, czy dany multizbiór liczb całkowitych może zostać podzielony na trójki, które wszystkie mają tę samą sumę. Dokładniej:

Wejście: multizbiór S zawierający n dodatnich elementów całkowitych.
Warunki: S musi być podzielny na m trójek, S1, S2, …, Sm, gdzie n = 3m. Te trójki dzielą S w tym sensie, że są rozłączne i pokrywają S. Wartość docelowa T jest obliczana przez wzięcie sumy wszystkich elementów w S, a następnie podzielenie przez m.
Wyjście: czy istnieje partycja S taka, że dla wszystkich trójek suma elementów w każdej trójce równa się T.

Przykład:
Zbiór S = {20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 22, 19} może zostać podzielony na cztery zbiory {20, 25, 45}, {23, 27, 40}, {49, 22, 19}, {30, 30, 30}, z których każdy sumuje się do T = 90
(żródło: https://en.wikipedia.org/wiki/3-partition_problem)

Implementacja problemu:
Implementacja problemu 3-partition znajduje się w pliku optimization_problem.py, w klasie ThreePertitionProblem. Zadanie polega na podziale zbioru liczb na podzbiory trzy elementowe, tak aby różnice sum były jak najmniejsze
  - objective_function - funkcja która wylicza różnice pomiędzy największą i najmniejszą sumą podzbiorów w danym rozwiązaniu.
  - generate_random_solution - funkcja generująca losowe rozwiązanie
  - get_neighborhood - funkcja generująca sąsiedztwo danego rozwiązania. Sasiedztwo jest definiowane jako zbiór rozwiązań uzyskanych przez zmianę elementów pomiedzy podzbiorami.
  - get_random_neighbor - funkcja generująca losowego sąsiada danego rozwiązania. Wybiera losowe elementy z dwóch różnych podzbiorów i zamienia je miejscami

Zastosowane algorytmy:
1. Algorytm pełnego przeglądu - przeszukuje całą przestrzeń rozwiązań w celu znalezienia optymalnego rozwiązania
     - brute_force - funkcja przegląda wszystkie możliwe permutacje w zadanym problemie, generując wszystkie możlwe rozwiązania i ocenia je za pomocą funkcji celu. Funkcja zwraca najlepsze rozwiązanie, jego wartość oraz krzywą zbieżności
2. Algorytm wspinaczkowy - metoda optymalizacji, która iteracyjnie poprawia bieżące roziwązanie poprzez wybór najlepszego sąsiada.
   2.1. klasyczny z deterministycznym wyborem najlepszego sąsiada punktu roboczego
     - hill_climbing - funkcja która implementuje algorytm wspinaczkowy dla problemu. Funkcja pobiera losowe rozwiązanie, wyznacza jego wartość, po czym przypisuje je jako aktualnie najlepsze rozwiązanie. Następnie tworzy sąsiadów rozwiązania, porównuje ich i wybiera tego z najlepszą wartością. Następnie prównuje najlepszego sąsaida z aktualnie najlepszym rozwiązaniem. Jeśli nowe rozwiązanie jest lepsze, to je nadpisuje jako najlepsze. Petla przerywa się gdy nowe rozwiązania nie są lepsze od aktualnego, i zwraca aktualnie najlepsze rozwiązanie, jego wartość oraz krzywą zbieżności
   2.2. z losowym wyborem sąsiada
       - hill_climbing_random - funkcja działa podobnie jak porzednio, z tą różnicą, że sąsiad który jest wybierany do porównania z aktualnym rozwiązaniem, jest wybierany w sposób losowy. Zasady dalszego działania są takie same jak przy hill_climbing
3. Algorytm tabu - technika optymalizacji, która unika wpadanie w lokalne minima poprzez przecowywanie listy zabronionych ruchów
       - tabu_search - funkcja implementująca algorytm Tabu, przyjmuje rozmiar tabu listy oraz maksymalną liczbę iteracji algorytmu. Funkcja pobiera losowe rozwiązanie, wyznacza jego wartość i przypisuje je jako najlepsze po czym inicjuje listę tabu. Następnie w pętli, która iteruje się przez określoną liczbę, generuje sąsiedztwo rozwiązania, oblicza ich wartość i paruje ze sobą. Następnie lista jest sortowana wg najlepszych rozwiązań. Po sortowaniu następuje iteracja owej listy aż do wyboru pierwszego sąsiada, który nie jest w liście tabu. Jeśli wybrany sąsiad jest lepszym rozwiązaniem od aktualnego to następuje nadpisanie najlepszego rozwiązania co kończy iteracje. Wybrane rozwiązanie jest dodawane do listy tabu. W przypadku gdy lista tabu jest pełna, usuwamu nastarszy element. Jeśli podaliśmy rozmiar listy jako 0 to lista jest nieskończenie wielka. Po osiągnięciu maksymalnej liczby iteracji pętli, funkcja zwraca najlepsze rozwiązanie, jego wartość oraz krzywą zbieżności
4. Algorytm Symulowanego wyżarzania - technika optymalizacji inspirowana procesem fizycznym, w którym materiał jest ogrzewany, a następnie schładzany. Pozwala to na eksplorację przestrzeni rozwiązań, akceptując gorsze rozwiązania z pewnymm prawdopodobieństwem, aby unkinąć utknięcia w lokalnych minimach
       - simulated_annealing - funkcja implemenyująca algorytm symulowanego rozwiązania, przyjmuje takie zmienne jak: początkowa temperatura, współczynnik chłodzenia, minimalna temperatura oraz liczba maksymalnych iteracji. Funkcja generuje losowe rozwiązanie i oblicza jego wartość po czym przypisuje je jako aktualne najlepsze rozwiązanie. Pętla wykonuje się dopóki temperatura jest większa od minimalnej i liczba iteracji nie przekracza maksymalnej. W pętli jest generowany losowy sąsiad, obliczana jest jego wartość po czym wyznaczan jest delta, czyli różnica pomiędzy aktualnie najlpeszym rozwiązaniem a nowo wygenerowanym. jJeśli delta jest mniejsza od zera lub losowa wartość jest mniejsza niż "exp(-delta / temperature(t))", sąsiad staje się nowym rozwiązaniem. Po osiągnięciu którejś z wytycznych pętla kończy się i zwraca najlepsze rozwiązanie, jego wartość oraz krzywą znieżności.
5. Algorytm genetyczny - technika optymalizacji insiprowana zasadami doboru naturalnego i genetyki.
     5.1. Metody krzyżowania
       - one_point_crossover - metoda krzyżowania jednopunktowego, któa dzieli rodziców w losowym punkcie i wymienia segmenty między nimi
       - two_point_crossover - metoda krzyżowania dwupunktowego, która wyiera dwa punkty podziału i wymienia segmenty między nimi
     5.2. Metody mutacji
       - swap_mutation - metoda mutacji przez zmianę, która wybiera dwa elementy w losowym podzbiorze i zmienia je miejscami
       - interchange_mutatuion - metoda mutacji przez wymianę, która wybiera elementy z dwóch różnych podzbiorów i zmienia je mijescami
     5.3. Warunki zakończenia
       - brak poprawy - no_imporvement - algorytm kończy działanie, gdy nie następuje poprawa przez określoną liczbę iteracji
       - liczba generacji - algorytm kończy działanie po osiągnięciu okręslonej liczby generacji
     5.4 Głowna pętla
   Funkcja generuje populacje losowych rozwiązań, znajduje w niej najlepsze rozwiązanie i przypisuje je pod zmienna.
   W następnej pętli dokonywana jest selekcja elity i dodanie jej do nowej populacji. Potem następuje tworzenie nowych dzieci, poprzez wybrane krzyżowanie, a następnie poprzez wybraną mutację i dodanie ich do nowej populacji. Posortowanie nowej populacji wg wartości rozwiązania i sprawdzenie najlepszego z nowej populacji z aktulnie najlepszym rozwiązaniem. Potencjalna wymiana najlepszego rozwiązania, po czym następuje sprawdzenie warunku zakończenia. Przy jego osiągnięciu zwracane jest najlepsze rozwiązanie, jego wartość oraz krzywa zbieżności.
     
