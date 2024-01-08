# Capitolul 1. Tema proiectului

## Enunțarea temei proiectului

Proiectul propus constă în dezvoltarea și implementarea algoritmului
Monte Carlo Tree Search (MCTS) în contextul jocului clasic Tic Tac Toe.
Scopul acestui proiect este să exploreze și să demonstreze aplicarea
eficientă a algoritmului MCTS într-un mediu simplu și interactiv precum
jocul Tic Tac Toe.

## Motivul alegerii temei

Implementarea algoritmului Monte Carlo Tree Search (MCTS) în jocul Tic
Tac Toe a fost selectată din mai multe motive pertinente și
educaționale. Unul dintre principalele motive a fost interesul pentru
înțelegerea și explorarea conceptelor de inteligență artificială
aplicate într-un mediu ludic și interactiv. Tic Tac Toe este un joc
simplu, însă implementarea algoritmului MCTS în acest context oferă
oportunitatea de a explora în profunzime mecanismele de luare a
deciziilor și strategiile utilizate de algoritmi AI în rezolvarea
problemelor.

De asemenea, alegerea acestui proiect a fost determinată și de natura sa
didactică și educativă. Implementarea algoritmului MCTS în jocul Tic Tac
Toe oferă o modalitate accesibilă și captivantă de a explora și de a
înțelege conceptele complexe ale inteligenței artificiale, oferind în
același timp o perspectivă practică asupra modului în care acest
algoritm poate fi aplicat într-un mediu de divertisment.

Proiectul Tic Tac Toe bazat pe MCTS oferă o platformă interactivă și
distractivă pentru testarea și experimentarea diferitelor strategii AI
într-un cadru simplu și familiar. Abordarea proiectului vine și din
dorința de a obține o cunoaștere mai profundă a funcționării
algoritmilor AI și a posibilităților lor de aplicare în contexte
diverse, începând de la jocuri și continuând până la aplicații practice
și probleme complexe din domenii variate.

# Capitolul 2. Arhitectura generală

## Arhitectura orientată eveniment

Arhitectura orientată pe eveniment (Event-Driven Architecture - EDA)
reprezintă un model de proiectare a aplicațiilor software în care fluxul
de activități și interacțiuni este determinat de evenimente și reacțiile
la acestea. În contextul bibliotecii Pygame, care este utilizată pentru
dezvoltarea de aplicații grafice și jocuri în Python, conceptul de
arhitectură orientată pe eveniment joacă un rol esențial.

Pygame este un framework versatil care se pretează bine la utilizarea
unui model de programare orientat pe evenimente. În Pygame, evenimentele
pot fi diverse acțiuni sau interacțiuni, precum apăsarea unei taste,
mișcarea mouse-ului sau alte acțiuni ale utilizatorului.

Aplicațiile Pygame sunt structurate în jurul unui ciclu de evenimente
continuu (event loop), care ascultă și procesează evenimentele generate
de utilizator sau de sistem. Aceste evenimente sunt capturate și
prelucrate de aplicație pentru a răspunde la acțiunile utilizatorului
sau pentru a actualiza starea jocului.

![A black background with white lines Description automatically
generated](./media/image2.png)

Fig 1. Gestionarea evenimentelor lansate de utilizator

## Arhitectura orientată obiect

Arhitectura orientată pe obiect (Object-Oriented Architecture - OOA)
este un model de proiectare software care se concentrează pe organizarea
și structurarea aplicațiilor în jurul conceptelor de obiecte și
interacțiuni între acestea. În cadrul acestei arhitecturi, obiectele
reprezintă entități care conțin date și funcționalități asociate, și
sunt interconectate prin intermediul relațiilor și a interfețelor
definite.

Sabloanele de proiectare sunt soluții și principii recurente, folosite
pentru a rezolva probleme comune în proiectarea software și pentru a
îmbunătăți structura și eficiența aplicațiilor. Aceste sabloane sunt
bazate pe experiență și au fost dezvoltate pentru a ajuta dezvoltatorii
să abordeze și să rezolve problemele recurente într-un mod elegant și
eficient.

# Capitolul 3. Funcționalitatea

## 

## Implementare

Proiectul a implicat implementarea algoritmului MCTS în Python,
utilizând biblioteca Pygame pentru realizarea interfeței grafice (GUI)
interactive. Interfața grafică a fost structurată într-un grid de 3x3,
fiecare celulă având dimensiunea de 200x200 pixeli, reprezentând tabla
de joc pentru Tic Tac Toe.

În partea de jos a ferestrei GUI, a fost inclus un panou care afișează
scorul și un buton de reset pentru a începe un nou joc.

Algoritmul MCTS a fost integrat în logica jocului pentru a lua decizii
strategice în timp real. În fiecare rundă, algoritmul explorează
posibilele mișcări și utilizează metoda MCTS pentru a evalua și a alege
cea mai promițătoare mutare. Implementarea sa a permis jucătorilor să se
confrunte cu un adversar AI capabil să ofere o competiție deschisă și
inteligentă în jocul Tic Tac Toe.

![A screenshot of a game Description automatically
generated](./media/image3.png)

Fig. 2. Fereastra aplicației la finalul unui joc

## 

## 

## Controale

-   **Selectarea unei celule:** Jucătorul poate interacționa cu tabla de
    joc prin simpla apăsare a clicului pe una din celulele grid-ului de
    3x3. Aceasta reprezintă mișcarea jucătorului și plasează simbolul
    corespunzător (X sau O) în celula selectată. Interfața grafică
    reacționează la această acțiune, permițând jucătorului să efectueze
    mutarea dorită.

-   **Rularea algoritmului AI:** După ce jucătorul face o mutare,
    algoritmul AI bazat pe Monte Carlo Tree Search (MCTS) intră în
    acțiune. Interfața grafică așteaptă răspunsul algoritmului și
    afișează mutarea AI-ului, oferind o reacție vizuală în joc. Astfel,
    jocul continuă într-un ciclu alternant între mișcările jucătorului
    și ale AI-ului.

-   **Resetarea jocului:** Utilizatorii au posibilitatea să reseteze
    jocul și să înceapă o nouă partidă prin intermediul butonului de
    reset. Fiecare clic pe butonul de reset împiedică desfășurarea
    jocului curent și readuce tabla de joc la starea inițială. Această
    opțiune permite jucătorilor să înceapă o partidă nouă în orice
    moment.

# Capitolul 4. Rolul fiecărui membru al echipei

## 

## Implementare

Realizarea elementelor grafice, precum si logica jocului au fost
implementate de Constantin Ciobanu si Sebastian Hofman. Implementarea
algoritmului de X si 0, cat si elementele statistice necesare pentru
simulare folosind algoritmul propus au fost realizate si documentate de
Mihai Nejneriu, iar implementarea algoritmului de simulare pe Arbori
Monte Carlo a fost realizata de Andrei-Iosif Ioja.

## Documentație

Documentarea legata de logica jocului si analiza complexității
secvențelor din algoritm, precum si analiza corectitudinii funcției de
căutare au fost realizate de Mihai Nejneriu si Sebastian Hofman. Restul
documentației a fost realizata de Andrei-Iosif Ioja si Constantin
Ciobanu.

# Capitolul 5. Complexitatea în cazul cel mai favorabil, cel mai defavorabil, în cazul mediu. Demonstrația corectitudinii pentru funcția de cautare pe Arbori Monte Carlo

## Scopul funcției

Această metodă implementează algoritmul Monte Carlo Tree Search (MCTS)
pentru a determina cea mai bună mutare pentru AI în jocul dat.
Algoritmul MCTS este împărțit în mai multe etape:

1.  **Selection:** Algoritmul alege cel mai bun copil al nodului curent
    (conform UCB - Upper Confidence Bound) până când ajunge la o stare
    care nu este complet expandată sau la o stare finală de joc.

2.  **Expansion:** Dacă nodul curent nu este complet expandat și jocul
    nu s-a încheiat, algoritmul generează și adaugă noi noduri în
    arborele MCTS, reprezentând posibilele mutări în joc. Se asigură că
    noile noduri sunt distincte pentru a nu repeta aceeași configurație
    a tablei.

3.  **Simulation:** Se realizează un număr specific de simulări
    aleatorii pentru a evalua stările generate în urma extinderii
    arborelui. Aceste simulări sunt folosite pentru a obține o estimare
    a câștigului potențial pentru fiecare stare.

4.  **Backpropagation:** Se actualizează statisticile de vizită și
    câștig ale nodurilor parinte în funcție de rezultatele simulărilor.

Pentru a analiza complexitatea spațiului:

-   **Numărul total de noduri:** În fiecare iterație a algoritmului
    MCTS, se adaugă sau actualizează noduri în arbore. Numărul de noduri
    create sau modificate în timpul iterațiilor va depinde de factori
    precum numărul total de iterații și cât de mult este extins arborele
    în fiecare iterație.

-   **Memoria asociată fiecărui nod:** Fiecare nod reține informații
    precum starea jocului, părintele, copiii, numărul de vizite și
    numărul de victorii. Acest lucru ocupă o anumită cantitate de
    memorie pentru fiecare nod creat.

Dacă numărul total de iterații este $n$ și se estimează că arborele are
o adâncime maximă de $d$ nivele, complexitatea spațiului pentru arborele
MCTS poate fi aproximativ:

-   **Numărul total de noduri:** În general, numărul total de noduri din
    arbore este direct legat de numărul de iterații și de modul în care
    sunt extinse ramurile arborelui în timpul căutării. Complexitatea
    poate fi în jurul valorii $O(n)$ sau $O(b^{D})$, unde $b$ este
    factorul de ramificare mediu al arborelui.

-   **Memorie asociată fiecărui nod:** Cantitatea de memorie asociată
    fiecărui nod poate varia, dar în mod tipic nu este direct
    proporțională cu adâncimea arborelui, deoarece nodurile din niveluri
    mai profunde nu sunt complet expandate. Fiecare nod poate necesita o
    cantitate constantă de memorie pentru a stoca informațiile necesare.

## Complexitatea în cazul cel mai favorabil

În cazul cel mai favorabil, analiza complexității timpului pentru
algoritmul Monte Carlo Tree Search (MCTS) poate fi detaliată astfel:

1.  **Selecție și Extindere:**

-   **Seleție:** În cazul cel mai favorabil, algoritmul selectează mereu
    copilul cel mai promițător în fiecare pas. Aceasta ar avea o
    complexitate de timp O(1) pentru selecție întrucât se accesează
    direct copilul cu cea mai mare valoare UCB (Upper Confidence Bound).

-   **Extindere:** Dacă arborele nu este complet expandat, extinderea ar
    putea implica generarea unei singure mutări valide, iar verificarea
    distinctivității acesteia poate necesita O(n) timp pentru a se
    asigura că este un nou nod valid.

2.  **Simulare și Backpropagare:**

-   **Simulare:** În cazul ideal, simulările ar fi rapide și ar avea o
    complexitate constantă $O(1)$ pentru fiecare simulare.

-   **Backpropagare:** După fiecare simulare, actualizarea nodurilor
    până la rădăcină prin backpropagare necesită parcurgerea arborelui
    de la nodul curent până la rădăcină, având o complexitate de timp
    $O(D)$, unde $D$ reprezintă adâncimea arborelui.

3.  **Complexitate totală în funcție de iterații:**

Complexitatea totală în funcție de numărul de iterații ($N$) poate fi
exprimată aproximativ ca $O(N*D)$ în cazul cel mai favorabil, unde $D$
reprezintă adâncimea arborelui (adâncimea maximă posibilă a arborelui
MCTS).

## Complexitatea în cazul cel mai defavorabil

În cazul cel mai defavorabil, analiza complexității timpului pentru
algoritmul Monte Carlo Tree Search (MCTS) poate fi detaliată astfel:

1.  **Selecție și Extindere:**

-   **Seleție:** În cel mai defavorabil scenariu, selecția ar putea
    implica parcurgerea întregii ramuri a arborelui pentru a găsi cea
    mai promițătoare mutare. Acest lucru ar avea o complexitate de timp
    $O(b^{D})$, unde $b$ reprezintă factorul de ramificare și $D$ este
    adâncimea arborelui.

-   **Extindere:** Întrucât toate nodurile sunt complet expandate,
    procesul de extindere va continua să genereze și să verifice mutări
    noi, până când găsește una distinctă. Aceasta poate avea o
    complexitate de timp $O(N)$ pentru fiecare încercare de extindere a
    unui nod.

2.  **Simulare și Backpropagare:**

-   **Simulare:** În cel mai defavorabil caz, simulările ar putea
    implica explorarea complet aleatoare a posibilelor mișcări, cu o
    complexitate a timpului $O(M)$, unde $M$ reprezintă numărul total de
    mutări valide.

-   **Backpropagare:** După fiecare simulare, actualizarea nodurilor
    până la rădăcină prin backpropagare necesită parcurgerea arborelui
    de la nodul curent până la rădăcină, având o complexitate de timp
    O(D), unde D reprezintă adâncimea arborelui.

3.  **Complexitate totală în funcție de iterații:**

Complexitatea totală în funcție de numărul de iterații $(N)$ într-un
scenariu cel mai defavorabil poate fi foarte mare și dificil de estimat
precis. Ea poate fi influențată de adâncimea arborelui, de factorul de
ramificare, de numărul de mutări valide și de modul în care sunt
distribuite rezultatele simulărilor.

## Complexitatea în cazul mediu

În cazul complexității medii a algoritmului Monte Carlo Tree Search
(MCTS), este dificil să se ofere o analiză exactă datorită variațiilor
și a dependenței acesteia de diferite aspecte ale jocului și ale
implementării algoritmului.

Totuși, putem lua în considerare următoarele aspecte într-o analiză a
complexității în caz mediu:

1.  **Selecție și Extindere:**

    -   **Selecție:** În cazul mediu, selecția poate implica explorarea
        unei părți a arborelui și determinarea unei mutări promițătoare.
        Complexitatea timpului pentru selecție ar putea fi în general
        mai mică decât în cazul cel mai defavorabil și poate varia în
        funcție de distribuția optimă a mutărilor în arbore.

    -   **Extindere:** Extinderea poate implica generarea și verificarea
        unor mutări noi. În medie, algoritmul poate găsi mutări
        distincte mai rapid decât în cazul cel mai defavorabil, dar
        totuși va avea nevoie de timp pentru a asigura distincția
        fiecărei mutări generate.

2.  **Simulare și Backpropagare:**

    -   **Simulare:** În cazul mediu, simulările pot fi o combinație
        între explorare aleatoare și evaluare euristică pentru a obține
        o estimare a rezultatelor. Complexitatea timpului pentru
        simulare poate varia în funcție de strategia utilizată în
        simulări și de structura jocului.

    -   **Backpropagare:** Actualizarea valorilor nodurilor prin
        backpropagare se va face pentru fiecare simulare și va avea o
        complexitate de timp $O(D)$, în care $D$ este adâncimea
        arborelui.

3.  **Complexitate totală în funcție de iterații:**

Complexitatea totală în funcție de numărul de iterații $(N)$ în cazul
mediu este influențată de o combinație a tuturor acestor factori. În
general, este dificil de estimat exact complexitatea în cazul mediu,
deoarece acesta depinde de distribuția mutărilor, de strategia utilizată
în selecție, extindere și simulare și de alți factori specifici jocului.

## 

## 

## 

## 

## Codul secvenței de analizat

```python
def monte_carlo_tree_search(initial_state: Board, iterations: int, sim_number: int) -> Board:
    """
    Runs a Monte Carlo Tree Search algorithm with configuration
    :param sim_number: number of random simulations
    :param initial_state: current state of the board
    :param iterations: the number of iterations
    :return: the new board with the best move to play for AI
    """
    P0
    root = Node(initial_state)    A0
    P01
    I1
    for _ in range(iterations):    C1
        P1
        node = root, state = initial_state    A1
        P2
        
        I2
        while not state.check_game_over() and node.is_fully_expanded() and len(node.children) > 0:    C2
        P3
            node = node.get_best_child() A2
        P4
            state = copy.deepcopy(node.state) A3
        P5
        # FINAL I2

        P6
        # Expansion
        if not node.is_fully_expanded() and not node.state.check_game_over():     
              <-C3 
            P7
            empty_cells = state.get_none_indexes()    A4
            P8
            # Keep generate new vales until I find a new son
            I3
            while True:
                P9
                random_empty_cell = random.choice(empty_cells)    A5
                P10
                new_state = copy.deepcopy(state)    A6
                P11
                new_state.make_move(random_empty_cell[0], random_empty_cell[1])                                   
                                                      <-A7
                P12
                if check_distinct_child(new_state, node.children):    C4
                    P13
                    new_node = Node(new_state, parent=node)    A8
                    P14
                    node.children.append(new_node)    A9
                    P15
                    node = new_node    A10
                    P16
                    break
                P17
            # FINAL I3

        # Simulation
        P18
        state = node.state    A11
        P19
        results = random_simulations(state, sim_number)    A12
        P20

        # Backpropagation
        I4
        while node is not None:    C5
            P21
            node.visits += 1   A13
            P22
            current_player = '0'     if node.state.get_turn() == X_PLAYER_ID else 'X'    <-C6

            P24
            node.wins += results[current_player]    A16
            P25
            node = node.parent    A17
            P26
        # FINAL I4	
        P27
    
    # FINAL I1
    P28
    return root.get_best_child().state    A18
    P29
    Q
```
Secv. 1. Codul metodei ce va fi analizata

## Demonstrația corectitudinii funcției

> **Precondiții** - Initial_state este o matrice de 3x3 valida;
>
> **Postcondiții** - Se va obtine o matrice de 3x3 valida care contine
> un 0 in plus, reprezentand mutarea calculatorului
>
> Invariantul din bucla 1:

-   Denumire: I1

-   Semnificație: Verifica iterations posibilitati pentru urmatoarea
    mutare si o returneaza pe cea mai buna

> Invariantul din bucla 2:

-   Denumire: I2

-   Semnificație: Va alege cea mai buna frunza.

> Invariantul din bucla 3:

-   Denumire: I3

-   Semnificație: Alege in mod aleator urmatoarea mutare

> Invariantul din bucla 4:

-   Denumire: I4

-   Semnificație: Calculeaza scorul pentru nodul curent si pentru toti
    parintii acestuia

**Demonstrație bucla 1 bine definită:**

Iterations este mai mare decat 0 =\> se va executa cel putin odata.

**Demonstrație bucla 2 bine definită:**

Node nu va fi null deoarece incepe cu radacina.

Len(node.children) \> 0 =\> nu este frunza =\> se va executa cel putin
odata.

**Demonstrație bucla 3 bine definită:**

Conditia este „True" =\> se va executa cel putin odata.

**Demonstrație bucla 4 bine definită:**

Node nu este null =\> se va executa cel putin odata.

**Demonstrație I1:**

În fiecare iterație a buclei for, se face o iterare prin procesul de
selecție în algoritmul MCTS pentru a alege următoarea mutare
promițătoare. Se verifică că jocul nu s-a încheiat, că nodul curent este
complet expandat și că există cel puțin un copil sub nodul curent. Acest
invariant asigură că algoritmul continuă să exploreze arborele de joc în
funcție de condițiile date și să facă selecții până la atingerea
numărului total de iterații specificat.

Pentru a demonstra că bucla for se va opri, putem utiliza un argument
inductiv pentru a arăta că numărul finit de iterații specificat
(iterations) va conduce la finalizarea buclei.

**Demonstrația prin inducție:**

Presupunem că avem o buclă for care rulează pentru un anumit număr de
iterații, specificat de iterations.

**Pașii inductivi:**

1.  ***Cazul de bază:***

    -   Pentru iterations = 1, bucla se execută o singură dată și se
        oprește. Aceasta reprezintă cazul de bază pentru demonstrația
        noastră.

2.  ***Ipoteza inductivă:***

    -   Presupunem că pentru un anumit k (unde k reprezintă un număr
        natural), bucla for se oprește după k iterații.

3.  ***Pașii inductivi:***

    -   Demonstrez că pentru iterations = k + 1, bucla for se va opri.

> Dacă bucla se oprește după k iterații (conform ipotezei inductive),
> atunci adăugând încă o iterație (k + 1), bucla va continua să se
> execute și se va opri după această iterație suplimentară, deoarece
> numărul total de iterații specificat (iterations) a fost atins.

Astfel, având în vedere cazul de bază și pașii inductivi, putem
concluziona că bucla for se va opri după numărul specificat de iterații
iterations, fiecare iterație reprezentând o etapă în procesul
algoritmului Monte Carlo Tree Search.

**Demonstrație I2:**

Pentru a demonstra corectitudinea invariantului din bucla respectivă,
vom analiza fiecare condiție separat pentru a verifica dacă invariantul
este respectat:

1.  **not state.check_game_over()**: Această condiție verifică dacă
    jocul nu s-a încheiat încă. Invariantul nu este influențat de
    această condiție, deoarece se referă doar la verificarea stării
    jocului în sine.

2.  **node.is_fully_expanded()**: Verifică dacă nodul curent din
    arborele MCTS este complet expandat. Aceasta implică faptul că toate
    posibilitățile de mutare înseamnă că toate copiii posibili au fost
    creați sub nodul curent. Invariantul este influențat de această
    condiție, deoarece asigură că arborele este explorat într-o oarecare
    măsură și că selecția poate continua pe baza copiilor existenți.

3.  **len(node.children) \> 0**: Verifică dacă nodul curent are copii
    (adică mutări posibile). Acest lucru este important pentru a
    continua procesul de selecție și extindere a arborelui. Invariantul
    este influențat și de această condiție, deoarece selecția se bazează
    pe existența și calitatea copiilor disponibili.

**Invariantul rezultă din combinația acestor condiții:**

-   În timpul selecției, se asigură că jocul nu s-a încheiat încă (not
    state.check_game_over()), iar nodul curent este complet expandat
    (node.is_fully_expanded()). Aceasta indică faptul că arborele a fost
    explorat până la un anumit nivel și că selecția poate continua pe
    baza rezultatelor disponibile până în acel moment.

-   De asemenea, se asigură că există cel puțin un copil sub nodul
    curent (len(node.children) \> 0), ceea ce indică faptul că sunt
    disponibile cel puțin unele mutări posibile din starea curentă a
    jocului.

Această combinație de condiții asigură că algoritmul MCTS continuă să
exploreze și să selecționeze mutările într-un mod corespunzător, până
când se îndeplinesc anumite condiții de oprire sau limitare a
explorării. Astfel, invariantul din bucla while este respectat pentru a
menține corectitudinea algoritmului în timpul selecției și extinderii
arborelui MCTS.

**Demonstrație I3:**

Să analizăm corectitudinea invariantului pentru bucla dată:

1.  **while True:**: Această condiție specifică că bucla va rula
    continuu până când se îndeplinește o anumită condiție de ieșire
    (break). Aceasta indică faptul că se va continua generarea de noi
    mutări până când se găsește o mutare distinctă.

2.  **Generarea unei noi mutări (new_state):** În fiecare iterație a
    buclei, se alege aleatoriu o poziție goală din empty_cells și se
    realizează o nouă mutare pe baza acestei selecții. new_state
    reprezintă starea jocului după aplicarea acestei noi mutări.

3.  **Verificarea distincției noii mutări:** După ce o nouă mutare este
    generată, se verifică dacă aceasta este distinctă față de copiii
    nodului curent (node). Acest lucru se realizează cu ajutorul
    funcției check_distinct_child.

4.  **Crearea și adăugarea unui nou nod:** În cazul în care mutarea
    generată este distinctă, se creează un nou nod (new_node) asociat
    acestei mutări și se adaugă acest nod ca și copil al nodului curent
    (node.children). Ulterior, bucla se oprește (break), indicând
    găsirea unei mutări valabile.

**Invariantul acestei bucle este:**

-   Această buclă garantează că se generează în mod continuu noi mutări
    (new_state) până când se găsește o mutare distinctă față de copiii
    nodului curent (node).

-   Se asigură că, oricât de multe mutări noi sunt generate, doar
    mutările care sunt distincte și care nu se regăsesc deja în copiii
    nodului sunt adăugate în arbore.

Această buclă are ca scop garantarea găsirii unei mutări valabile și
distincte, păstrând o formă de explorare și extindere corespunzătoare a
arborelui Monte Carlo Tree Search.

**Demonstrație I4:**

Să analizăm corectitudinea invariantului pentru bucla de backpropagare:

1.  **while node is not None:**: Această condiție specifică că bucla de
    backpropagare va continua să ruleze până când se ajunge la rădăcina
    arborelui (node.parent = None). Aceasta asigură că se parcurge
    arborele de la nodul curent (node) până la rădăcină.

2.  **Incrementarea vizitelor (node.visits += 1):** În fiecare iterație,
    numărul de vizite pentru nodul curent (node.visits) este incrementat
    cu 1. Acest lucru ține evidența de câte ori a fost vizitat un nod în
    timpul procesului de simulare și selecție.

3.  **Actualizarea scorului câștigurilor (node.wins +=
    results\[current_player\]):** Se actualizează scorul câștigurilor
    pentru nodul curent (node.wins) în funcție de rezultatul simulării
    pentru jucătorul curent (current_player). Acest lucru este important
    pentru a reflecta rezultatele simulării în evaluarea nodurilor din
    arbore.

4.  **Deplasarea către nodul părinte (node = node.parent):** La fiecare
    iterație, se trece la nodul părinte pentru a continua backpropagarea
    către rădăcina arborelui.

**Invariantul acestei bucle este:**

-   Această buclă de backpropagare asigură actualizarea corectă a
    informațiilor pentru fiecare nod pe traseul de la un nod frunză la
    rădăcina arborelui.

-   Se asigură că informațiile precum numărul de vizite și scorul
    câștigurilor sunt actualizate corect pentru fiecare nod pe măsură ce
    se urcă către rădăcină.

**Partea formala inainte de bucle:**

P -\> P0

P0 -\> A0 -\> P01, se vor initializa datele

P01 -\> I1 -\> P28, se vor executa „iterations" iteratii.

P28 -\> A19 -\> P29, se va returna board-ul care contine mutarea
calculatorului.

P29 -\> Q

**Partea formala pentru Bucla 1:**

P1 -\> A1 -\> P2, se initializeaza variabilele

P2 -\> I2 -\> P3, se selecteaza nodul care urmeaza a fi procesat

P3 -\> A2 -\> P4, se trece la cel mai bun copil al acestuia

P4 -\> A3 -\> P5, se face o copie ca sa se evide modificari neasteptate

P6 & C3 -\> P7, exista continuare la joc

P7 -\> A4 -\> P8, va salva in empty_cells casutele goale care reprezinta
posibilele miscari viitoare

P8 -\> I3 -\> P18, se va efectua o noua mutare

P18 -\> A11 -\> P19, se va salva starea mutarii noi

P19 -\> A12 -\> P20, se va calcula scorul mutarii

P20 -\> I4 -\> P27, se vor actualiza mutarile anterioare cu noul scor.

**Partea formala pentru Bucla 2:**

> P2&c2 →A2→P4, pentru fiecare fiu neexploatat, il adaugam in lista de
> fii
>
> P4 -\> A3 -\> P5, pentru fiecare stare nou determinata, o salvez ca
> stare globala

**Partea formala pentru Bucla 3:**

P9 -\> A5 -\> P10, se va selecta o celula random

P10 -\> A6 -\> P11, se va salva o copie a starii

P11 -\> A7 -\> P12, se va actualiza copia starii cu mutarea selectata

P12 & C4 -\> P13, este o stare noua

P13 -\> A8 -\> P14, se va creea un nou nod

P14 -\> A9 -\> P15, se va adauga noul nod ca si copil a nodului curent

P15 -\> A10 -\> P16, se schimba noul curent ca fiind noul nod

P16 -\> P18, se termina bucla

P12 & not C4 -\> P17, noua stare a mai fost gasita.

P17 -\> P9

**Partea formala pentru Bucla 4:**

P21 -\> A13 -\> P22, se actualizeaza de cate ori a fost vizitat nodul
curent

P22 & C6 -\>P24, se va salva ca a castigat calculatorul

P22 & not C6 -\> P24, se va salva ca a castigat jucatorul

P24 -\> A16 -\> P25, se va actualiza scorul

P25 -\> A17, se va trece la urmatorul nod, acesta fiind parintele

**Funcția de terminare pentru bucla 1:**

S-a efectuat numarul dorit de iteratii =\> Va iesi din bucla

**Funcția de terminare pentru bucla 2:**

Cand se gaseste un nou copil care nu a fost deja ales. Se intra in
aceasta bucla doar daca exista un copil care nu a fost ales =\> Va iesi
din bucla

## 

**Funcția de terminare pentru bucla 3:**

Cand se gaseste un nou copil care nu a fost deja ales. Se intra in
aceasta bucla doar daca exista un copil care nu a fost ales =\> Va iesi
din bucla

## 

**Funcția de terminare pentru bucla 4:**

Radacina are ca si parinte „None", iar toate nodurile, fiind un arbore
fara ciclu, vor avea la un moment dat ca parinte Radacina =\> Va iesi
din bucla

# Capitolul 6. Teste pentru a demonstra buna funcționare a programului.

## Modulul de Testare 

Acest fragment de cod folosește simulări pentru a testa algoritmul MCTS
în jocul de X și O (Tic Tac Toe), evaluând performanța algoritmului
pentru diferite configurări ale numărului de simulări și iterațiilor.

1.  Se testează algoritmul MCTS utilizând diferite configurații de
    sim_numbers (numărul de simulări la fiecare iterație a algoritmului)
    și iterations (numărul total de iterații în algoritmul MCTS).

2.  Pentru fiecare combinație de sim_numbers și iterations, se rulează
    mai multe simulări (specificat de simulations), unde se evaluează
    câteva aspecte ale performanței algoritmului.

În timpul fiecărei simulări:

-   Se inițializează un nou joc (obiectul Board).

-   Se realizează mutări aleatoare până când jocul se încheie
    (check_game_over() returnează un rezultat diferit de None), adică
    până când cineva câștigă sau se ajunge la remiză.

-   Dacă jocul se încheie și \'X\' (reprezentând AI) câștigă, se
    înregistrează această înfrângere (total_losses).

-   Se repetă acest proces pentru un număr specificat de simulări.

La final, pentru fiecare combinație de sim_numbers și iterations, se
afișează procentul de înfrângeri în contextul numărului total de
simulări (simulations). Acest lucru oferă o măsură a performanței
algoritmului pentru aceste configurații specifice. De asemenea, se
afișează timpul scurs pentru fiecare set de simulări.

Acest fragment de cod oferă o modalitate de testare și evaluare a
eficacității algoritmului MCTS pentru jocul de X și O în funcție de
parametrii specificați.

## Rezultate

![A graph of a number of simulation Description automatically
generated](./media/image4.png)

Fig 3. Evolutia timpului de executie in functie de configuratie

În general, există anumite interpretări și tendințe care pot fi
observate în rezultatele algoritmului de MCTS în funcție de
configurațiile sim_numbers și iterations.

-   **Timpul de execuție și complexitatea computațională:** Cu cât avem
    mai multe simulări (sim_numbers), timpul total de execuție va crește
    în mod direct proporțional. Fiecare simulare presupune o serie de
    iterații, iar o creștere a numărului de simulări va crește de
    asemenea timpul total de execuție.

-   **Impactul iterațiilor:** Reducerea numărului de iterații
    (iterations) în timpul unei simulări poate duce la o scădere a
    timpului total de execuție, deoarece se face o cantitate mai mică de
    muncă în fiecare simulare individuală.

-   **Precizie și performanță:** Cu toate acestea, o scădere a numărului
    de iterații poate afecta, în general, precizia și performanța
    algoritmului. Cu cât sunt efectuate mai multe iterații în fiecare
    simulare, cu atât algoritmul are o mai mare șansă de a explora mai
    în profunzime spațiul de căutare și de a lua decizii mai bune.

-   **Compromis între timpul de execuție și performanță:** În practică,
    există un compromis între timpul de execuție și performanță. O
    alegere echilibrată a numărului de simulări și a numărului de
    iterații poate fi necesară pentru a obține un rezultat acceptabil
    într-un timp rezonabil.

## 

## Utilizarea algoritmului Monte Carlo Tree Search

Formula Upper Confidence Bound (UCB) este o componentă cheie în
algoritmul Monte Carlo Tree Search (MCTS). Această formulă este
utilizată pentru a selecta un nod copil în etapa de selecție a
algoritmului MCTS, având rolul de a ghida explorarea către nodurile care
par să ofere cele mai bune perspective de câștig.

Formula UCB este exprimată ca o combinație între două componente
principale: exploatarea și explorarea.

-   **Exploatarea:** Reprezintă evaluarea nodului copil în funcție de
    informațiile disponibile până în acel moment. Cu cât un nod are o
    rată de câștig mai mare (sau alte metrici relevante), cu atât este
    considerat mai promițător pentru a fi explorat mai adânc.

-   **Explorarea:** Vizează nodurile care nu au fost explore complet și
    care ar putea oferi informații utile pentru a lua decizii mai bune
    în viitor. Această componentă încurajează explorarea pentru a
    descoperi zone noi sau puțin investigate din arborele de căutare.

Formula UCB combină aceste două componente într-un mod echilibrat,
permițând algoritmului să aleagă nodurile care maximizează o anumită
metrică UCB pentru a decide ce nod să exploreze în continuare.

Formula UCB poate fi reprezentată matematic astfel:

​![A black and white background with text Description automatically
generated](./media/image5.png)

Prin utilizarea acestei formule, algoritmul MCTS selectează următorul
nod copil care maximizează valoarea UCB, combinând astfel exploatarea și
explorarea pentru a direcționa căutarea către zonele promițătoare din
arborele de căutare. Alegerea parametrului cc este crucială pentru
echilibrarea dintre explorarea și exploatarea optimă a spațiului de
căutare.

# Capitolul 7. Bibliografie

-   Monte Carlo Tree Search: a review of recent modifcations and
    applications, M. Świechowski, K. Godlewski, B, Sawicki, J. Mańdziuk,
    July 2022

-   Parallel Monte-Carlo Tree Search, Guillaume M.J-B. Chaslot, Mark
    H.M. Winands, and H. Jaap van den Heri

-   Introduction to Algorithms, [Thomas H.
    Cormen](https://carturesti.ro/autor/thomas_h._cormen), [Charles E.
    Leiserson](https://carturesti.ro/autor/charles_e._leiserson),
    [Ronald L. Rivest](https://carturesti.ro/autor/ronald_l._rivest),
    [Clifford Stein](https://carturesti.ro/autor/clifford_stein), Third
    Edition, 2009

-   <https://towardsdatascience.com/monte-carlo-tree-search-an-introduction-503d8c04e168>

-   <https://builtin.com/machine-learning/monte-carlo-tree-search>

-   <https://medium.com/swlh/tic-tac-toe-at-the-monte-carlo-a5e0394c7bc2>

-   <https://www.flaticon.com/free-icons/tic-tac-toe>

-   <https://vgarciasc.github.io/mcts-viz/>
