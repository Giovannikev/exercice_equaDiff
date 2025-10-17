import subprocess, sys, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXO_DIR = ROOT / "src" / "exercises"

EXOS = [
    ("Exo1_Croissance_Exponentielle", "croissance_exponentielle.py"),
    ("Exo2_Refroidissement_Newton", "refroidissement_newton.py"),
    ("Exo3_Euler", "euler_method.py"),
    ("Exo4_Systeme_Lineaire", "systeme_lineaire.py"),
    ("Exo5_SIR_Model", "sir_model.py"),
    ("Exo6_SystemeDynamique_Classe", "systeme_dynamique.py"),
]

def main():
    print("== Lancement des exercices ==")
    for folder, file in EXOS:
        path = EXO_DIR / folder / file
        print(f"-> Exécution: {path}")
        subprocess.run([sys.executable, str(path)], check=False)

if __name__ == "__main__":
    main()
