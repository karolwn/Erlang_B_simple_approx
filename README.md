# Erlang_B_simple_approx

prosty skrypt testujący różne przybliżenia prawdopodobieństwa blokady modelu Erlanga B

założenia:
- liczba kanałów, n ∈ \[1, 10\]
- natężenie ruchu, ρ ∈ \[n, n + 0.99]

testowane przybliżenia:
- zaproponowane przez Vladimira Shakova (https://ieeexplore.ieee.org/document/5555345), B ≈ 1 - n/ρ
- rozwiązanie własne naiwne, B ≈ ρ - n
- rozwiązanie własne proste 1, B ≈ ((ρ - n) / n^2) + 1/n 
- rozwiązanie własne proste 2, B ≈ ((ρ - n) / n^2) + 2/n 
- rozwiązanie własne trudne, B ≈ ((ρ - n) / n^2) + ln(n)/n 

wykresy z wynikami umieszczono w katalogu results