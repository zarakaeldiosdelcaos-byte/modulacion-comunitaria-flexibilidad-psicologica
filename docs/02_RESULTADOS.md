# Resultados

## 1. Criterio de presentación

Este documento distingue dos capas de evidencia:

* **Capa A — Resultados históricos documentados:** resultados presentes en las fuentes históricas y, para los tres coeficientes principales del resumen, localizados además en las salidas primarias de `lavaan::sem`.
* **Capa B — Reproducción / reanálisis:** resultados obtenidos posteriormente mediante scripts de reconstrucción o mediante análisis sobre bases distintas a la utilizada por el análisis principal.

Las cifras de la Capa A no se sustituyen por resultados del reanálisis independiente.

La muestra del análisis principal está constituida por **24 pacientes y 124 observaciones longitudinales**. Las observaciones repetidas no se consideran equivalentes a 124 participantes independientes.

Cuando una cifra fue denominada `β` en el resumen histórico pero la salida primaria conserva el parámetro como `Estimate`, se mantiene aquí el valor numérico documentado y se evita inferir una estandarización que no esté explícitamente registrada.

---

# CAPA A — RESULTADOS HISTÓRICOS DOCUMENTADOS

## 2. Modelo principal de mediación secuencial

El modelo histórico examinó la cadena:

$$
\text{Indefensión}
\rightarrow
\text{Evitación}
\rightarrow
\text{EROS}
\rightarrow
\text{ATQ-8}
$$

con tiempo, capital comunitario y balance comunitario como covariables.

### 2.1 Muestra analítica

La muestra utilizada para el análisis principal comprendió:

* **24 pacientes**
* **124 observaciones longitudinales**

La identificación del paciente se realizó mediante `ID`.

### 2.2 Coeficientes del modelo

La salida primaria `mediacion_dos_pasos_bootstrap.txt` documenta los siguientes coeficientes:

| Relación / parámetro                                 | Coeficiente |            IC 95 % |          p |
| ---------------------------------------------------- | ----------: | -----------------: | ---------: |
| Indefensión → BADS evitación (`a1`)                  |      10.013 |    [7.080, 12.947] |     < .001 |
| BADS evitación → EROS (`a2`)                         |       0.730 |     [0.666, 0.794] |     < .001 |
| EROS → ATQ-8 (`b1`)                                  |       0.374 |     [0.269, 0.480] |     < .001 |
| Efecto indirecto secuencial (`indirect1 = a1·a2·b1`) |   **2.735** | **[1.633, 3.837]** | **< .001** |
| Indirecto por evitación (`indirect2 = a1·b2`)        |      −0.201 |                  — |       .689 |
| Indirecto por EROS (`indirect3 = a3·b1`)             |      −0.131 |                  — |       .390 |
| Efecto total (`total`)                               |   **2.303** | **[1.366, 3.241]** | **< .001** |

### Precisión sobre la nomenclatura del resumen

El resumen histórico denomina `2.735` como **“efecto indirecto total”**. En la especificación estadística recuperada, `2.735` corresponde específicamente a:

```text
indirect1 = a1 × a2 × b1
```

El parámetro denominado `total` en el modelo es:

```text
total = c_prime + indirect1 + indirect2 + indirect3
```

y toma el valor:

$$
2.303\ [1.366,\ 3.241],\quad p<.001
$$

Por tanto, se trata de una diferencia de nomenclatura del resumen y no de una discrepancia entre los valores calculados.

---

## 3. Moderación por capital comunitario

La salida primaria `moderacion_capital_proxy_C.txt` documenta un término de interacción entre evitación y capital comunitario:

| Parámetro                                   | Coeficiente |            IC 95 % |        p |
| ------------------------------------------- | ----------: | -----------------: | -------: |
| BADS evitación → EROS                       |       0.735 |     [0.672, 0.798] |   < .001 |
| Capital comunitario (`cap_c`) → EROS        |       1.854 |    [−1.922, 5.629] |     .336 |
| **Evitación × capital (`evit_cap`) → EROS** |   **0.195** | **[0.024, 0.366]** | **.026** |
| EROS → ATQ-8                                |       0.379 |     [0.273, 0.485] |   < .001 |

Los efectos indirectos condicionales documentados fueron:

| Nivel de capital | Efecto indirecto |    SE |     z |      p |
| ---------------- | ---------------: | ----: | ----: | -----: |
| Bajo             |            1.711 | 0.958 | 1.785 |   .074 |
| Medio            |            2.804 | 0.561 | 5.000 | < .001 |
| Alto             |            4.150 | 1.733 | 2.395 |   .017 |

---

## 4. Efecto de la flexibilidad psicológica

La salida primaria `moderacion_flexibilidad_proxy_F.txt` documenta:

| Parámetro                                     | Coeficiente |              IC 95 % |        p |
| --------------------------------------------- | ----------: | -------------------: | -------: |
| BADS evitación → EROS                         |       0.731 |       [0.663, 0.799] |   < .001 |
| **Flexibilidad (`flex_c`) → EROS**            |  **−3.559** | **[−6.604, −0.515]** | **.022** |
| Evitación × flexibilidad (`evit_flex`) → EROS |       0.001 |      [−0.109, 0.111] |     .987 |
| EROS → ATQ-8                                  |       0.365 |       [0.261, 0.468] |   < .001 |

El efecto directo de la flexibilidad sobre EROS fue el coeficiente reportado históricamente en el resumen:

$$
\beta=-3.559,\quad p=.022
$$

---

## 5. Modelos complementarios de la misma línea analítica

Las salidas primarias contienen además los siguientes resultados:

| Análisis                                                                            | Resultado documentado                                                                       |                                                             |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Mediación estandarizada, `mediacion_2pasos.txt`                                     | `indirect1 = 0.351`; `total = 0.297`; CFI = 1.000; TLI = 1.000; RMSEA = 0.000; SRMR = 0.000 |                                                             |
| Moderación con `dico_capital_compuesto`                                             | `EROS_total ~ evit_cap = 0.045`, p = .154                                                   |                                                             |
| Moderación con `dico_balance`                                                       | `EROS_total ~ evit_bal = 0.452`, p = .039                                                   |                                                             |
| Modelo combinado capital + flexibilidad                                             | `flex_c = −3.468`, p = .017; `evit_cap = 0.197`, p = .020                                   |                                                             |
| Indefensión → EROS → ATQ-8                                                          | efecto indirecto = 2.476, IC 95 % [1.690, 3.262], p < .001                                  |                                                             |
| Indefensión → rumiación → ATQ-8                                                     | efecto indirecto = −0.011, p = .760                                                         |                                                             |
| LMM `ATQ8_total ~ semana_norm + EROS_total + indefension_idx_z + Rumiacion_sim + (1 | ID)`                                                                                        | EROS: β = 0.366, t = 21.0; indefensión: β = −0.060, p = .83 |
| Moderación LMM `ATQ8 × indef_z * EROS_z`                                            | interacción = −1.204, p < .0001                                                             |                                                             |
| Mediación causal con `mediation`                                                    | tamaño muestral utilizado = 24 pacientes; simulaciones = 500                                |                                                             |
| Rejilla de mediaciones                                                              | tamaño muestral correspondiente al análisis principal; `n_boot = 500`                       |                                                             |
| GAM capital comunitario                                                             | término suave p = .197                                                                      |                                                             |
| GAM flexibilidad                                                                    | término suave p = .533                                                                      |                                                             |
| Logit `rum_early * indef_early`                                                     | interacción = 21.97, p = .258                                                               |                                                             |

---

# CAPA A — LÍNEA INDEPENDIENTE DE RUMIACIÓN

## 6. Resultados históricos del estudio piloto de rumiación

Este bloque corresponde a una **línea independiente del análisis de mediación secuencial**.

### 6.1 Muestra

Se documentó un piloto controlado en comunidad terapéutica masculina:

* **N = 24**
* Tratamiento: `n = 14`
* Comparación: `n = 10`

En una versión ampliada se documentó:

* **N = 35**
* Tratamiento: `n = 20`
* Comparación: `n = 15`
* Edad media = 38.2 años
* DE = 10.4
* Rango = 18–55
* Abandono en seguimiento quincenal = 28.6 %
* Log-rank: `p = .0002`

### 6.2 Fiabilidad

| Instrumento / escala |        Coeficiente |
| -------------------- | -----------------: |
| RRS                  | α = .944; ω = .948 |
| PSWQ-II              | α = .935; ω = .937 |
| DASS-21 Total        |           ω = .941 |
| GHQ-12               |           ω = .902 |
| RRS-SF Reflexión     |           ω = .688 |
| VQ Obstrucción       |           ω = .634 |

### 6.3 Cambios pre-post intragrupo en tratamiento

| Variable          |                Efecto | Evidencia                                    |
| ----------------- | --------------------: | -------------------------------------------- |
| VQ Progreso       |           `g = +1.60` | Δ = +4.40; IC 95 % [2.31, 6.49]; BF₁₀ > 1000 |
| GHQ-12            |           `g = −0.81` | Δ = −3.60; BF₁₀ = 10.4                       |
| DASS-21 Depresión |           `g = −0.86` | BF₁₀ = 16.5                                  |
| CFQ               |           `g = −0.50` | BF₁₀ = 7.8                                   |
| AAQ-II            |           `g = −0.75` | —                                            |
| RRS total         |           `g = −0.49` | BF₁₀ = 0.6–1.2                               |
| PSWQ-II           |           `g = −0.43` | BF₁₀ = 0.6–1.2                               |
| ATQ-8             | `g = −0.31` a `−0.44` | BF₁₀ = 0.6–1.2                               |

### 6.4 Comparación intergrupo

| Variable    |     Estadístico |      p |  η²p |
| ----------- | --------------: | -----: | ---: |
| VQ Progreso | F(1,21) = 22.15 | < .001 | .513 |
| CFQ         |  F(1,21) = 6.74 |   .017 | .243 |

### 6.5 Moderaciones documentadas

| Modelo                    | Coeficiente | Evidencia                            |
| ------------------------- | ----------: | ------------------------------------ |
| VQ Progreso × Grupo → RRS |  **+1.283** | p = .002                             |
| RRS-SF Reflexión × Grupo  |  **−1.615** | p = .0001                            |
| ΔATQ-8 → VQ Progreso      |  **+1.757** | p < .0001; R² = .863                 |
| ΔATQ-8 → DASS-21 Total    |  **−2.018** | HDI 95 % [−2.314, −1.695]; R² = .922 |

### 6.6 Trayectorias quincenales

| Variable |                     Cambio semanal | p ajustada |
| -------- | ---------------------------------: | ---------: |
| GAD-7    |                −0.49 puntos/semana |     < .001 |
| ATQ-8    |                −1.02 puntos/semana |     < .001 |
| EROS     |                −0.83 puntos/semana |       .005 |
| BADS     | sin significación lineal tras Holm |          — |

La edad no mostró una moderación significativa de estas trayectorias.

---

# CAPA B — REPRODUCCIÓN / REANÁLISIS

## 7. Corrida 1 — Reproducción del estudio piloto

La reproducción utilizó una copia de `Rumia_preliminar.xlsx`.

### 7.1 Muestra reproducida

| Indicador                | Resultado |
| ------------------------ | --------: |
| ID únicos                |        24 |
| Tratamiento              |        14 |
| Comparación              |        10 |
| Casos completos pre-post |        24 |

La composición muestral coincidió con la documentada históricamente.

### 7.2 Comparación entre resultados documentados y reproducidos

| Modelo                           |           Documentado |                      Reproducido | Diferencia |
| -------------------------------- | --------------------: | -------------------------------: | ---------: |
| `DASS-21 Total ~ Grupo × ΔATQ-8` | β = −2.018; R² = .922 | β = −2.028; p < .0001; R² = .922 |      0.010 |
| `VQ Progreso ~ Grupo × ΔATQ-8`   | β = +1.757; R² = .863 | β = +1.757; p < .0001; R² = .863 |      0.000 |
| `RRS ~ Grupo × ΔVQ Progreso`     |  β = +1.283; p = .002 | β = +1.283; p = .0024; R² = .679 |      0.000 |

Se estimaron 40 modelos, con 26 términos de interacción con `p < .05`.

El resultado `−2.028` frente a `−2.018` corresponde a la diferencia entre el estimador bayesiano documentado históricamente y la estimación OLS empleada en la reproducción.

---

## 8. Corrida 2 — Reanálisis BADS–EROS–ATQ-8

Se utilizó `Registro Quincenal BADS EROS ATQ INV.xlsx`.

Esta corrida corresponde a una base complementaria y **no modifica la definición de la muestra principal**.

Características de la base reproducida:

* 127 observaciones persona-ola con BADS + EROS + ATQ
* 33 participantes
* cinco olas
* submuestra completa T1–T5: `N = 20`

### 8.1 Resultados

| Modelo                             |          b |         p |          β |         p |   R² |
| ---------------------------------- | ---------: | --------: | ---------: | --------: | ---: |
| `EROS_T1 ~ Evitación_T1`           |     +0.144 |      .209 |     +0.286 |      .209 | .082 |
| `EROS_T1 ~ Evitación_T1 × ATQ8_T1` |     +0.019 |      .247 |     +0.251 |      .247 | .197 |
| `ΔEROS ~ ΔEvitación`               | **+0.641** | **.0025** | **+0.637** | **.0025** | .405 |
| `ΔEROS ~ ΔEvitación × ATQ8_T1`     |     −0.055 |      .120 |     −0.372 |      .120 | .627 |

La base no contenía una variable de capital comunitario equivalente a la utilizada en el análisis principal, por lo que esa moderación no pudo reproducirse sobre esta fuente.

---

## 9. Corrida 3 — Control externo de la mediación secuencial

La tercera corrida utilizó:

```text
narraciones_rumia.csv
```

con:

* 251 observaciones
* 21 participantes
* 869 variables originales

Esta base **no corresponde a la muestra principal del proyecto**.

El análisis se utilizó como control externo del encadenamiento:

$$
\text{Indefensión}
\rightarrow
\text{Evitación}
\rightarrow
\text{EROS}
\rightarrow
\text{GAD-7}
$$

### 9.1 Resultados

| Parámetro                     | Estimador | IC 95 % percentil |
| ----------------------------- | --------: | ----------------: |
| Indefensión → evitación (`a`) |   +9.7936 | [7.0562, 13.7354] |
| Evitación → EROS (`b`)        |   +0.7574 |  [0.6961, 0.8133] |
| EROS → malestar (`c`)         |   +0.0300 | [−0.1767, 0.2486] |
| Efecto indirecto (`a·b·c`)    |   +0.2222 | [−1.2544, 2.0075] |
| Efecto directo                |   −0.1456 | [−0.6133, 0.3548] |

El intervalo del efecto indirecto incluye cero.

Este análisis no constituye una réplica del modelo principal debido a diferencias en:

* muestra;
* variable de desenlace;
* disponibilidad de los proxies comunitarios y de flexibilidad.

---

## 10. Verificación documental de las salidas primarias

La revisión de las salidas originales del MFCA permitió localizar los tres coeficientes centrales reportados en el resumen histórico:

| Resultado histórico           | Archivo primario                                                         | Estado         |
| ----------------------------- | ------------------------------------------------------------------------ | -------------- |
| `indirect1 = 2.735`, p < .001 | `mediacion_dos_pasos_bootstrap.txt` y `mediacion_dos_pasos_con_DICO.txt` | **Localizado** |
| `evit_cap = 0.195`, p = .026  | `moderacion_capital_proxy_C.txt`                                         | **Localizado** |
| `flex_c = −3.559`, p = .022   | `moderacion_flexibilidad_proxy_F.txt`                                    | **Localizado** |

También se verificó en el código histórico:

```text
set.seed(2025)
bootstrap = 500
```

y la especificación del modelo mediante `lavaan::sem`.

Esta verificación es documental: no implica una nueva ejecución del modelo original.

---

## 11. Reproducción del análisis principal

El análisis principal corresponde a una muestra de:

```text
24 pacientes
124 observaciones longitudinales
```

Los resultados históricos utilizados en este repositorio se conservan a partir de las salidas estadísticas documentadas del análisis.

Cuando una nueva ejecución independiente no es posible por ausencia de una copia íntegra y directamente ejecutable del entorno original, el resultado se clasifica como:

> **resultado históricamente documentado y verificado mediante salida primaria**

y no como una réplica computacional independiente.

---

## 12. Resumen de evidencia

| Resultado                                           | Evidencia                                           |
| --------------------------------------------------- | --------------------------------------------------- |
| Muestra principal: 24 pacientes / 124 observaciones | **Base analítica del proyecto**                     |
| `indirect1 = 2.735`, IC [1.633, 3.837], p < .001    | **Salida primaria N1**                              |
| `evit_cap = 0.195`, IC [0.024, 0.366], p = .026     | **Salida primaria N1**                              |
| `flex_c = −3.559`, IC [−6.604, −0.515], p = .022    | **Salida primaria N1**                              |
| `total = 2.303`, IC [1.366, 3.241], p < .001        | **Salida primaria N1**                              |
| Resultados del piloto de rumiación                  | **Documentación histórica N2 + reproducción**       |
| β +1.283, +1.757 y −1.615 del piloto                | **Reproducidos**                                    |
| β −2.018 del piloto                                 | **Reproducido con diferencia de 0.010**             |
| Relación `ΔEvitación → ΔEROS`                       | **Reanálisis independiente, b = +0.641, p = .0025** |
| Mediación sobre base externa de 21 participantes    | **Control externo; efecto indirecto IC incluye 0**  |

---

## 13. Distinción de muestras

Para evitar mezclar líneas analíticas:

```text
ANÁLISIS PRINCIPAL
24 pacientes
124 observaciones longitudinales

LÍNEA PILOTO DE RUMIACIÓN
N = 24
14 tratamiento
10 comparación

REANÁLISIS EXTERNO
21 participantes
251 observaciones
```

Las tres categorías se mantienen separadas.

El `N = 24` del estudio piloto no se utiliza para redefinir la muestra del análisis principal, y las bases externas tampoco se utilizan para redefinir la muestra principal.

---

## 14. Convención de reporte

Para mantener trazabilidad:

* los coeficientes, IC y valores de `p` de los análisis históricos se conservan con la precisión disponible en las salidas primarias;
* los resultados reproducidos posteriormente se identifican como tales;
* los análisis realizados sobre bases distintas no se presentan como réplicas del análisis principal;
* cuando una salida no contiene un IC o una medida de incertidumbre, no se calcula ni se agrega uno de manera retrospectiva;
* los resultados numéricos no se modifican para hacerlos coincidir con la formulación del resumen;
* la muestra principal se reporta consistentemente como **24 pacientes y 124 observaciones**.

La procedencia específica de cada resultado se documenta en:

```text
04_PROCEDENCIA.md
```

Las discrepancias y limitaciones metodológicas se documentan en:

```text
03_LIMITACIONES.md
```
