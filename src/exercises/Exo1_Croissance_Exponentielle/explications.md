# Exercice 1 – Croissance Exponentielle

## Description
Cet exercice modélise la croissance exponentielle d'une population ou d'une quantité au fil du temps. Il utilise la bibliothèque `numpy` pour les calculs numériques et `matplotlib` pour la visualisation graphique des résultats.

## Modèle Mathématique
La croissance exponentielle est décrite par l'équation différentielle suivante :
$$ \frac{dN}{dt} = rN $$
où :
- $N(t)$ est la quantité (ou population) au temps $t$.
- $r$ est le taux de croissance.

La solution analytique de cette équation différentielle, avec une condition initiale $N(0) = N_0$, est :
$$ N(t) = N_0 e^{rt} $$

## Implémentation Python

Le fichier `croissance_exponentielle.py` contient la fonction `solution` qui calcule la valeur de $N(t)$ et un bloc principal pour la visualisation.

```python
import numpy as np
import matplotlib.pyplot as plt

def solution(t, r=0.2, N0=100):
    """
    Calculates the exponential growth at time t.

    Args:
        t (float or np.array): Time.
        r (float): Growth rate (default: 0.2).
        N0 (float): Initial quantity (default: 100).

    Returns:
        float or np.array: Quantity at time t.
    """
    return N0 * np.exp(r * t)

if __name__ == "__main__":
    # Generate time points
    t = np.linspace(0, 20, 400)
    # Calculate corresponding quantities
    y = solution(t)

    # Plot the results
    plt.plot(t, y)
    plt.xlabel("t")
    plt.ylabel("N(t)")
    plt.title("Croissance exponentielle")
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **`solution(t, r=0.2, N0=100)`** : Cette fonction prend en entrée le temps `t`, le taux de croissance `r` (par défaut 0.2) et la quantité initiale `N0` (par défaut 100). Elle retourne la valeur de $N(t)$ en utilisant la formule de croissance exponentielle.
- **Bloc `if __name__ == "__main__":`** :
    - Un vecteur temps `t` est créé de 0 à 20 avec 400 points.
    - La fonction `solution` est appelée pour calculer les valeurs `y` correspondantes.
    - `matplotlib.pyplot` est utilisé pour tracer le graphique de `N(t)` en fonction de `t`.
    - Les étiquettes des axes et le titre du graphique sont définis.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy` et `matplotlib` installés. Ensuite, exécutez le script Python :
```bash
python croissance_exponentielle.py
```
Ceci affichera un graphique de la croissance exponentielle.
