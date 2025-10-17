# Exercice 5 – Modèle SIR

## Description
Cet exercice implémente le modèle épidémiologique SIR (Susceptible-Infectious-Recovered), un modèle compartimental simple utilisé pour décrire la dynamique de propagation d'une maladie infectieuse dans une population. Il utilise `numpy` pour les calculs, `matplotlib` pour la visualisation, et `scipy.integrate.solve_ivp` pour la résolution numérique du système d'équations différentielles.

## Modèle Mathématique (Modèle SIR)
Le modèle SIR divise la population en trois compartiments :
- **S** : Individus Susceptibles (non infectés mais pouvant le devenir).
- **I** : Individus Infectieux (infectés et capables de transmettre la maladie).
- **R** : Individus Rétablis (immunisés ou décédés, ne pouvant plus être infectés ni infecter).

Le système d'équations différentielles qui décrit l'évolution de ces populations est le suivant :
$$ \begin{cases}
\frac{dS}{dt} = -\beta SI \\
\frac{dI}{dt} = \beta SI - \gamma I \\
\frac{dR}{dt} = \gamma I
\end{cases} $$
où :
- $\beta$ (beta) est le taux de transmission (probabilité de transmission par contact entre un susceptible et un infectieux).
- $\gamma$ (gamma) est le taux de guérison (taux auquel les infectieux se rétablissent ou sont retirés de la population infectieuse).
- La population totale $N = S + I + R$ est supposée constante.

## Implémentation Python

Le fichier `sir_model.py` définit les paramètres du modèle, la fonction du système `sir`, et utilise `solve_ivp` pour trouver la solution et tracer l'évolution des populations.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Model parameters
beta, gamma, N = 0.002, 0.5, 1000 # Transmission rate, Recovery rate, Total population

def sir(t, y):
    """
    Defines the SIR model differential equations.

    Args:
        t (float): Current time.
        y (np.array): Current state vector [S, I, R].

    Returns:
        list: List of derivatives [dS/dt, dI/dt, dR/dt].
    """
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

if __name__ == "__main__":
    # Initial conditions: S, I, R
    y0 = [990, 10, 0] # 990 susceptible, 10 infected, 0 recovered

    # Time vector for simulation
    t = np.linspace(0, 30, 600) # Simulate for 30 days with 600 points

    # Solve the initial value problem
    # sir: the system of differential equations
    # [t[0], t[-1]]: time span for the integration
    # y0: initial conditions for S, I, R
    # t_eval: specific time points to evaluate the solution
    sol = solve_ivp(sir, [t[0], t[-1]], y0, t_eval=t)

    # Extract S, I, R components from the solution
    S, I, R = sol.y

    # Plot the results
    plt.plot(t, S, label="S")
    plt.plot(t, I, label="I")
    plt.plot(t, R, label="R")
    plt.legend() # Display legend for S, I, R
    plt.xlabel("t")
    plt.ylabel("Population")
    plt.title("Modèle SIR")
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **`beta, gamma, N = 0.002, 0.5, 1000`** : Définit les paramètres du modèle : taux de transmission (`beta`), taux de guérison (`gamma`) et population totale (`N`).
- **`sir(t, y)`** : Cette fonction implémente le système d'équations différentielles du modèle SIR. Elle prend le temps `t` et le vecteur d'état `y` (contenant S, I, R) en entrée, et retourne les dérivées `dS/dt`, `dI/dt`, `dR/dt`.
- **Bloc `if __name__ == "__main__":`** :
    - **`y0 = [990, 10, 0]`** : Définit les conditions initiales pour les populations Susceptibles, Infectieuses et Rétablies.
    - **`t = np.linspace(0, 30, 600)`** : Crée un vecteur temps pour la simulation sur 30 jours.
    - **`solve_ivp(sir, [t[0], t[-1]], y0, t_eval=t)`** : Résout le système d'équations différentielles.
        - `sir` est la fonction définissant le système.
        - `[t[0], t[-1]]` est l'intervalle de temps d'intégration.
        - `y0` sont les conditions initiales.
        - `t_eval` spécifie les points de temps où la solution est évaluée.
    - **`S, I, R = sol.y`** : Extrait les populations S, I, R de la solution.
    - `matplotlib.pyplot` est utilisé pour tracer l'évolution de S, I et R en fonction du temps.
    - Une légende, des étiquettes d'axes et un titre sont ajoutés.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy`, `matplotlib` et `scipy` installés. Ensuite, exécutez le script Python :
```bash
python sir_model.py
```
Ceci affichera un graphique montrant l'évolution des populations Susceptibles, Infectieuses et Rétablies au cours du temps.
