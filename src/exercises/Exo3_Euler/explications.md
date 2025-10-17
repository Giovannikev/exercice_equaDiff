# Exercice 3 – Méthode d'Euler

## Description
Cet exercice présente la méthode d'Euler, une technique numérique fondamentale pour approximer les solutions d'équations différentielles ordinaires (EDO). Il utilise `numpy` pour les calculs et `matplotlib` pour la visualisation des résultats.

## Modèle Mathématique et Méthode d'Euler
Considérons une équation différentielle du premier ordre de la forme :
$$ \frac{dy}{dt} = f(t, y) $$
avec une condition initiale $y(t_0) = y_0$.

La méthode d'Euler est une méthode numérique itérative qui permet d'approximer la solution $y(t)$ à des pas de temps discrets. Pour un pas de temps $h$, l'approximation de $y$ au temps $t_{k+1} = t_k + h$ est donnée par :
$$ y_{k+1} = y_k + h \cdot f(t_k, y_k) $$

Dans cet exercice, l'équation différentielle spécifique est celle de la croissance exponentielle :
$$ \frac{dy}{dt} = ry $$
Donc, $f(t, y) = ry$. L'itération d'Euler devient :
$$ y_{k+1} = y_k + h \cdot r y_k $$

## Implémentation Python

Le fichier `euler_method.py` contient la fonction `euler` qui implémente la méthode et un bloc principal pour la visualisation.

```python
import numpy as np
import matplotlib.pyplot as plt

def euler(y0=100, r=0.2, h=0.1, t_max=10.0):
    """
    Applies Euler's method to solve the differential equation dy/dt = r*y.

    Args:
        y0 (float): Initial value of y (default: 100).
        r (float): Growth rate (default: 0.2).
        h (float): Step size (default: 0.1).
        t_max (float): Maximum time for the simulation (default: 10.0).

    Returns:
        tuple: A tuple containing two numpy arrays (t, y).
               t: Array of time points.
               y: Array of approximated y values at each time point.
    """
    n = int(t_max / h)  # Number of steps
    t = np.linspace(0, t_max, n + 1) # Time points
    y = np.zeros_like(t) # Initialize y array
    y[0] = y0 # Set initial condition

    # Euler's method iteration
    for k in range(n):
        y[k+1] = y[k] + h * r * y[k]
    return t, y

if __name__ == "__main__":
    # Run Euler's method with default parameters
    t, y = euler()

    # Plot the results
    plt.plot(t, y)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("Euler sur y' = r y")
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **`euler(y0=100, r=0.2, h=0.1, t_max=10.0)`** : Cette fonction implémente la méthode d'Euler :
    - `n` est le nombre de pas de temps calculé à partir de `t_max` et `h`.
    - `t` est un tableau `numpy` des points de temps.
    - `y` est un tableau `numpy` initialisé avec `y0` comme condition initiale.
    - La boucle `for` applique la formule d'itération d'Euler pour calculer `y` à chaque pas de temps.
- **Bloc `if __name__ == "__main__":`** :
    - La fonction `euler` est appelée pour obtenir les points de temps `t` et les valeurs `y` approximées.
    - `matplotlib.pyplot` est utilisé pour tracer le graphique de `y(t)` en fonction de `t`.
    - Les étiquettes des axes et le titre du graphique sont définis.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy` et `matplotlib` installés. Ensuite, exécutez le script Python :
```bash
python euler_method.py
```
Ceci affichera un graphique de la solution approximée par la méthode d'Euler.
