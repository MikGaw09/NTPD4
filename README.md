# SPRAWOZDANIE NTPD LAB 3
## Cel zajęć: Celem zajęć jest praktyczne łączenie endpointów api z modelami ml

# ZADANIE 1
## Stworzenie podstawowej aplikacji API
Po utworzeniu projektu FastAPI, stworzyłem endpoint który przesyła json z wiadomością:

<img width="307" height="112" alt="image" src="https://github.com/user-attachments/assets/5bb82439-e508-4cc4-a172-eb70f9313481" />

# ZADANIE 2
## Dodanie modelu ML i endpointu predykcji
Wykorzystałem model zbudowany na pierwszych zajęciach. Zaimportowałem go do pliku app.py, następnie stworzyłem endpoint post który przyjmuje jsona z parametrami 
kwiatów a następnie zwraca predykcje typu. 

<img width="390" height="360" alt="image" src="https://github.com/user-attachments/assets/34828475-c812-4e57-8cbc-56a35ecf9f2c" />

# ZADANIE 3
## Obsługa błędów i walidacja danych
Do aplikacji dodałem handler błędów, który opakowuje informacje o błędzie w jsona który posiada wiadomość odnoszącą się do typu błędu. 

<img width="401" height="440" alt="image" src="https://github.com/user-attachments/assets/b4b2d94a-7bcb-45d7-807a-e9c2e4c74772" />

# ZADANIE 4
## Rozszerzenie API o dodatkowe endpointy i dokumentację
Do aplikacji dodano dwa endpointy: Pierwszy z nich wskazuje czy serwer żyje a drugi podaje nam informacje o modelu

<img width="448" height="494" alt="image" src="https://github.com/user-attachments/assets/6c831e76-5d4d-4d48-aca7-8e4af32f359b" />
<img width="460" height="543" alt="image" src="https://github.com/user-attachments/assets/05b2b376-f4e4-45e9-97f9-8c9b1c255a1f" />

# ZADANIE 5
## Uruchomienie aplikacji w środowisku produkcyjnym
Po uruchomieniu przez uvicorn, aplikacja działa zgodnie z założeniem. 

<img width="990" height="314" alt="image" src="https://github.com/user-attachments/assets/a7febd23-4178-49d2-a1f0-1fa1a97fc49b" />



