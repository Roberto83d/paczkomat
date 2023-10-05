# Inicjalizacja zmiennych
liczba_paczek = int(input("Ile paczek chcesz wysłać? "))
wagi_paczek = []
najwieksze_puste_kilogramy = 0
najwieksza_paczka_index = 0

# Pobieranie wag paczek
for i in range(liczba_paczek):
    waga = float(input("Podaj wagę paczki {} (w kilogramach): ".format(i + 1)))
    wagi_paczek.append(waga)
    puste_kilogramy = 20 - waga
    if puste_kilogramy > najwieksze_puste_kilogramy:
        najwieksze_puste_kilogramy = puste_kilogramy
        najwieksza_paczka_index = i

# Obliczenia
liczba_kilogramow_wyslanych = sum(wagi_paczek)
puste_kilogramy = liczba_paczek * 20 - liczba_kilogramow_wyslanych

# Wyświetlanie podsumowania
print("\nPodsumowanie:")
print("Liczba paczek wysłanych: ", liczba_paczek)
print("Liczba kilogramów wysłanych: ", liczba_kilogramow_wyslanych)
print("Suma 'pustych' kilogramów: ", puste_kilogramy)
print("Paczka o indeksie {} miała najwięcej 'pustych' kilogramów: {} kg.".format(najwieksza_paczka_index + 1, najwieksze_puste_kilogramy))
