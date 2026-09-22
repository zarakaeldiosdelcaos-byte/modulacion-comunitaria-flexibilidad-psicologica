# Procedencia de los datos y resultados

> **Investigación en proceso.** Este documento registra de qué archivo proviene cada variable, cifra y
> resultado del análisis, de modo que cualquier persona pueda seguir el rastro de lo que se publica.

## 1. Propósito

Este documento responde a:

> **¿De qué archivo salió exactamente cada variable, cifra y resultado del análisis?**

La procedencia corresponde a la base analítica utilizada en este proyecto:

* **425 observaciones persona-semana**
* **39 participantes**
* identificador de participante: `ID`

La línea del estudio piloto de rumiación y las bases complementarias se documentan por separado en
`02_RESULTADOS.md` y no se utilizan para definir el tamaño muestral del proyecto.

---

## 2. Fuente de la base analítica

### 2.1 Base del análisis

| Elemento                   | Procedencia                     | Archivo / fuente                  | Variable / evidencia | Estado         |
| -------------------------- | ------------------------------- | --------------------------------- | -------------------- | -------------- |
| Número de observaciones    | Base del análisis               | registros persona-semana          | `425`                | **Documentado** |
| Número de participantes    | Base del análisis               | identificadores únicos            | `39` `ID`            | **Documentado** |
| Identificador del participante | Base del análisis            | `ID`                              | `ID`                 | **Documentado** |
| Unidad de análisis         | Estructura longitudinal         | registros por participante y medición | persona-semana   | **Documentado** |

**Base del análisis:**

```text
425 observaciones persona-semana
39 participantes
```

**Nivel de evidencia:** N1 (salidas estadísticas del análisis)
**Confianza:** Alta

El número de observaciones proviene de las salidas que lo reportan de forma explícita: los modelos mixtos
(`Number of obs: 425, groups: ID, 39`), los modelos aditivos generalizados (`n = 400` a `n = 425` según
especificación) y el análisis de mediación con el paquete `mediation` (`Sample Size Used: 425`). El modelo de
ecuaciones estructurales no imprime el número de observaciones retenidas.

---

## 3. Sobre otras cifras presentes en los materiales

En los materiales del proyecto aparecen otras dos cifras de tamaño muestral que **no describen la base
analítica de este estudio** y por tanto no se utilizan aquí:

| Cifra | De dónde viene | Uso en este repositorio |
|---|---|---|
| `N = 24` (14 tratamiento / 10 comparación) | Estudio piloto de rumiación, línea independiente | Se documenta en `02_RESULTADOS.md` §6 como otra línea del programa de trabajo |
| `127 observaciones / 33 participantes` | Base complementaria del registro quincenal | Se documenta en `02_RESULTADOS.md` §8 como base de un reanálisis complementario |

Las tres categorías —base del análisis, piloto de rumiación y bases complementarias— se mantienen separadas
en toda la documentación.

---

## 4. Variables principales

### 4.1 BADS — evitación

| Elemento                 | Procedencia              |
| ------------------------ | ------------------------ |
| Variable                 | `BADS_evitacion`         |
| Fuente                   | base del análisis        |
| Tipo                     | variable derivada        |
| Construcción documentada | `P8:P10 + P13:P15 + P24:P25` |
| Estado                   | **Documentado**          |

---

### 4.2 EROS

| Elemento     | Procedencia       |
| ------------ | ----------------- |
| Variable     | `EROS_total`      |
| Fuente       | base del análisis |
| Construcción | `SUM(P1:P10)`     |
| Tipo         | variable observada |
| Estado       | **Documentado**   |

---

### 4.3 ATQ-8

| Elemento     | Procedencia       |
| ------------ | ----------------- |
| Variable     | `ATQ8_total`      |
| Fuente       | base del análisis |
| Construcción | `SUM(P1:P8)`      |
| Tipo         | variable observada |
| Estado       | **Documentado**   |

---

## 5. Indefensión

La variable principal del modelo es:

```text
indefension_idx_z
```

También se localizaron:

```text
indefension_idx
impotencia_indefension
Indefension_sim
dico_Desesperanza
```

La variable está presente en la estructura analítica del proyecto. La fórmula completa de construcción de `indefension_idx_z` no quedó localizada de forma reproducible en los materiales disponibles.

Por tanto:

```text
Variable: localizada
Fórmula exacta: no localizada
```

**Nivel:** N1 + N3
**Confianza:** Media-alta

---

## 6. Capital comunitario

El índice de capital comunitario se construyó mediante el bloque correspondiente de `MFCA_Autoencodere.R`.

### Componentes

Se utilizaron 13 indicadores normalizados:

```text
apoyo_social_norm
ct_norm
valencia_norm
esperanza_norm
progreso_norm
eros_norm
evitacion_inv_norm
gad7_inv_norm
ect_norm
iaa_norm
sueño_norm
adherencia_norm
estres_inv_norm
```

### Procedimiento

```text
13 variables
    ↓
imputación por mediana
    ↓
PCA
    ↓
selección/combinación de componentes
    ↓
robust_plogis
    ↓
suavizado exponencial por ID
    ↓
C_smooth
```

Parámetro de suavizado:

```text
α = 0.3
```

**Estado:** Documentado
**Nivel:** N1
**Confianza:** Alta

La varianza explicada utilizada en la ejecución del PCA no quedó almacenada como salida persistente.

---

## 7. Flexibilidad psicológica

La flexibilidad psicológica se representa mediante:

```text
F_flex
F_flex_smooth
```

La fórmula recuperada del código es:

$$
F_{flex}
=
0.45F_{proceso}
+
0.35F_{activacion}
-
0.20F_{evitar}
$$

Posteriormente:

```text
F_flex
    ↓
robust_plogis
    ↓
suavizado exponencial por ID
    ↓
F_flex_smooth
```

con:

```text
α = 0.3
```

Este índice **no utiliza PCA** en la implementación recuperada.

**Estado:** Documentado
**Nivel:** N1
**Confianza:** Alta

---

## 8. Variables temporales y comunitarias

| Variable                 | Procedencia                             | Uso                 |
| ------------------------ | --------------------------------------- | ------------------- |
| `semana_norm`            | transformación en `MFCA_Autoencodere.R` | covariable temporal |
| `dico_capital_compuesto` | variables DICO / código del proyecto    | covariable          |
| `dico_balance`           | variables DICO / código del proyecto    | covariable          |

La definición exacta de cada versión se conserva asociada al script y a la salida donde fue utilizada.

---

## 9. Modelo estadístico

La especificación del modelo principal se localiza en:

```text
MFCA_Autoencodere.R
```

Objeto:

```text
modelo_mediacion
```

Cadena:

```text
indefensión
    ↓
BADS_evitacion
    ↓
EROS_total
    ↓
ATQ8_total
```

Con:

```text
semana_norm
dico_capital_compuesto
dico_balance
```

como covariables.

**Estado:** Documentado
**Nivel:** N1
**Confianza:** Alta

---

## 10. Resultados y procedencia

Cada cifra que se publica en `02_RESULTADOS.md` se acompaña del archivo de salida del que proviene. La
correspondencia es la siguiente:

| Resultado | Salida primaria |
|---|---|
| `indirect1 = 2.735`, IC [1.633, 3.837] | `mediacion_dos_pasos_bootstrap.txt` |
| `evit_cap = 0.195`, IC [0.024, 0.366] | `moderacion_capital_proxy_C.txt` |
| `flex_c = −3.559`, IC [−6.604, −0.515] | `moderacion_flexibilidad_proxy_F.txt` |
| `total = 2.303`, IC [1.366, 3.241] | `mediacion_dos_pasos_bootstrap.txt` |
| `indirect1 = 0.351`, `total = 0.297` (estandarizado) | `mediacion_2pasos.txt` |
| `indirect = 2.476`, IC [1.690, 3.262] | `mediacion_EROS_indefension.txt` |
| `n = 425` · `groups: ID, 39` | modelo mixto del desenlace ATQ-8 |

Los archivos de salida se conservan y están disponibles para su cotejo.

---

## 11. Regla de trazabilidad

Cada cifra publicada en `02_RESULTADOS.md` puede rastrearse mediante:

```text
resultado
    ↓
archivo de salida
    ↓
script del análisis
    ↓
base del análisis
    ↓
425 observaciones persona-semana / 39 participantes
```

Cuando un resultado proviene de una base distinta —el piloto de rumiación o una base complementaria— se
identifica explícitamente como tal en `02_RESULTADOS.md`.

---

## 12. Estado actual de procedencia

### Documentado

```text
Base del análisis:
425 observaciones persona-semana
39 participantes

BADS_evitacion
EROS_total
ATQ8_total

Capital comunitario:
PCA + robust_plogis + suavizado α = .3

Flexibilidad:
0.45 / 0.35 / −0.20
+ robust_plogis
+ suavizado α = .3

Modelo:
mediación secuencial
```

### Registrado, fuera de la base del análisis

```text
Estudio piloto de rumiación:
N = 24 (14 tratamiento / 10 comparación)

Base complementaria del registro quincenal:
127 observaciones / 33 participantes

Reanálisis externo:
251 observaciones / 21 participantes
```

---

## 13. Regla final

La base analítica del repositorio es:

> **425 observaciones persona-semana correspondientes a 39 participantes.**

Toda cifra incluida en `02_RESULTADOS.md` está vinculada a esa base o se identifica explícitamente como
procedente de otra línea o base complementaria.
