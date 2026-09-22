# Procedencia de los datos y resultados

## 1. Propósito

Este documento responde a:

> **¿De qué archivo salió exactamente cada variable, cifra y resultado del análisis?**

La procedencia se restringe a la muestra analítica utilizada en este proyecto:

* **124 observaciones**
* **24 pacientes/residentes**
* identificador de participante: `ID`

El estudio piloto histórico de rumiación y cualquier otra extracción que no corresponda a esta muestra se mantienen separados y no se utilizan para definir el tamaño muestral del proyecto.

---

## 2. Fuente de la muestra analítica

### 2.1 Muestra principal

| Elemento                   | Procedencia              | Archivo / fuente                  | Variable / evidencia | Estado                      |
| -------------------------- | ------------------------ | --------------------------------- | -------------------- | --------------------------- |
| Número de observaciones    | Base analítica utilizada | archivo de datos del proyecto     | `124` registros      | **RECUPERADA DIRECTAMENTE** |
| Número de pacientes        | Base analítica utilizada | archivo de datos del proyecto     | `24` `ID` únicos     | **RECUPERADA DIRECTAMENTE** |
| Identificador del paciente | Base analítica           | `ID`                              | `ID`                 | **RECUPERADA DIRECTAMENTE** |
| Unidad de análisis         | Estructura longitudinal  | registros por paciente y medición | paciente-observación | **RECUPERADA DIRECTAMENTE** |

**Muestra oficial del proyecto:**

```text
124 observaciones
24 pacientes/residentes
```

**Nivel de evidencia:** N1
**Confianza:** Alta

---

## 3. Corrección de una discrepancia documental previa

En materiales previamente auditados aparece una salida estadística que informa:

```text
Number of obs: 425
groups: ID, 39
```

Esa cifra **no debe utilizarse para describir la muestra oficial de este proyecto**, dado que la muestra analítica adoptada para este repositorio es de:

```text
124 observaciones
24 pacientes
```

Por tanto, cualquier archivo, output o resultado que corresponda a la extracción de `425 / 39` debe clasificarse como:

```text
versión / extracción distinta
```

hasta establecer documentalmente su relación con la base de 124 observaciones y 24 pacientes.

No se sustituye una cifra por otra dentro de un mismo análisis: se conserva la distinción entre versiones para mantener la trazabilidad.

---

## 4. Variables principales

### 4.1 BADS — evitación

| Elemento                 | Procedencia                  |
| ------------------------ | ---------------------------- |
| Variable                 | `BADS_evitacion`             |
| Fuente                   | base analítica del proyecto  |
| Tipo                     | variable derivada observada  |
| Construcción documentada | `P8:P10 + P13:P15 + P24:P25` |
| Estado                   | **RECUPERADA DIRECTAMENTE**  |

---

### 4.2 EROS

| Elemento     | Procedencia                 |
| ------------ | --------------------------- |
| Variable     | `EROS_total`                |
| Fuente       | base analítica del proyecto |
| Construcción | `SUM(P1:P10)`               |
| Tipo         | variable observada          |
| Estado       | **RECUPERADA DIRECTAMENTE** |

---

### 4.3 ATQ-8

| Elemento     | Procedencia                 |
| ------------ | --------------------------- |
| Variable     | `ATQ8_total`                |
| Fuente       | base analítica del proyecto |
| Construcción | `SUM(P1:P8)`                |
| Tipo         | variable observada          |
| Estado       | **RECUPERADA DIRECTAMENTE** |

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

La variable está presente en la estructura analítica del proyecto, pero la fórmula completa de construcción de `indefension_idx_z` no quedó localizada de forma reproducible en la auditoría.

Por tanto:

```text
Variable: recuperada
Fórmula exacta: no localizada
```

**Nivel:** N1 + N3
**Confianza:** Media-alta

---

## 6. Capital comunitario

El proxy de capital comunitario se construyó mediante el bloque correspondiente de `MFCA_Autoencodere.R`.

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

**Estado:** RECUPERADA DIRECTAMENTE
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

Este proxy **no utiliza PCA** en la implementación recuperada.

**Estado:** RECUPERADA DIRECTAMENTE
**Nivel:** N1
**Confianza:** Alta

---

## 8. Variables temporales y comunitarias

| Variable                 | Procedencia                             | Uso                 |
| ------------------------ | --------------------------------------- | ------------------- |
| `semana_norm`            | transformación en `MFCA_Autoencodere.R` | covariable temporal |
| `dico_capital_compuesto` | variables DICO / código del proyecto    | covariable          |
| `dico_balance`           | variables DICO / código del proyecto    | covariable          |

La definición exacta de cada versión debe conservarse asociada al script y al output donde fue utilizada.

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

**Estado:** RECUPERADA DIRECTAMENTE
**Nivel:** N1
**Confianza:** Alta

---

## 10. Resultados y procedencia

Los resultados numéricos solo se atribuirán a la muestra oficial de **124 observaciones / 24 pacientes** cuando el archivo de salida pueda vincularse inequívocamente con esa misma base.

Por tanto, se utilizará la siguiente regla:

```text
BASE = 124 observaciones / 24 pacientes
        +
OUTPUT correspondiente
        =
resultado atribuible al proyecto
```

Cuando un output indique otra muestra, esa cifra se conservará como evidencia histórica o como versión distinta, pero **no se utilizará para afirmar que el resultado proviene de los 24 pacientes**.

---

## 11. Regla de trazabilidad

Cada cifra publicada en `02_RESULTADOS.md` debe poder rastrearse mediante:

```text
resultado
    ↓
archivo de output
    ↓
script
    ↓
base analítica
    ↓
124 observaciones / 24 pacientes
```

Si uno de estos vínculos no puede establecerse, el resultado debe marcarse como:

```text
PROCEDENCIA NO CONFIRMADA
```

y no como resultado confirmado de la muestra principal.

---

## 12. Estado actual de procedencia

### Confirmado

```text
Muestra oficial:
124 observaciones
24 pacientes

BADS_evitacion
EROS_total
ATQ8_total

Capital comunitario:
PCA + robust_plogis + suavizado α=.3

Flexibilidad:
0.45 / 0.35 / −0.20
+ robust_plogis
+ suavizado α=.3

Modelo:
mediación secuencial
```

### Pendiente de conciliación

```text
Outputs que reportan:
425 observaciones
39 pacientes
```

Estos outputs no deben mezclarse con la muestra oficial de 24 pacientes hasta establecer su procedencia exacta.

---

## 13. Regla final

La muestra oficial del repositorio es:

> **24 pacientes y 124 observaciones.**

Toda cifra incluida en `02_RESULTADOS.md` deberá estar vinculada a esa muestra o identificarse explícitamente como procedente de otra versión, estudio o extracción.

No se utilizará el valor `425 / 39` como muestra del proyecto.
