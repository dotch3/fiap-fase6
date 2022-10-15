### Fase6 FIAP - GIVEMEAAHAND

This project is the implemenation of operations and use of AVL.

<p align="center">


----

<div align="center">


```zsh
> Jorge Mercado - RM89287
````

</div>

</p>

----

Before to run, ensure to have the libaries installed on the venv
#### Executing the program in command line:

Run the python command
```
python3 main.py
```


```sh
*******************************************************************************************
                        MENU
*******************************************************************************************

(1) - Add Person
(2) - Search person by id <DATABASE>
(3) - Search person by id <MEMORY>
(4) - Search by ALV 
(5) - Get All
(6) - Create Test Users using Fake
<0> - Exit
Enter your choice: 
```

### Running the stats.

```
python3 model/person.py       
```

```sh
*****_____STATS____*****

CREATE USER: --- 0.09753608703613281 seconds ---
GET ALL USERS:--- 0.09917998313903809 seconds ---
FIND_IN DATABASE:--- 0.09984207153320312 seconds ---
FIND_IN_MEMORY:--- 0.10058212280273438 seconds ---
SORT DATA AVL:--- 0.10141730308532715 seconds ---

FINAL STATS:--- 0.10143113136291504 seconds ---
```