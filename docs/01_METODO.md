# Método

## 1. Diseño

Estudio con **medidas repetidas** realizado en una comunidad terapéutica residencial, con observaciones semanales por residente.

La unidad longitudinal de observación fue la combinación **residente-semana**. Debido a esta estructura repetida, `ID` se utilizó como identificador de participante y variable de agrupamiento en los análisis que incorporaron dependencia intraindividuo.

El análisis se orientó a examinar la relación temporal y estadística entre **indefensión, evitación, reforzamiento ambiental y malestar cognitivo**, incorporando además indicadores de contexto comunitario y flexibilidad psicológica.

---

## 2. Muestra y unidad de análisis

La base analítica principal comprendió:

* **39 residentes**
* **425 observaciones persona-semana**

La unidad de agrupamiento fue `ID`, correspondiente a cada residente.

El número histórico de **24 participantes** corresponde a un estudio piloto independiente de rumiación y **no constituye la muestra del análisis principal**. Esa base se utilizó únicamente en procedimientos posteriores de verificación y reproducción documental.

Las bases externas utilizadas para controles de sensibilidad o reconstrucción se consideran independientes de la muestra principal y no se utilizan para redefinir su tamaño muestral.

---

## 3. Variables e instrumentos

### 3.1 Indefensión

La variable predictora principal del modelo de mediación fue `indefension_idx_z`.

La variable se incorporó en forma estandarizada (`z`) en la especificación recuperada del modelo principal.

El procedimiento exacto mediante el cual se construyó originalmente `indefension_idx_z` no quedó completamente localizado en los materiales disponibles y, por tanto, no se reconstruye aquí una fórmula que no esté documentada en la fuente primaria.

---

### 3.2 Evitación y activación: BADS

La conducta de evitación se representó mediante `BADS_evitacion`, derivada del instrumento **Behavioral Activation for Depression Scale (BADS)**.

En el modelo secuencial, esta variable constituye el **primer mediador**:

$$
\text{Indefensión} \rightarrow \text{Evitación}
$$

---

### 3.3 Reforzamiento ambiental: EROS

El reforzamiento ambiental se representó mediante `EROS_total`, derivado de la escala **Environmental Reward Observation Scale (EROS)**.

En el modelo secuencial, constituye el **segundo mediador**:

$$
\text{Evitación} \rightarrow \text{Reforzamiento ambiental}
$$

---

### 3.4 Malestar cognitivo: ATQ-8

El desenlace principal del modelo de mediación fue `ATQ8_total`, derivado del **Automatic Thoughts Questionnaire, versión de 8 ítems (ATQ-8)**.

En la especificación principal, `ATQ8_total` representa el componente de **malestar cognitivo / pensamientos automáticos negativos**.

---

### 3.5 Variables comunitarias y longitudinales

Se incorporaron variables relacionadas con el contexto comunitario y la progresión temporal:

* `semana_norm`: semana normalizada.
* `dico_capital_compuesto`: indicador compuesto de capital comunitario.
* `dico_balance`: indicador de balance comunitario utilizado como covariable.

Estas variables se incorporaron como covariables en las ecuaciones del modelo principal.

---

### 3.6 Índice de capital comunitario

El capital comunitario se representó mediante un índice compuesto construido a partir de un **análisis de componentes principales (PCA)** aplicado a **13 indicadores normalizados**.

Posteriormente, el índice fue sometido a un procedimiento de **suavizado exponencial por residente**, con el propósito de generar una representación longitudinal del constructo.

La definición operativa de este índice debe distinguirse de otros indicadores de capital utilizados en análisis complementarios; no se consideran automáticamente equivalentes.

---

### 3.7 Índice de flexibilidad psicológica

La flexibilidad psicológica se representó mediante un índice compuesto ponderado basado en componentes de:

* proceso,
* activación,
* evitación.

El índice fue sometido al mismo procedimiento de suavizado longitudinal por residente utilizado para el indicador comunitario.

Los pesos exactos y la fórmula completa de combinación no se reproducen en este documento mientras no estén respaldados de manera inequívoca por la fuente primaria de construcción.

---

### 3.8 Rumiación

La rumiación se incluyó en análisis complementarios y modelos adicionales, pero **no forma parte de la cadena principal de mediación secuencial** descrita en este documento.

Cuando se utilizó la variable correspondiente, se distinguió explícitamente de los componentes BADS de evitación y de los índices comunitarios.

---

## 4. Análisis estadístico

### 4.1 Modelo de mediación secuencial

Se especificó un modelo de **ecuaciones estructurales** para evaluar la siguiente cadena:

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

Los coeficientes, intervalos de confianza y valores de `p` correspondientes se reportan exclusivamente en `02_RESULTADOS.md`.

---

### 4.2 Estimación del modelo principal

La especificación estadística documentada para el modelo original utilizó:

* **R**
* **`lavaan`** para el modelo de ecuaciones estructurales
* estimador **MLR**
* agrupamiento por participante mediante `ID`
* tratamiento de datos faltantes mediante **casos completos por modelo** en la especificación recuperada
* **500 réplicas bootstrap**
* semilla documentada en la ejecución original: `2025`

En la reconstrucción posterior se mantuvo separada esta especificación histórica de las decisiones adoptadas específicamente para reproducirla.

---

### 4.3 Moderación por capital comunitario

Se evaluaron modelos en los que indicadores de capital comunitario se incorporaron como posibles moderadores de las relaciones entre los componentes de la cadena de mediación.

El análisis incluyó términos de interacción y se examinó la relación entre:

* evitación,
* capital comunitario,
* reforzamiento ambiental.

La especificación exacta de cada término de interacción se conserva en los scripts de análisis correspondientes.

Los coeficientes de interacción, intervalos de confianza y valores de `p` se reportan en `02_RESULTADOS.md`.

---

### 4.4 Moderación por flexibilidad psicológica

Se evaluó la participación de la flexibilidad psicológica como variable moderadora dentro de la estructura de mediación.

Los modelos examinaron tanto sus efectos principales como los términos de interacción correspondientes a las relaciones especificadas en el análisis.

La interpretación de los efectos condicionales se reserva para `02_RESULTADOS.md`; este documento únicamente describe su procedimiento de estimación.

---

### 4.5 Modelo combinado

Se estimó adicionalmente un modelo que incorporó simultáneamente los indicadores de:

* capital comunitario,
* flexibilidad psicológica,
* términos de interacción correspondientes.

Este análisis tuvo como finalidad evaluar ambos procesos dentro de una misma especificación estadística.

No se presentan aquí los coeficientes ni los valores de significancia.

---

### 4.6 Modelos mixtos para el desenlace semanal

Para analizar el comportamiento longitudinal del desenlace semanal se utilizaron **modelos mixtos**, considerando la estructura repetida de las observaciones por residente.

La implementación documentada utilizó:

```text
R / lme4
```

La inclusión de `ID` permitió representar la dependencia derivada de las observaciones repetidas dentro de cada participante.

Las fórmulas específicas de los modelos mixtos se conservan en los scripts reproducibles y no se reconstruyen aquí cuando la especificación completa no está documentada en el material metodológico.

---

### 4.7 Modelos aditivos generalizados

Se evaluaron posibles relaciones no lineales mediante **modelos aditivos generalizados (GAM)**.

La implementación documentada utilizó:

```text
R / mgcv
```

Los modelos GAM se utilizaron para examinar términos suaves asociados con los indicadores comunitarios y de flexibilidad.

Los resultados de los términos suaves se reportan en `02_RESULTADOS.md`.

---

## 5. Datos faltantes y estandarización

No se realizó imputación de datos en los procedimientos de reconstrucción.

Las estimaciones se calcularon utilizando **casos completos para cada modelo**, y el tamaño analítico correspondiente se reportó por separado para cada especificación cuando fue necesario.

No se aplicó estandarización de variables de manera oculta durante la reconstrucción.

Cuando una variable fue utilizada en escala estandarizada, dicha transformación se identificó explícitamente en la variable correspondiente, como en `indefension_idx_z`.

Los modelos de reconstrucción conservaron y reportaron por separado las escalas originales (`b`) y estandarizadas (`β`) cuando ambas fueron calculadas.

---

## 6. Reproducción estadística

La reproducción estadística se desarrolló como un procedimiento independiente de **reconstrucción y verificación**.

Ningún archivo original fue modificado. Los scripts de reproducción operan sobre copias de las bases depositadas en:

```text
../03_BASES_DE_DATOS/
```

La estructura de reproducción fue:

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

La reproducción debe interpretarse como **verificación de trazabilidad y sensibilidad**, no como sustitución del análisis original.

---

### 6.1 Corrida 1: moderación y rumiación

Se utilizó la base:

```text
Rumia_preliminar.xlsx
```

Esta base corresponde al estudio piloto histórico de **24 participantes**.

Su función en la reproducción fue verificar los coeficientes de moderación previamente documentados y la correspondencia de la muestra histórica.

Esta base no modifica el tamaño muestral del estudio principal.

---

### 6.2 Corrida 2: BADS, EROS y ATQ

Se utilizó:

```text
Registro Quincenal BADS EROS ATQ INV.xlsx
```

El objetivo fue determinar qué relaciones podían estimarse en la única base disponible que contenía conjuntamente variables BADS y EROS.

Esta corrida se considera un análisis de **estimabilidad y verificación**, no una sustitución de la base analítica principal.

---

### 6.3 Corrida 3: reconstrucción de mediación secuencial

Se utilizó:

```text
narraciones_rumia.csv
```

con:

* 251 observaciones
* 21 participantes (`ID`)

Esta base constituye un **control externo de sensibilidad** y no corresponde a la muestra principal de 39 residentes.

Por esta razón, sus resultados no se utilizan para redefinir, confirmar o refutar el modelo principal del proyecto.

Además, el desenlace utilizado en esta base no es idéntico al desenlace principal del modelo original.

---

## 7. Procedimiento de bootstrap en la reproducción

Cuando se reconstruyó la mediación secuencial sin disponer de la implementación analítica original, el efecto indirecto se calculó como **producto de coeficientes** y se estimó mediante **bootstrap percentil de 500 réplicas**.

Esta decisión se adoptó exclusivamente como procedimiento de reconstrucción compatible con la documentación disponible, que indicaba “bootstrapping (500 réplicas)”, sin que se hubiera localizado la función original utilizada para generar dicho procedimiento.

Por tanto:

> El bootstrap implementado durante la reproducción **no debe interpretarse como evidencia de que el análisis original utilizó exactamente este procedimiento**.

En particular, la reconstrucción no sustituye una implementación original de `lavaan` ni presupone el uso de intervalos sesgo-corregidos de Preacher–Hayes.

---

## 8. Semillas y entorno reproducible

Para la tercera corrida de reproducción se utilizó:

```r
set.seed(20260101)
```

El script original de enero utilizaba:

```r
set.seed(1234)
```

La diferencia se mantiene explícita porque el bootstrap puede depender de la semilla.

Entorno utilizado para la reproducción:

```text
R version 4.6.1 (2026-06-24 ucrt)
R >= 4.4 requerido
paquete readxl
```

Los scripts son independientes y de solo lectura respecto de las bases de entrada.

Ejemplo de ejecución en Windows mediante `Rscript`:

```bash
"/c/Program Files/R/R-4.6.1/bin/Rscript.exe" \
  "G:/Mi unidad/RECONSTRUCCION_MODULACION_COMUNITARIA_FLEXIBILIDAD/07_REPRODUCCION_ESTADISTICA/codigo/REPRODUCCION_moderacion_rumia.R"
```

---

## 9. Verificación documental de resultados históricos

Además de las corridas de reproducción, se realizó una **verificación documental de las salidas primarias**.

Las salidas originales localizadas en:

```text
...\MFCA-N1\Autoencodere\outputs_MFCA\
```

fueron cotejadas y copiadas en:

```text
../08_RESULTADOS_HISTORICOS/salidas_MFCA_mediacion_moderacion/
```

Esta verificación documental constituye un procedimiento distinto de la reproducción computacional.

Su función es establecer la trazabilidad entre los coeficientes históricamente reportados y los archivos primarios generados por el análisis original.

---

## 10. Trazabilidad y conservación de archivos

Los procedimientos de reproducción se ejecutan exclusivamente sobre copias de las bases.

Los scripts:

* no modifican los archivos originales;
* escriben sus resultados únicamente dentro de `07_REPRODUCCION_ESTADISTICA/`;
* conservan logs de ejecución;
* generan archivos de salida diferenciados por corrida;
* permiten distinguir entre resultados reproducidos y resultados procedentes de salidas históricas.

La procedencia específica de cada cifra se documenta por separado en:

```text
04_PROCEDENCIA.md
```

---

## 11. Distinción entre análisis original y reconstrucción

Para evitar una falsa equivalencia metodológica, este repositorio distingue explícitamente:

### Análisis original

Corresponde al análisis estadístico documentado y/o recuperado de las fuentes primarias del proyecto, incluyendo la especificación SEM, sus variables, covariables, estructura de mediación, agrupamiento por participante y procedimiento de estimación documentado.

### Reproducción estadística

Corresponde a los procedimientos desarrollados posteriormente para verificar, reconstruir o someter a control de sensibilidad determinados resultados cuando la base analítica original o parte de su implementación no estaba disponible.

La reproducción **no reemplaza** el análisis original y sus resultados no deben presentarse como si provinieran de la misma muestra, base de datos o implementación estadística.

---

## 12. Software y herramientas

Los análisis se realizaron en el entorno R y utilizaron, según el procedimiento:

```text
lavaan
lme4
mgcv
readxl
```

La documentación de ejecución y los scripts reproducibles se conservan en:

```text
07_REPRODUCCION_ESTADISTICA/
```

Los resultados numéricos, intervalos de confianza y valores de `p` se reportan en:

```text
02_RESULTADOS.md
```
