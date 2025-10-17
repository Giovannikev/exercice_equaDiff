# Exercice 6 – Système Dynamique avec Classe

## Description
Cet exercice présente une implémentation orientée objet de la méthode d'Euler pour la résolution numérique d'équations différentielles ordinaires (EDO). Il encapsule la logique de résolution dans une classe `SystemeDynamique`, permettant une approche plus modulaire et réutilisable. Il utilise `numpy` pour les calculs et `matplotlib` pour la visualisation.

## Modèle Mathématique et Méthode d'Euler
Le cadre général est la résolution d'une équation différentielle du premier ordre de la forme :
$$ \frac{dy}{dt} = f(t, y) $$
avec une condition initiale $y(t_0) = y_0$.

La méthode d'Euler est appliquée pour approximer la solution $y(t)$ à des pas de temps discrets $t_k$. L'itération est donnée par :
$$ y_{k+1} = y_k + h \cdot f(t_k, y_k) $$

Dans l'exemple fourni, l'équation différentielle résolue est :
$$ \frac{dy}{dt} = -0.1y + 2 $$
Ici, $f(t, y) = -0.1y + 2$.

## Implémentation Python

Le fichier `systeme_dynamique.py` contient la classe `SystemeDynamique` et un bloc principal pour l'instanciation et la visualisation.

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

class SystemeDynamique:
    """
    A class to represent and solve a dynamic system using Euler's method.
    """
    def __init__(self, f: Callable[[float, float], float], y0: float, t_max: float, h: float):
        """
        Initializes the dynamic system.

        Args:
            f (Callable[[float, float], float]): The function f(t, y) defining the ODE dy/dt = f(t, y).
            y0 (float): Initial value of y.
            t_max (float): Maximum time for the simulation.
            h (float): Step size.
        """
        self.f = f
        self.y0 = y0
        self.t_max = t_max
        self.h = h

    def euler(self):
        """
        Applies Euler's method to solve the ODE.

        Returns:
            tuple: A tuple containing two numpy arrays (t, y).
                   t: Array of time points.
                   y: Array of approximated y values at each time point.
        """
        n = int(self.t_max / self.h)  # Number of steps
        t = np.linspace(0, self.t_max, n + 1) # Time points
        y = np.zeros_like(t) # Initialize y array
        y[0] = self.y0 # Set initial condition

        # Euler's method iteration
        for k in range(n):
            y[k+1] = y[k] + self.h * self.f(t[k], y[k])
        return t, y

if __name__ == "__main__":
    # Define the function f(t, y) for the ODE y' = -0.1y + 2
    f = lambda t, y: -0.1 * y + 2

    # Instantiate the SystemeDynamique class
    sys = SystemeDynamique(f, y0=0.0, t_max=50.0, h=0.1)

    # Solve the ODE using Euler's method
    t, y = sys.euler()

    # Plot the results
    plt.plot(t, y)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("y' = -0.1y + 2 (Euler)")
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **Classe `SystemeDynamique`** :
    - **`__init__(self, f, y0, t_max, h)`** : Le constructeur initialise le système avec la fonction `f` (le côté droit de l'EDO), la condition initiale `y0`, le temps maximal de simulation `t_max` et le pas de temps `h`.
    - **`euler(self)`** : Cette méthode implémente la méthode d'Euler. Elle calcule le nombre de pas, initialise les tableaux de temps `t` et de solution `y`, puis itère pour appliquer la formule d'Euler à chaque pas.
- **Bloc `if __name__ == "__main__":`** :
    - **`f = lambda t, y: -0.1 * y + 2`** : Définit la fonction `f(t, y)` pour l'EDO spécifique à résoudre.
    - **`sys = SystemeDynamique(f, y0=0.0, t_max=50.0, h=0.1)`** : Crée une instance de la classe `SystemeDynamique` avec les paramètres de l'EDO.
    - **`t, y = sys.euler()`** : Appelle la méthode `euler` de l'instance pour obtenir la solution numérique.
    - `matplotlib.pyplot` est utilisé pour tracer le graphique de `y(t)` en fonction de `t`.
    - Les étiquettes des axes et le titre du graphique sont définis.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy` et `matplotlib` installés. Ensuite, exécutez le script Python :
```bash
python systeme_dynamique.py
```
Ceci affichera un graphique de la solution numérique de l'EDO par la méthode d'Euler.
