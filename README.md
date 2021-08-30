# Sistema Especialista em Indicação de SmartPhone

Sistema de Inteligência Artificial utilizando máquina de inferência para indicação de smartphone para o usuário

## Informações sobre o Projeto

* **Equipe:** Lucas A. Lisboa, João Victor Ribeiro Ferro e Eduardo Lisboa;
* **IDE:** Visual Studio 2017;
* **Linguagem:** Python;
* **Bibliotecas:** Experta, PIL e tkinter;

## Base de Dados
| MARCA    | MODELO              | RAM   | CAMERA FRONTAL       | CAMERA PRINCIPAL           | MEMÓRIA SECUNDÁRIA | QTD CHIPS | BATERIA  | RESOLUÇÃO          | TAMANHO DA TELA | PREÇO       |
| -------- | ------------------- | ----- | -------------------- | -------------------------- | ------------------ | --------- | -------- | ------------------ | --------------- | ----------- |
| APPLE    | iPhone 6S           | 2 GB  | 5 Mp                 | 12 Mp                      | 128 GB             | 1         | 1715 mAh | 750 x 1334 pixels  | 4.7             | R$ 1.749,00 |
| APPLE    | iPhone X            | 3 GB  | 7 Mp                 | 12 Mp + 12 Mp              | 256 GB             | 1         | 2716 mAh | 1125 x 2436 pixels | 5.8             | R$ 3.799,00 |
| APPLE    | iPhone 12           | 6 GB  | 12 Mp                | 12 Mp + 12 Mp + 12 Mp      | 512 GB             | 1         | 2815 mAh | 1170 x 2532 pixels | 6.1             | R$ 7.199,00 |
| ASUS     | ZenFone 7 Pro       | 8 GB  | 64 Mp + 12 Mp + 8 Mp | 64 Mp + 12 Mp + 8 Mp       | 256 GB             | 2         | 5000 mAh | 1080 x 2400 pixels | 6.67            | R$ 6.497,00 |
| ASUS     | ZenFone 5           | 4 GB  | 8 Mp                 | 12 Mp + 8 Mp               | 64 GB              | 2         | 3300 mAh | 1080 x 2246 pixels | 6.2             | R$ 1.799,00 |
| ASUS     | ZenFone 6           | 6 GB  | 48 Mp + 13 Mp        | 48 Mp + 13 Mp              | 64 GB              | 2         | 5000 mAh | 1080 x 2340 pixels | 6.4             | R$ 3.799,00 |
| LG       | LG Velvet           | 6 GB  | 16 Mp                | 48 Mp + 8 Mp + 5 Mp        | 128 GB             | 2         | 4300 mAh | 1080 x 2460 pixels | 6.8             | R$ 2.299,00 |
| LG       | LG K62              | 4 GB  | 13 Mp                | 48 Mp + 5 Mp + 2 Mp + 2 Mp | 64 GB              | 2         | 4000 mAh | 8000 x 6000 pixels | 6.6             | R$ 1.049,00 |
| MOTOROLA | Motorola One Action | 4 GB  | 12 Mp                | 12 Mp + 5 Mp + 16 Mp       | 128 GB             | 2         | 3500 mAh | 1080 x 2520 pixels | 6.3             | R$ 1.149,00 |
| MOTOROLA | Motorola Moto G100  | 12 GB | 16 Mp                | 64 Mp + 16 Mp + 2 Mp       | 256 GB             | 2         | 5000 mAh | 1080 x 2520 pixels | 6.7             | R$ 2.852,00 |
| MOTOROLA | Motorola Moto E6i   | 2 GB  | 5 Mp                 | 13 Mp + 2 Mp               | 32 GB              | 2         | 3000 mAh | 720 x 1560 pixels  | 6.1             | R$ 699,00   |
| SAMSUNG  | Samsung Galaxy A31  | 4 GB  | 20 Mp                | 48 Mp + 8 Mp + 5 Mp + 5 Mp | 128 GB             | 2         | 5000 mAh | 1080 x 2400 pixels | 6.4             | R$ 1.619,00 |
| SAMSUNG  | ‎Samsung Galaxy S21 | 8 GB  | 10 Mp                | 12 Mp + 64 Mp + 12 Mp      | 256 GB             | 2         | 4000 mAh | 1080 x 2400 pixels | 6.2             | R$ 3.869,00 |
| SAMSUNG  | Samsung Galaxy A21s | 4 GB  | 13 Mp                | 48 Mp + 8 Mp + 2 Mp + 2 Mp | 64 GB              | 2         | 5000 mAh | 720 x 1600 pixels  | 6.5             | R$ 1.435,00 |
| XIAOMI   | Mi 9T               | 6 GB  | 20 Mp                | 48 Mp + 8 Mp + 13 Mp       | 128 GB             | 2         | 4000 mAh | 1080 x 2340 pixels | 6.39            | R$ 1.340,00 |
| XIAOMI   | Poco F3             | 6 GB  | 20 Mp                | 48 Mp + 8 Mp + 5 Mp        | 128 GB             | 2         | 4520 mAh | 1080 x 2400 pixels | 6.67            | R$ 2.679,00 |
| XIAOMI   | Mi 11               | 8 GB  | 20 Mp                | 108 Mp + 13 Mp + 5 Mp      | 256 GB             | 2         | 4600 mAh | 1440 x 3200 pixels | 6.81            | R$ 7.189,00 |

## Árvore de Decisão 
![Árvore de decisão.png](https://github.com/joaovictorferro/I.A/blob/main/%C3%81rvore%20de%20decis%C3%A3o.png)
