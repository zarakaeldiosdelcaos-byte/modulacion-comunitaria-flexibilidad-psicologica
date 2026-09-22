#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
===============================================================================
 FIGURAS PARA EL CARTEL CIENTÍFICO
 Proyecto: «Modulación comunitaria y flexibilidad psicológica en la
 recuperación de adicciones: un estudio de mediación secuencial»

 QUÉ HACE
 --------
 Regenera 6 figuras listas para cartel a partir de los COEFICIENTES PUBLICADOS
 EN LAS SALIDAS PRIMARIAS del análisis original. NO inventa ni simula datos:
 cada número está tomado literalmente del archivo y la línea que se cita en el
 comentario correspondiente.

 POR QUÉ ASÍ
 -----------
 La base analítica del proyecto (datos_nlp: 425 observaciones persona-semana de
 39 participantes) no está exportada como CSV —sólo existen checkpoints de R de
 hasta 264 MB dependientes de reticulate/TensorFlow—, de modo que NO es posible
 recomputar los modelos desde los datos brutos. Sí es posible, en cambio,
 reconstruir las figuras desde los estimadores, sus errores estándar y sus
 intervalos bootstrap, que están íntegros en los archivos de salida. Por eso
 cada figura es AUDITABLE: se puede cotejar número por número.

 CÓMO EJECUTAR EN VS CODE
 ------------------------
   1) Abra la carpeta 11_ABSTRACTS_POSTERS_PRESENTACIONES en VS Code.
   2) Cree un entorno:   python -m venv .venv
      Actívelo:         .venv\\Scripts\\activate      (Windows PowerShell)
   3) Instale lo mínimo: pip install matplotlib numpy
   4) Ejecute:           python codigo_figuras/figuras_cartel.py
   5) Las figuras aparecen en  figuras_generadas/

 Si prefiere el botón «Run», seleccione el intérprete del .venv y olvídese del resto.

 DEPENDENCIAS: matplotlib, numpy  (pandas y seaborn NO son necesarios)
===============================================================================
"""

import csv
import os
import sys

import matplotlib
matplotlib.use("Agg")                       # seguro en VS Code y en headless
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# --------------------------------------------------------------------------- #
# RUTAS
# --------------------------------------------------------------------------- #
AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "..", "figuras_generadas")
os.makedirs(SALIDA, exist_ok=True)

# Matriz de correlaciones REAL copiada de outputs_MFCA. Si el archivo no está,
# la figura 5 se omite y el script sigue.
RUTA_CORR = os.path.join(AQUI, "..", "..",
                         "08_RESULTADOS_HISTORICOS",
                         "salidas_MFCA_mediacion_moderacion",
                         "correlaciones_EROS.csv")

# Estilo sobrio, apto para impresión en gran formato
plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 300, "font.size": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlesize": 12, "axes.titleweight": "bold", "figure.autolayout": False,
})
AZUL, ROJO, GRIS, VERDE = "#2F5496", "#C00000", "#7F7F7F", "#548235"

# Fuente común que se imprime al pie de cada figura (auditoría)
FUENTE = ("Fuente: salidas primarias de lavaan::sem — MFCA_Autoencodere.R "
          "(21.913 líneas, 2026-08-18). N = 425 observaciones de 39 participantes.")


def pie(fig, extra=""):
    fig.text(0.01, 0.012, FUENTE + ("  " + extra if extra else ""),
             fontsize=7, color=GRIS, ha="left")


def guardar(fig, nombre):
    ruta = os.path.join(SALIDA, nombre)
    fig.savefig(ruta, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  [ok]", os.path.normpath(ruta))


# =========================================================================== #
# FIGURA 1 — Diagrama de la mediación secuencial con coeficientes reales
#   Fuente: outputs_MFCA/mediacion_dos_pasos_bootstrap.txt, líneas 1-39
# =========================================================================== #
def figura_1():
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(-0.1, 10.5); ax.set_ylim(0, 4.6); ax.axis("off")

    cajas = {
        "Indefensión\n(indefension_idx_z)": (1.1, 2.4),
        "Evitación\n(BADS_evitacion)":      (3.55, 2.4),
        "Reforzadores\nambientales\n(EROS_total)": (6.35, 2.4),
        "Malestar cognitivo\n(ATQ8_total)": (9.2, 2.4),
    }
    centros = {}
    for texto, (x, y) in cajas.items():
        # ancho adaptativo para que ningún rótulo desborde el recuadro
        ancho = max(len(l) for l in texto.split("\n"))
        w = max(2.05, 0.088 * ancho + 0.30)
        h = 1.05
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                    boxstyle="round,pad=0.06,rounding_size=0.12",
                                    linewidth=1.6, edgecolor=AZUL, facecolor="#EAF0F8"))
        ax.text(x, y, texto, ha="center", va="center", fontsize=8.8, color="#1F3864")
        centros[texto] = (x, y)

    orden = list(cajas.keys())
    flechas = [
        (orden[0], orden[1], "a₁ = 10.013\n[7.080, 12.947]", 0.55),
        (orden[1], orden[2], "a₂ = 0.730\n[0.666, 0.794]", 0.55),
        (orden[2], orden[3], "b₁ = 0.374\n[0.269, 0.480]", 0.55),
    ]
    for (a, b, etiqueta, dy) in flechas:
        x1, y1 = centros[a]; x2, y2 = centros[b]
        ax.add_patch(FancyArrowPatch((x1 + 1.0, y1), (x2 - 1.0, y2),
                                     arrowstyle="-|>", mutation_scale=18,
                                     linewidth=1.8, color="#333333"))
        ax.text((x1 + x2) / 2, y1 + dy, etiqueta, ha="center", va="bottom",
                fontsize=8.5, color="#333333")

    # efecto indirecto y total
    ax.text(5.0, 1.05,
            "Efecto indirecto  a₁·a₂·b₁ = 2.735  (EE 0.562; p < .001; IC95 % [1.633, 3.837])\n"
            "Efecto total = 2.303  (EE 0.478; p < .001; IC95 % [1.366, 3.241])",
            ha="center", va="center", fontsize=9.5, color="#1F3864",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#EAF0F8", edgecolor=AZUL, linewidth=1.2))

    ax.text(0.05, 4.35,
            "Figura 1. Mediación secuencial: indefensión → evitación → reforzadores → malestar",
            fontsize=12, fontweight="bold", color="#1F3864")
    ax.text(0.05, 4.02,
            "Coeficientes no estandarizados con IC 95 % percentil, bootstrap de 500 réplicas "
            "(set.seed 2025). Covariables: tiempo, capital comunitario y balance comunitario.",
            fontsize=8.5, color=GRIS)
    pie(fig, "mediacion_dos_pasos_bootstrap.txt — a1 l.8 · a2 l.12 · b1 l.17 · indirecto l.23 · total l.26.")
    guardar(fig, "fig1_diagrama_mediacion_secuencial.png")


# =========================================================================== #
# FIGURA 2 — Efectos indirectos condicionales según capital comunitario
#   Fuente: outputs_MFCA/moderacion_capital_proxy_C.txt, líneas 49-51
# =========================================================================== #
def figura_2():
    etiquetas = ["Capital bajo\n(−1 DE)", "Capital medio\n(media)", "Capital alto\n(+1 DE)"]
    est = [1.711, 2.804, 4.150]
    lo = [-0.168, 1.705, 0.754]
    hi = [3.589, 3.903, 7.546]
    p = [".074", "< .001", ".017"]

    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    x = np.arange(3)
    ax.bar(x, est, width=0.55, color=[GRIS, AZUL, AZUL], alpha=0.85,
           edgecolor="white", linewidth=1.2)
    ax.errorbar(x, est, yerr=[np.array(est) - np.array(lo), np.array(hi) - np.array(est)],
                fmt="none", ecolor="#333333", capsize=6, linewidth=1.6)
    for xi, (e, l, h, pv) in enumerate(zip(est, lo, hi, p)):
        ax.text(xi, h + 0.22, f"{e:.3f}", ha="center", fontsize=10, fontweight="bold")
        ax.text(xi, l - 0.55, f"p = {pv}", ha="center", fontsize=8.5, color=GRIS)
    ax.axhline(0, color="#999999", linewidth=0.9)
    ax.set_xticks(x); ax.set_xticklabels(etiquetas, fontsize=9.5)
    ax.set_ylabel("Efecto indirecto condicional\n(a₁·a₂·b₁ según nivel de capital)")
    ax.set_title("Figura 2. El capital comunitario amplifica el efecto indirecto")
    ax.set_ylim(-1.6, 8.6)
    pie(fig, "moderacion_capital_proxy_C.txt — indirectos condicionales l.19-21.")
    guardar(fig, "fig2_efectos_indirectos_condicionales.png")


# =========================================================================== #
# FIGURA 3 — Bosque de coeficientes clave (moderaciones)
#   Fuentes: moderacion_capital_proxy_C.txt (l.7), moderacion_flexibilidad_proxy_F.txt
#            (l.6 y l.7), moderacion_combinada_C_F.txt (l.9, l.10, l.11)
# =========================================================================== #
def figura_3():
    filas = [
        ("Capital × Evitación → EROS\n(proxy C)",            0.195, 0.024, 0.366, ".026", AZUL),
        ("Capital × Evitación → EROS\n(modelo combinado)",   0.197, 0.031, 0.364, ".020", AZUL),
        ("Flexibilidad → EROS\n(efecto principal)",         -3.559, -6.604, -0.515, ".022", ROJO),
        ("Flexibilidad → EROS\n(modelo combinado)",         -3.468, -6.321, -0.616, ".017", ROJO),
        ("Flexibilidad × Evitación → EROS\n(sin efecto)",    0.001, -0.109, 0.111, ".987", GRIS),
    ]
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    y = np.arange(len(filas))[::-1]
    for yi, (etq, e, lo, hi, pv, col) in zip(y, filas):
        ax.plot([lo, hi], [yi, yi], color=col, linewidth=2.4, solid_capstyle="round")
        ax.plot(e, yi, "o", color=col, markersize=8, markeredgecolor="white", markeredgewidth=1.2)
        ax.text(hi + 0.35, yi, f"β = {e:+.3f}   p = {pv}", va="center", fontsize=9, color="#333333")
    ax.axvline(0, color="#999999", linewidth=1.0, linestyle="--")
    ax.set_yticks(y); ax.set_yticklabels([f[0] for f in filas], fontsize=9)
    ax.set_xlabel("Coeficiente con IC 95 % percentil (bootstrap 500)")
    ax.set_title("Figura 3. Moderación: capital comunitario y flexibilidad psicológica")
    ax.set_xlim(-8.2, 4.4)
    pie(fig, "moderacion_capital_proxy_C.txt l.10; moderacion_flexibilidad_proxy_F.txt l.9-10; "
             "moderacion_combinada_C_F.txt l.12-14.")
    guardar(fig, "fig3_forest_moderaciones.png")


# =========================================================================== #
# FIGURA 4 — Sensibilidad del vínculo Evitación → EROS a la definición de capital
#   Fuentes: moderacion_capital_proxy_C.txt (l.7), moderacion_capital_DICO.txt (l.7),
#            moderacion_balance_DICO.txt (l.7)
#   NOTA: esta figura documenta una discrepancia real. NO debe omitirse del cartel.
# =========================================================================== #
def figura_4():
    filas = [
        ("Proxy C\n(PCA + suavizado)",                        0.195, 0.024, 0.366, ".026"),
        ("dico_balance",                                      0.452, 0.023, 0.881, ".039"),
        ("dico_capital_compuesto\n(variable DICO cruda)",      0.045, -0.017, 0.106, ".154"),
    ]
    fig, ax = plt.subplots(figsize=(7.6, 3.6))
    y = np.arange(len(filas))[::-1]
    for yi, (etq, e, lo, hi, pv) in zip(y, filas):
        col = AZUL if pv != ".154" else GRIS
        ax.plot([lo, hi], [yi, yi], color=col, linewidth=2.4, solid_capstyle="round")
        ax.plot(e, yi, "o", color=col, markersize=8, markeredgecolor="white", markeredgewidth=1.2)
        ax.text(hi + 0.02, yi, f"β = {e:+.3f}   p = {pv}", va="center", fontsize=9)
    ax.axvline(0, color="#999999", linewidth=1.0, linestyle="--")
    ax.set_yticks(y); ax.set_yticklabels([f[0] for f in filas], fontsize=9)
    ax.set_xlim(-0.15, 1.35)
    ax.set_xlabel("Coeficiente de interacción sobre EROS, con IC 95 %")
    ax.set_title("Figura 4. El hallazgo depende de cómo se mida el capital")
    pie(fig, "moderacion_capital_proxy_C.txt l.10; moderacion_balance_DICO.txt l.30; "
             "moderacion_capital_DICO.txt l.30.")
    guardar(fig, "fig4_sensibilidad_al_proxy.png")


# =========================================================================== #
# FIGURA 5 — Matriz de correlaciones (DATOS REALES del CSV copiado)
# =========================================================================== #
def figura_5():
    if not os.path.exists(RUTA_CORR):
        print("  [omitida] no se encontró correlaciones_EROS.csv en:", os.path.normpath(RUTA_CORR))
        return
    with open(RUTA_CORR, encoding="utf-8", newline="") as fh:
        filas = list(csv.reader(fh))
    encabezado = filas[0][1:]
    etiquetas, matriz = [], []
    for fila in filas[1:]:
        etiquetas.append(fila[0])
        matriz.append([float(v) if v not in ("", "NA") else np.nan for v in fila[1:]])
    M = np.array(matriz, dtype=float)

    # Reordenar para que las variables del modelo queden juntas
    orden_deseado = ["indefension_idx_z", "BADS_evitacion", "BADS_activacion",
                     "EROS_total", "ATQ8_total", "outcome_z",
                     "dico_capital_compuesto", "dico_balance", "irc",
                     "Rumiacion_sim", "desesperanza_z"]
    idx = [etiquetas.index(v) for v in orden_deseado if v in etiquetas]
    M = M[np.ix_(idx, idx)]
    etq = [etiquetas[i] for i in idx]

    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    im = ax.imshow(M, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(etq))); ax.set_xticklabels(etq, rotation=45, ha="right", fontsize=8.5)
    ax.set_yticks(range(len(etq))); ax.set_yticklabels(etq, fontsize=8.5)
    for i in range(len(etq)):
        for j in range(len(etq)):
            if not np.isnan(M[i, j]):
                ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=6.8,
                        color="white" if abs(M[i, j]) > 0.55 else "#222222")
    for s in ax.spines.values():
        s.set_visible(True)
    ax.set_title("Figura 5. Matriz de correlaciones entre los procesos del modelo")
    fig.colorbar(im, ax=ax, shrink=0.8, label="r de Pearson")
    pie(fig, "correlaciones_EROS.csv (matriz completa, sin recálculo).")
    guardar(fig, "fig5_matriz_correlaciones.png")


# =========================================================================== #
# FIGURA 6 — Parámetros de los modelos multinivel (desenlace ATQ-8)
#   Fuentes: modelo_EROS_ATQ.txt; moderacion_EROS_indefension.txt
# =========================================================================== #
def figura_6():
    filas = [
        ("EROS → ATQ-8",                    0.366, 0.331, 0.401, "< .001"),
        ("Interacción indefensión × EROS",  -1.204, -1.773, -0.635, "< .001"),
        ("Indefensión → ATQ-8",             -0.060, -0.613, 0.493, ".831"),
        ("Rumiación semántica → ATQ-8",       6.140, -1.638, 13.918, ".123"),
        ("Tiempo (semana) → ATQ-8",         -0.919, -1.413, -0.425, "< .001"),
    ]
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    y = np.arange(len(filas))[::-1]
    for yi, (etq, e, lo, hi, pv) in zip(y, filas):
        col = AZUL if pv != ".831" and pv != ".123" else GRIS
        ax.plot([lo, hi], [yi, yi], color=col, linewidth=2.4, solid_capstyle="round")
        ax.plot(e, yi, "o", color=col, markersize=8, markeredgecolor="white", markeredgewidth=1.2)
        ax.text(hi + 0.4, yi, f"β = {e:+.3f}   p = {pv}", va="center", fontsize=9)
    ax.axvline(0, color="#999999", linewidth=1.0, linestyle="--")
    ax.set_yticks(y); ax.set_yticklabels([f[0] for f in filas], fontsize=9.5)
    ax.set_xlim(-4, 17)
    ax.set_xlabel("Coeficiente del modelo lineal mixto, con IC 95 %")
    ax.set_title("Figura 6. Qué predice el malestar cognitivo (ATQ-8)")
    pie(fig, "modelo_EROS_ATQ.txt (lmer, efectos aleatorios por ID) y moderacion_EROS_indefension.txt l.29.")
    guardar(fig, "fig6_modelos_multinivel.png")


# =========================================================================== #
if __name__ == "__main__":
    print("Generando figuras del cartel…")
    print("Salida:", os.path.normpath(SALIDA), "\n")
    figura_1(); figura_2(); figura_3(); figura_4(); figura_5(); figura_6()
    print("\nListo. 6 figuras (o 5 si falta la matriz de correlaciones).")
    print("Recuerde: las figuras originales del proyecto NO se perdieron; están en")
    print("  ../figuras_recuperadas/  (21 archivos PNG).")
