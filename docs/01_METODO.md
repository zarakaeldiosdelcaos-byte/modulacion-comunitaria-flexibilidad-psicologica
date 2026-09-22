# Método

## 1. Diseño

Estudio con **medidas repetidas** realizado en una comunidad terapéutica residencial, con observaciones longitudinales por paciente.

La unidad de identificación del participante fue `ID`. La estructura repetida de las observaciones se consideró en los análisis que incorporaron agrupamiento por participante.

El análisis examinó la relación entre **indefensión, evitación, reforzamiento ambiental y malestar cognitivo**, incorporando indicadores de contexto comunitario y flexibilidad psicológica.

---

## 2. Muestra y unidad de análisis

La muestra analítica comprendió:

* **24 pacientes**
* **124 observaciones**

El identificador de participante fue `ID`.

Las 124 observaciones corresponden a mediciones repetidas de los 24 pacientes y, por tanto, no representan 124 participantes independientes.

---

## 3. Variables e instrumentos

### 3.1 Indefensión

La variable predictora principal del modelo de mediación fue:

```text
indefension_idx_z
```

La variable se incorporó en la especificación del modelo en escala estandarizada.

El procedimiento exacto mediante el cual fue construido originalmente `indefension_idx_z` no quedó completamente localizado en los materiales disponibles. Por ello, no se reproduce aquí una fórmula que no esté documentada directamente en la fuente primaria.

---

### 3.2 Evitación y activación: BADS

La conducta de evitación se representó mediante:

```text
BADS_evitacion
```

derivada del **Behavioral Activation for Depression Scale (BADS)**.

En el modelo secuencial, esta variable constituyó el primer mediador:

$$
\text{Indefensión} \rightarrow \text{Evitación}
$$

---

### 3.3 Reforzamiento ambiental: EROS

El reforzamiento ambiental se representó mediante:

```text
EROS_total
```

derivado de la **Environmental Reward Observation Scale (EROS)**.

En el modelo secuencial, esta variable constituyó el segundo mediador:

$$
\text{Evitación} \rightarrow \text{Reforzamiento ambiental}
$$

---

### 3.4 Malestar cognitivo: ATQ-8

El desenlace principal del modelo de mediación fue:

```text
ATQ8_total
```

derivado del **Automatic Thoughts Questionnaire, versión de 8 ítems (ATQ-8)**.

En la especificación principal, `ATQ8_total` representó el componente de malestar cognitivo/pensamientos automáticos negativos utilizado en el análisis.

---

### 3.5 Variables comunitarias y longitudinales

Se incorporaron como covariables:

```text
semana_norm
dico_capital_compuesto
dico_balance
```

`semana_norm` representó la dimensión temporal incluida en el modelo.

`dico_capital_compuesto` y `dico_balance` correspondieron a los indicadores comunitarios utilizados en las especificaciones recuperadas del análisis.

---

### 3.6 Índice de capital comunitario

El capital comunitario se representó mediante un índice compuesto construido a partir de un **análisis de componentes principales (PCA)** sobre 13 indicadores normalizados.

El procedimiento recuperado incluyó:

1. preparación de los indicadores normalizados;
2. análisis de componentes principales;
3. combinación de componentes de acuerdo con la varianza explicada;
4. transformación mediante `robust_plogis`;
5. suavizado exponencial recursivo por paciente.

El suavizado utilizó:

```text
α = 0.3
```

La varianza explicada específica utilizada en la ejecución del PCA no quedó conservada como salida persistente.

---

### 3.7 Índice de flexibilidad psicológica

La flexibilidad psicológica se representó mediante un índice compuesto basado en tres componentes:

* proceso;
* activación;
* evitación.

La implementación recuperada utilizó pesos fijos:

$$
F_{flex}
=
0.45F_{proceso}
+
0.35F_{activacion}
-
0.20F_{evitar}
$$

Posteriormente se aplicó `robust_plogis` y suavizado exponencial recursivo por paciente, con:

```text
α = 0.3
```

La implementación recuperada de este índice **no utiliza PCA**.

---

### 3.8 Rumiación

La rumiación se utilizó en análisis complementarios y modelos adicionales.

No forma parte de la cadena principal del modelo de mediación secuencial:

$$
\text{Indefensión}
\rightarrow
\text{Evitación}
\rightarrow
\text{EROS}
\rightarrow
\text{ATQ-8}
$$

---

## 4. Análisis estadístico

### 4.1 Modelo de mediación secuencial

Se especificó un modelo de **ecuaciones estructurales** para evaluar la cadena:

$$
\text{Indefensión}
\rightarrow
\text{Evitación}
\rightarrow
\text{Reforzamiento ambiental}
\rightarrow
\text{Malestar cognitivo}
$$

La especificación recuperada fue:

```r
modelo_mediacion <- '
  BADS_evitacion ~ a1 * indefension_idx_z + semana_norm +
                   dico_capital_compuesto + dico_balance

  EROS_total ~ a2 * BADS_evitacion +
               a3 * indefension_idx_z +
               semana_norm +
               dico_capital_compuesto +
               dico_balance

  ATQ8_total ~ b1 * EROS_total +
               b2 * BADS_evitacion +
               c_prime * indefension_idx_z +
               semana_norm +
               dico_capital_compuesto +
               dico_balance

  indirect1 := a1 * a2 * b1
  indirect2 := a1 * b2
  indirect3 := a3 * b1

  total := c_prime + indirect1 + indirect2 + indirect3
'
```

Los efectos indirectos se definieron como:

$$
indirect1=a_1a_2b_1
$$

$$
indirect2=a_1b_2
$$

$$
indirect3=a_3b_1
$$

y el efecto total como:

$$
total=c'+indirect1+indirect2+indirect3
$$

Los coeficientes, intervalos de confianza y valores de `p` se presentan en `02_RESULTADOS.md`.

---

### 4.2 Estimación del modelo principal

La especificación estadística documentada utilizó:

* **R**
* **`lavaan`**
* estimador **MLR**
* agrupamiento por participante mediante `ID`
* casos completos por modelo en la especificación recuperada
* **500 réplicas bootstrap**
* `set.seed(2025)` en la ejecución original

---

### 4.3 Moderación por capital comunitario

Se estimaron modelos que incorporaron el capital comunitario como moderador.

Se evaluaron términos de interacción entre el componente de evitación y el indicador de capital comunitario dentro de la estructura del modelo.

Los coeficientes, intervalos de confianza y valores de `p` se presentan en `02_RESULTADOS.md`.

---

### 4.4 Moderación por flexibilidad psicológica

Se estimaron modelos que incorporaron la flexibilidad psicológica como variable moderadora.

Los modelos incluyeron los efectos correspondientes de flexibilidad y los términos de interacción especificados en el análisis recuperado.

Los resultados numéricos se presentan en `02_RESULTADOS.md`.

---

### 4.5 Modelo combinado

Se estimó un modelo combinado que incorporó simultáneamente:

* capital comunitario;
* flexibilidad psicológica;
* términos de interacción correspondientes.

Los coeficientes y valores de significancia se presentan en `02_RESULTADOS.md`.

---

### 4.6 Modelos mixtos

También se utilizaron **modelos mixtos** para análisis longitudinales del desenlace.

La implementación documentada utilizó:

```text
R / lme4
```

La estructura repetida por participante se representó mediante `ID`.

Las fórmulas específicas de cada modelo mixto se conservan en las salidas y scripts correspondientes.

---

### 4.7 Modelos aditivos generalizados

Se evaluaron relaciones no lineales mediante **modelos aditivos generalizados (GAM)**.

La implementación documentada utilizó:

```text
R / mgcv
```

Se evaluaron términos suaves asociados con los indicadores comunitarios y de flexibilidad.

Los resultados de estos términos se presentan en `02_RESULTADOS.md`.

---

## 5. Datos faltantes y transformaciones

En los procedimientos de reconstrucción no se realizó imputación de datos.

Las estimaciones de los modelos de reconstrucción utilizaron casos completos para cada especificación.

Las variables utilizadas en forma estandarizada fueron identificadas explícitamente, como:

```text
indefension_idx_z
```

No se asumieron transformaciones adicionales que no estuvieran documentadas en las fuentes analizadas.

---

## 6. Reproducción estadística

La reproducción estadística se desarrolló como un procedimiento independiente de **reconstrucción y verificación**.

Ningún archivo original fue modificado. Los scripts de reproducción operan sobre copias de las bases depositadas en:

```text
../03_BASES_DE_DATOS/
```

La estructura de reproducción es:

```text
07_REPRODUCCION_ESTADISTICA/

├── codigo/
│   ├── REPRODUCCION_moderacion_rumia.R
│   ├── REPRODUCCION_modelo_EROS_BADS_ATQ.R
│   └── REPRODUCCION_v3_mediacion_secuencial.R
│
├── salidas/
│   ├── log_reproduccion.txt
│   ├── log_reproduccion_v2.txt
│   ├── log_reproduccion_v3.txt
│   ├── dataset_deltas_reproducido.csv
│   ├── moderacion_reproducida.csv
│   ├── registro_quincenal_largo_reproducido.csv
│   ├── submuestra_T1_T5.csv
│   └── bootstrap_mediacion_secuencial_500.csv
│
└── README_REPRODUCCION.md
```

La reproducción se mantiene separada del análisis histórico.

---

## 7. Procedimiento de bootstrap en la reproducción

Cuando fue necesario reconstruir la mediación sin disponer de la implementación analítica original, el efecto indirecto se calculó como producto de coeficientes y se estimó mediante **bootstrap percentil de 500 réplicas**.

Esta implementación corresponde al procedimiento de reconstrucción y no se presenta como una afirmación de que el análisis original utilizó exactamente este método.

---

## 8. Entorno de reproducción

Para la tercera corrida de reproducción se utilizó:

```r
set.seed(20260101)
```

El script original de enero utilizaba:

```r
set.seed(1234)
```

Entorno de reproducción:

```text
R version 4.6.1 (2026-06-24 ucrt)
R >= 4.4 requerido
readxl
```

Los scripts operan en modo de solo lectura sobre las bases de entrada.

---

## 9. Verificación documental

Además de las corridas de reproducción, se realizó una verificación documental de salidas estadísticas históricas.

Las salidas localizadas en:

```text
...\MFCA-N1\Autoencodere\outputs_MFCA\
```

fueron cotejadas y conservadas en:

```text
../08_RESULTADOS_HISTORICOS/salidas_MFCA_mediacion_moderacion/
```

Esta verificación se considera distinta de una nueva ejecución computacional.

---

## 10. Distinción entre análisis y reproducción

### Análisis principal

Corresponde al análisis realizado sobre la muestra de:

```text
24 pacientes
124 observaciones
```

incluyendo la especificación de mediación, las variables y covariables documentadas, los modelos de moderación y los análisis complementarios.

### Reproducción estadística

Corresponde a procedimientos posteriores de reconstrucción, verificación o control de sensibilidad realizados sobre copias de bases y/o bases complementarias.

Los resultados de estos procedimientos se identifican separadamente en `02_RESULTADOS.md`.

---

## 11. Software

Los análisis y procedimientos de reconstrucción utilizaron:

```text
R
lavaan
lme4
mgcv
readxl
```

Los scripts de reproducción se conservan en:

```text
07_REPRODUCCION_ESTADISTICA/
```

La procedencia específica de cada variable y cifra se documenta en:

```text
04_PROCEDENCIA.md
```

Los resultados numéricos se documentan en:

```text
02_RESULTADOS.md
```
