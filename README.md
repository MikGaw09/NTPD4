# NTPD4

## Zadanie 1 
## Plik requirements zawiera wszystkie potrzebne do działania biblioteki. Ponadto do poprawnego działania kontenera dodano uvicorn tak aby nie aplikacja nie wyłączała się od razu po uruchomieniu kontenera
<img width="178" height="121" alt="image" src="https://github.com/user-attachments/assets/3faf2248-5b3f-495d-9438-10ddaf6d1b7d" />

## Zadanie 2
## plik Dockerfile uruchamia aplikacje poprzez uvicorna, wciągając do kontenera wszystkie wymagane biblioteki z pliku requirements
<img width="539" height="294" alt="image" src="https://github.com/user-attachments/assets/21f4d448-66bd-400b-b372-c59651586dd1" />

<img width="239" height="35" alt="image" src="https://github.com/user-attachments/assets/08c8cea5-4de9-47c7-a812-1500385df1fc" />
<img width="768" height="55" alt="image" src="https://github.com/user-attachments/assets/a38db311-bdc4-4c8c-8c51-9afe4b7e1c39" />

## Zadanie 3 
## Komenda docker run pozwala na uruchamianie utworzonych kontenerów. Port aplikacji został ustawiony na 8000 zgodnie z poleceniem. Za pomocą swaggera przetestowałem endpoint predict
<img width="325" height="26" alt="image" src="https://github.com/user-attachments/assets/611c837d-dde3-4384-a822-f55ae1df60da" />

<img width="709" height="424" alt="image" src="https://github.com/user-attachments/assets/75126f4b-7ff7-4c41-a69a-56e8d0fd59d2" />

## Zadanie 4
## Zbudowanie kontenera compose polegało na stworzeniu pliku compose.yml w którym dodawane są kolejne komponenty. W tym przykładzie dodano stworzona wczesniej aplikacje oraz bazę danych redis. Endpoint został sprawdzony przy użyciu postmana. Redis sprawdziłem przy pomocy exec tak aby dostać się do bazy, a następnie wysłałem komunikat ping 
<img width="392" height="530" alt="image" src="https://github.com/user-attachments/assets/c94ca3e2-0610-43fb-95d0-512d29edf0e4" />

<img width="281" height="31" alt="image" src="https://github.com/user-attachments/assets/d337e8dd-b12f-4ad3-9c18-0af2bdd52c96" />

<img width="455" height="490" alt="image" src="https://github.com/user-attachments/assets/48750e6b-1bd9-438c-9a3c-834044f0804e" />

<img width="781" height="74" alt="image" src="https://github.com/user-attachments/assets/5e116084-57c2-4a2e-80f1-2f636164d02f" />

## Zadanie 5

# Instrukcja uruchamiania
## Lokalnie
1. Instalacja bibliotek requirements.txt:
pip install -r requirements.txt
2. Uruchomienie aplikacji poprzez uvicorn 
uvicorn app:app --host 127.0.0.1 --port 8000
3. Aplikacja działa pod url: http://127.0.0.1:8000

## Docker 
1. Obraz aplikacji
docker build -t iris-app .
2. Uruchomienie kontenera
docker run -p 8000:8000 iris-app
3. Aplikacja działa pod url: http://localhost:8000

## Docker Compose
1. Uruchamianie compose
docker compose up --build[
2. Aplikacja działa pod url: http://localhost:8000

# Wymagania i konfiguracja
## Zasoby
1. Zainstalowany Docker na maszynie
2. Pliki app.py, requirements.txt, model_iris_v1.pkl 
