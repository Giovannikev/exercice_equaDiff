# Exercice 2 – Refroidissement de Newton

## Description
Cet exercice illustre la loi de refroidissement de Newton, qui décrit comment la température d'un objet change au fil du temps en fonction de la différence de température entre l'objet et son environnement. Il utilise `numpy` pour les calculs et `matplotlib` pour la visualisation.

## Modèle Mathématique
La loi de refroidissement de Newton est donnée par l'équation différentielle suivante :
$$ \frac{dT}{dt} = -k(T - T_{ext}) $$
où :
- $T(t)$ est la température de l'objet au temps $t$.
- $T_{ext}$ est la température ambiante (température extérieure).
- $k$ est une constante de proportionnalité positive, liée aux propriétés thermiques de l'objet et de son environnement.

La solution analytique de cette équation différentielle, avec une condition initiale $T(0) = T_0$, est :
$$ T(t) = T_{ext} + (T_0 - T_{ext})e^{-kt} $$

## Implémentation Python

Le fichier `refroidissement_newton.py` contient la fonction `temperature` qui calcule la température de l'objet et un bloc principal pour la visualisation.

```python
import numpy as np
import matplotlib.pyplot as plt

def temperature(t, T0=80, Text=20, k=0.1):
    """
    Calculates the temperature of an object at time t according to Newton's Law of Cooling.

    Args:
        t (float or np.array): Time.
        T0 (float): Initial temperature of the object (default: 80°C).
        Text (float): Ambient temperature (default: 20°C).
        k (float): Cooling constant (default: 0.1).

    Returns:
        float or np.array: Temperature of the object at time t.
    """
    return Text + (T0 - Text) * np.exp(-k * t)

if __name__ == "__main__":
    # Generate time points (e.g., 0 to 60 minutes)
    t = np.linspace(0, 60, 601)
    # Calculate corresponding temperatures
    T = temperature(t)

    # Plot the results
    plt.plot(t, T)
    plt.xlabel("t (min)")
    plt.ylabel("T(t) (°C)")
    plt.title("Refroidissement de Newton")
    plt.grid(True)
    plt.show()
```

### Explication du Code

- **`temperature(t, T0=80, Text=20, k=0.1)`** : Cette fonction prend en entrée le temps `t`, la température initiale `T0` (par défaut 80°C), la température ambiante `Text` (par défaut 20°C) et la constante de refroidissement `k` (par défaut 0.1). Elle retourne la température de l'objet au temps `t` en utilisant la solution analytique de la loi de refroidissement de Newton.
- **Bloc `if __name__ == "__main__":`** :
    - Un vecteur temps `t` est créé de 0 à 60 minutes avec 601 points.
    - La fonction `temperature` est appelée pour calculer les valeurs `T` correspondantes.
    - `matplotlib.pyplot` est utilisé pour tracer le graphique de `T(t)` en fonction de `t`.
    - Les étiquettes des axes et le titre du graphique sont définis.
    - `plt.grid(True)` a été ajouté pour améliorer la lisibilité du graphique.
    - `plt.show()` affiche le graphique.

## Comment Exécuter
Pour exécuter ce code, assurez-vous d'avoir `numpy` et `matplotlib` installés. Ensuite, exécutez le script Python :
```bash
python refroidissement_newton.py
```
Ceci affichera un graphique de la température de l'objet au fil du temps.
