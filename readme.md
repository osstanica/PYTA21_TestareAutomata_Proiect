# PYTA21 Testare Automata

Acest proiect a fost dezvoltat ca parte din cerințele pentru obținerea diplomei în Programare Python și Testare Automată în cardul Academiei {IT} Factory. 


## Documentation
Proiectul folosește un framework de tip UnitTest pentru a testa site-ul demo https://www.saucedemo.com/, un magazin online, și a fost scris în Python, folosind IDE-ul PyCharm Community Edition, 2025.1.1.1.

Testele sunt grupate în fișiere .py în funcție de pagina aplicației care conține funcționalitatea testată. 
Fiecare fișier cu teste din directorul */tests* are un echivalent în */setup* din care moștenește variabile, constante și metode specifice funcționalităților de pe pagina respectivă.

Sunt testate următoarele aspecte ale magazinului online:

- **login tests**:  
  - verificarea logării cu credențiale greșite (test_login_incorrect_credentials), 
  - verificarea logării cu credențiale corecte (test_login_correct_credentials);
- **inventory tests**: 
  - verificarea sortării alfabetice în mod default (test_az_default_sorting), 
  - verificarea celorlalte modalități de sortare (test_other_sorting), 
  - verificarea funcționalității de adăugare produs în coș (test_product_added_to_cart);
- **product tests**: 
  - verificarea detaliilor produsului de pe pagina dedicată (test_product_details), 
  - verificarea butonului de întoarcere pe pagina de inventar (test_return_to_inventory_page);
- **cart tests**: 
  - verificare detaliilor coșului (test_cart_details), 
  - verificarea butonului de continuare a cumpărăturilor (test_continue_shopping_functionality);
- **checkout tests**: 
  - verificare procesului end-to-end de comandare a unui produs (test_checkout_process), 
  - verificarea sumelor TVA și preț total pentru produsul comandat (test_total_price_value).

În directorul */runner* se regăsește runner-ul testelor. 
Utilizând clasa TestSuite din framework-ul unittest, se crează o colecție de teste (toate testele menționate anterior), iar prin intermediul package-ului HTMLTestRunner această suită este rulată, iar rezultatele sunt formatate ca un raport HTML, salvat în */runner/reports*, cu numele "Saucedemo_Test_Report_*yyyy-mm-dd*_*hh-mm-ss*".

## Deployment


Este necesară crearea unui mediu virtual, cu următoarele pachete instalate: 

[![python](https://img.shields.io/badge/python-3.12.0-gree)](https://www.python.org/downloads/release/python-3120/)
[![selenium](https://img.shields.io/badge/selenium-4.33.0-gree)](https://pypi.org/project/selenium/)
[![html-testrunner](https://img.shields.io/badge/html--testrunner-1.2.1-gree)](https://pypi.org/project/html-testRunner/)


## Running Tests

Pentru a rula testele din acest proiect din terminal trebuie utilizată următoarea comandă: 

```bash
  .\.venv\Scripts\python.exe .\runner\test_suites.py TestSuite.test_suite
```

Alternativa este opțiunea de Run Test din IDE pe metoda *test_suite* din *runner/test_suites.py*.


## Screenshots

**Exemplu de raport:** 
![Image](https://github.com/user-attachments/assets/c529ea04-38ef-47be-bad7-748cf463282a)


## Authors

- [@osstanica](https://github.com/osstanica)