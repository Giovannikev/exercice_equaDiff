# Exercice 4 – Système Linéaire d'Équations Différentielles

## Description
Cet exercice explore la résolution numérique et la visualisation des portraits de phase pour un système linéaire d'équations différentielles ordinaires. Il utilise `numpy` pour la manipulation des matrices, `matplotlib` pour la visualisation, et `scipy.integrate.solve_ivp` pour la résolution numérique du système.

## Modèle Mathématique
Un système linéaire d'équations différentielles du premier ordre peut être représenté sous la forme matricielle :
$$ \frac{dX}{dt} = AX $$
où :
- $X(t)$ est un vecteur de fonctions dépendant du temps, $X(t) = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix}$.
- $A$ est une matrice carrée de coefficients constants.

Dans cet exercice, la matrice $A$ est définie comme :
$$ A = \begin{pmatrix} 3 & -4 \\ 1 & 1 \end{pmatrix} $$
Le système d'équations différentielles est donc :
$$ \begin{cases}
\frac{dx}{dt} = 3x - 4y \\
\frac{dy}{dt} = x + y
\end{cases} $$

## Implémentation Python

Le fichier `systeme_lineaire.py` définit la matrice $A$, la fonction du système `f`, et utilise `solve_ivp` pour trouver la solution et tracer le portrait de phase.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the matrix A for the linear system
A = np.array([[3, -4],[1, 1]], float)

def f(t, X):
    """
    Defines the right-hand side of the differential equation dX/dt = A @ X.

    Args:
        t (float): Current time (not explicitly used in this autonomous system).
        X (np.array): Current state vector [x, y].

    Returns:
        np.array: The derivative dX/dt.
    """
    return A @ X

if __name__ == "__main__":
    # Solve the initial value problem
    # f: the system of differential equations
    # [0, 5]: time span for the integration
    # y0=[1,0]: initial conditions for x and y
    # t_eval: specific time points to evaluate the solution
    sol = solve_ivp(f, [0, 5], y0=[1,0], t_eval=np.linspace(0,5,400))

    # Extract x and y components from the solution
    x, y = sol.y

    # Plot the phase portrait
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Portrait de phase (système linéaire)")
    plt.axis("equal") # Ensures equal scaling for x and y axes
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **`A = np.array([[3, -4],[1, 1]], float)`** : Définit la matrice des coefficients du système linéaire.
- **`f(t, X)`** : Cette fonction représente le côté droit du système d'équations différentielles, $AX$. Elle prend le temps `t` (non utilisé car le système est autonome) et le vecteur d'état `X` en entrée, et retourne le produit matriciel `A @ X`.
- **Bloc `if __name__ == "__main__":`** :
    - **`solve_ivp(f, [0, 5], y0=[1,0], t_eval=np.linspace(0,5,400))`** : Cette fonction de `scipy.integrate` est utilisée pour résoudre le problème de valeur initiale.
        - `f` est la fonction définissant le système.
        - `[0, 5]` est l'intervalle de temps sur lequel intégrer.
        - `y0=[1,0]` sont les conditions initiales pour $x(0)$ et $y(0)$.
        - `t_eval` spécifie les points de temps où la solution doit être évaluée.
    - **`x, y = sol.y`** : Extrait les composantes $x(t)$ et $y(t)$ de la solution.
    - `matplotlib.pyplot` est utilisé pour tracer le portrait de phase ($y$ en fonction de $x$).
    - Les étiquettes des axes, le titre et `plt.axis("equal")` (pour une échelle égale des axes) sont définis.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy`, `matplotlib` et `scipy` installés. Ensuite, exécutez le script Python :
```bash
python systeme_lineaire.py
```
Ceci affichera le portrait de phase du système linéaire d'équations différentielles.
