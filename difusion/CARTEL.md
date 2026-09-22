# Esquema para el cartel científico

**Proyecto:** *Modulación comunitaria y flexibilidad psicológica en la recuperación de adicciones: un estudio de mediación secuencial*

**Evento:** XI Reunión Nacional de Investigación en Psicología — trabajo aceptado.

**Documento:** esquema de trabajo para la construcción del cartel.

> Este archivo es el **plano científico y gráfico del cartel**. No constituye el cartel final.

---

# 1. Objetivo del documento

Definir la arquitectura científica, gráfica y documental del cartel a partir de los resultados y fuentes conservados en el repositorio.

El cartel debe:

* presentar únicamente resultados documentados;
* distinguir análisis principal, análisis complementarios y reproducción;
* utilizar la base analítica de **425 observaciones persona-semana correspondientes a 39 participantes**;
* mantener trazabilidad entre cada cifra y su fuente;
* distinguir resultados estadísticos de interpretaciones;
* hacer explícitas las principales limitaciones metodológicas.

---

# 2. Inventario gráfico disponible

Las figuras del proyecto se conservan dentro del repositorio de presentaciones y carteles.

```text
11_ABSTRACTS_POSTERS_PRESENTACIONES/

├── figuras_recuperadas/
│
├── figuras_generadas/
│
└── codigo_figuras/
    └── figuras_cartel.py
```

## 2.1 Figuras originales recuperadas

| Archivo                                         | Contenido                                                         | Uso previsto                     |
| ----------------------------------------------- | ----------------------------------------------------------------- | -------------------------------- |
| `mod_proxy_evit_eros_cap.png`                   | Moderación de la relación evitación → EROS por niveles de capital | Figura principal                 |
| `mod_proxy_evit_eros_flex.png`                  | Relación evitación → EROS por niveles de flexibilidad             | Figura secundaria                |
| `mod_proxy_eros_atq_cap.png`                    | Moderación de capital en EROS → ATQ-8                             | Opcional                         |
| `mod_proxy_eros_atq_flex.png`                   | Moderación de flexibilidad en EROS → ATQ-8                        | Opcional                         |
| `mod_proxy_indef_evit_cap.png`                  | Moderación de capital en indefensión → evitación                  | Opcional                         |
| `mod_proxy_indef_evit_flex.png`                 | Moderación de flexibilidad en indefensión → evitación             | Opcional                         |
| `mod_evit_eros_bal.png`                         | Moderación con balance comunitario                                | Sensibilidad                     |
| `mod_eros_atq_bal.png`                          | Moderación con balance comunitario en EROS → ATQ-8                | Opcional                         |
| `mod_indef_evit_bal.png`                        | Moderación con balance comunitario en indefensión → evitación     | Opcional                         |
| `diagrama_mediacion_dos_pasos.png`              | Diagrama histórico del modelo de mediación                        | Sustituir por versión regenerada |
| `diagrama_SEM.png`                              | Diagrama general del modelo SEM                                   | Referencia interna               |
| `mediacion_indefension.png`                     | Representación gráfica de la mediación                            | Referencia interna               |
| `interaccion_indefension_EROS.png`              | Interacción indefensión × EROS                                    | Opcional                         |
| `evitacion_ATQ_por_EROS.png`                    | Relación evitación → ATQ-8                                        | Opcional                         |
| `red_centrada_EROS.png`                         | Red centrada en EROS                                              | Opcional                         |
| `GAM_smooth_dico_capital_comunitario.png`       | Término suave para capital comunitario                            | Figura de sensibilidad           |
| `GAM_smooth_dico_flexibilidad_act.png`          | Término suave para flexibilidad                                   | Opcional                         |
| `delta_ATQ_vs_indefension.png`                  | Cambio en ATQ-8 frente a indefensión                              | Opcional                         |
| `evolucion_indefension.png`                     | Evolución temporal de indefensión                                 | Opcional                         |
| `trayectoria_indefension_idx_z_por_cluster.png` | Trayectorias por conglomerado                                     | Opcional                         |
| `scree_pca_indefension_idx_z.png`               | Sedimentación de PCA del índice de indefensión                    | Opcional                         |

---

## 2.2 Figuras generadas para el cartel

Las siguientes figuras se reconstruyen a partir de coeficientes documentados en las salidas estadísticas. **No utilizan datos simulados.**

| Figura                                      | Contenido                                                                                     | Prioridad          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------ |
| `fig1_diagrama_mediacion_secuencial.png`    | `a1 = 10.013`, `a2 = 0.730`, `b1 = 0.374`, efecto indirecto = `2.735`, efecto total = `2.303` | **Imprescindible** |
| `fig2_efectos_indirectos_condicionales.png` | Efecto indirecto condicional bajo, medio y alto de capital                                    | **Imprescindible** |
| `fig3_forest_moderaciones.png`              | Coeficientes principales de moderación y efectos asociados                                    | **Imprescindible** |
| `fig4_sensibilidad_al_proxy.png`            | Comparación de resultados según indicador de capital                                          | **Recomendada**    |
| `fig5_matriz_correlaciones.png`             | Matriz de correlaciones del análisis                                                          | Recomendada        |
| `fig6_modelos_multinivel.png`               | Resultados complementarios del desenlace ATQ-8                                                | Recomendada        |

Toda figura generada para el cartel debe conservar su procedencia en el código y/o en el pie de figura.

---

# 3. Selección de figuras para el cartel

Se propone utilizar entre **4 y 6 elementos gráficos**, de acuerdo con el espacio disponible.

| Ranura | Figura                                      | Función                                                                      |
| ------ | ------------------------------------------- | ---------------------------------------------------------------------------- |
| R1     | `fig1_diagrama_mediacion_secuencial.png`    | Mostrar la estructura y magnitud del modelo                                  |
| R2     | `fig2_efectos_indirectos_condicionales.png` | Mostrar los efectos indirectos condicionales                                 |
| R3     | `mod_proxy_evit_eros_cap.png`               | Representación visual de la interacción evitación–capital–EROS               |
| R4     | `fig4_sensibilidad_al_proxy.png`            | Mostrar sensibilidad del resultado a la definición del indicador comunitario |
| R5     | `fig5_matriz_correlaciones.png`             | Contexto de las relaciones entre variables                                   |
| R6     | `GAM_smooth_dico_capital_comunitario.png`   | Mostrar el análisis no lineal complementario                                 |

La selección final dependerá de las dimensiones y de la legibilidad del cartel.

---

# 4. Arquitectura propuesta del cartel

```text
┌────────────────────────────────────────────────────────────┐
│ TÍTULO · AUTORES · FILIACIÓN · IDENTIFICACIÓN DEL EVENTO │
├────────────────────────┬───────────────────────────────────┤
│ INTRODUCCIÓN           │ RESULTADOS                        │
│                        │                                   │
│ OBJETIVO               │ Figura 1                          │
│                        │ Figura 2                          │
│ MÉTODO                 │ Figura 3                          │
│                        │ Figura 4                          │
│                        │                                   │
│                        │ DISCUSIÓN                          │
│                        │ CONCLUSIONES                       │
│                        │ LIMITACIONES                       │
│                        │ REFERENCIAS / QR                   │
└────────────────────────┴───────────────────────────────────┘
```

## 4.1 Diseño visual exploratorio

Como parte de la fase inicial de producción se generó un **diseño visual exploratorio con Gemini**
para visualizar una posible distribución del cartel.

Este material tiene únicamente función de referencia durante la etapa de diseño. **No corresponde al
cartel final y será descartado antes de la versión definitiva.**

La imagen se conserva en `assets/` exclusivamente como registro del proceso de exploración visual.

<p align="center">
  <img
    src="assets/diseno-prueba-gemini-product.jpg"
    alt="Diseño visual exploratorio del cartel generado como prueba"
    width="85%"
  >
</p>

> **Estado:** diseño exploratorio / descartable.  
> **Uso:** referencia visual para evaluar composición, jerarquía y distribución de elementos.

---

# 5. Proporción sugerida de contenidos

| Bloque                 | Área aproximada | Función                               |
| ---------------------- | --------------: | ------------------------------------- |
| Encabezado             |             8 % | Identificación                        |
| Introducción           |         10–12 % | Contextualización                     |
| Objetivo               |           5–6 % | Pregunta del estudio                  |
| Método                 |            18 % | Diseño, muestra, variables y análisis |
| Resultados             |            30 % | Figuras y cifras principales          |
| Discusión              |            12 % | Interpretación                        |
| Limitaciones           |             7 % | Alcance del estudio                   |
| Referencias / contacto |           7–8 % | Fuentes y acceso al repositorio       |

El formato final deberá ajustarse a las especificaciones oficiales del evento.

---

# 6. Contenido científico del cartel

## 6.1 Encabezado

**Título:**

> *Modulación comunitaria y flexibilidad psicológica en la recuperación de adicciones: un estudio de mediación secuencial*

Incluir:

* autores;
* filiaciones;
* identificación del evento;
* información de contacto;
* QR al repositorio, cuando corresponda.

---

## 6.2 Introducción

La introducción debe formular el problema sin presentar como hechos resultados que todavía no hayan sido demostrados.

Se propone organizarla en tres movimientos:

1. El análisis examina procesos psicológicos asociados con el malestar cognitivo dentro de un contexto de tratamiento residencial.
2. El modelo integra indefensión, evitación y reforzamiento ambiental.
3. El proyecto incorpora indicadores de contexto comunitario y flexibilidad psicológica como variables adicionales del modelo.

No utilizar afirmaciones generales del tipo “la investigación rara vez…” salvo que estén respaldadas por referencias documentadas.

---

## 6.3 Objetivo

**Objetivo principal:**

> Examinar la relación entre indefensión y malestar cognitivo mediante una secuencia que incorpora evitación y reforzamiento ambiental, y evaluar el papel de los indicadores de capital comunitario y flexibilidad psicológica dentro del modelo.

---

## 6.4 Método

| Elemento                 | Información                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| Diseño                   | Medidas repetidas en comunidad terapéutica residencial            |
| Base analítica           | **425 observaciones persona-semana / 39 participantes**           |
| Unidad de análisis       | Observación persona-semana                                        |
| Identificador            | `ID`                                                              |
| Variables principales    | `indefension_idx_z`, `BADS_evitacion`, `EROS_total`, `ATQ8_total` |
| Variables comunitarias   | Capital comunitario y balance comunitario                         |
| Flexibilidad             | Índice compuesto de proceso, activación y evitación               |
| Análisis principal       | Modelo de ecuaciones estructurales                                |
| Software                 | R / `lavaan`                                                      |
| Estimación               | MLR; agrupamiento por `ID`; bootstrap de 500 réplicas             |
| Análisis complementarios | Modelos mixtos y GAM                                              |

El capital comunitario fue construido mediante PCA sobre 13 indicadores normalizados y posteriormente suavizado longitudinalmente.

La flexibilidad psicológica fue representada mediante un índice compuesto ponderado y posteriormente suavizada longitudinalmente.

---

# 7. Resultados principales

## 7.1 Mediación secuencial

La cadena analizada fue:

$$
\text{Indefensión}
\rightarrow
\text{Evitación}
\rightarrow
\text{EROS}
\rightarrow
\text{ATQ-8}
$$

Resultados documentados:

* Indefensión → evitación: `10.013`, IC 95 % `[7.080, 12.947]`, `p < .001`.
* Evitación → EROS: `0.730`, IC 95 % `[0.666, 0.794]`, `p < .001`.
* EROS → ATQ-8: `0.374`, IC 95 % `[0.269, 0.480]`, `p < .001`.
* Efecto indirecto secuencial: **`2.735`**, IC 95 % `[1.633, 3.837]`, `p < .001`.
* Efecto total: **`2.303`**, IC 95 % `[1.366, 3.241]`, `p < .001`.

> La etiqueta “efecto indirecto total” utilizada en el resumen histórico se refiere a `indirect1 = a1 × a2 × b1`; el parámetro `total` del modelo tiene un valor distinto.

---

## 7.2 Moderación por capital comunitario

La interacción entre evitación y capital comunitario sobre EROS fue:

$$
\beta=0.195,\quad IC95\%=[0.024,0.366],\quad p=.026
$$

Los efectos indirectos condicionales documentados fueron:

| Capital | Efecto indirecto |      p |
| ------- | ---------------: | -----: |
| Bajo    |            1.711 |   .074 |
| Medio   |            2.804 | < .001 |
| Alto    |            4.150 |   .017 |

Para el cartel debe utilizarse la formulación descriptiva:

> **La magnitud del efecto indirecto varió según el nivel del indicador de capital comunitario.**

No es necesario presentar esta variación como evidencia causal.

---

## 7.3 Flexibilidad psicológica

El efecto principal de flexibilidad sobre EROS fue:

$$
\beta=-3.559,\quad IC95\%=[-6.604,-0.515],\quad p=.022
$$

El término de interacción con evitación fue:

$$
\beta=0.001,\quad p=.987
$$

Por tanto, el cartel debe distinguir explícitamente:

> **La flexibilidad mostró una asociación directa con EROS en el modelo; no se observó una interacción significativa entre flexibilidad y evitación.**

No debe describirse como “moderación por flexibilidad”.

---

## 7.4 Resultados complementarios

Se podrán mostrar, según espacio:

* EROS → ATQ-8 en modelos complementarios;
* interacción indefensión × EROS;
* términos suaves de capital y flexibilidad;
* resultados de modelos mixtos.

Los análisis complementarios deben identificarse visualmente como tales para no confundirlos con la mediación principal.

---

# 8. Sensibilidad del indicador de capital

Una figura específica puede mostrar la variación del coeficiente de interacción según la definición del indicador utilizado.

| Indicador          | Coeficiente |      p |
| ------------------ | ----------: | -----: |
| Proxy de capital C |     `0.195` | `.026` |
| `dico_balance`     |     `0.452` | `.039` |
| Capital crudo      |     `0.045` | `.154` |

Esta figura debe titularse de manera descriptiva, por ejemplo:

> **Sensibilidad de la interacción a la definición del indicador comunitario**

y no debe presentarse como evidencia de una única estimación invariable del efecto.

---

# 9. Discusión

La discusión debe distinguir entre resultados directamente observados y posibles interpretaciones.

### Resultado central

El modelo documenta una cadena estadística entre indefensión, evitación, EROS y ATQ-8, así como una interacción entre el indicador de capital comunitario y la evitación.

### Interpretación posible

Una interpretación sustantiva es que el contexto comunitario podría modificar la relación entre evitación y reforzamiento ambiental.

### Interpretación metodológica

El resultado también debe interpretarse considerando que los indicadores de capital y flexibilidad son **índices construidos para este análisis**, no instrumentos psicométricos independientes con una validación específica para este modelo.

La figura de sensibilidad debe conservarse precisamente para mostrar que la magnitud del efecto depende de la definición operacional del indicador comunitario.

---

# 10. Conclusiones

1. El modelo documentó una asociación indirecta secuencial entre indefensión, evitación, EROS y ATQ-8.
2. La relación entre evitación y EROS varió según el indicador de capital comunitario utilizado.
3. La flexibilidad psicológica mostró un efecto principal sobre EROS, pero no una interacción significativa con la evitación.

Las conclusiones deben mantenerse en términos asociativos y estadísticos y no formularse como demostraciones experimentales de causalidad.

---

# 11. Limitaciones

El cartel debe conservar las principales limitaciones documentadas en `03_LIMITACIONES.md`:

1. **Base analítica:** 425 observaciones persona-semana de 39 participantes; las observaciones repetidas no equivalen a 425 participantes independientes.
2. **Tamaño muestral individual:** el número de participantes limita la precisión de modelos con múltiples parámetros.
3. **Índices derivados:** capital comunitario y flexibilidad son construcciones específicas del análisis.
4. **Reconstrucción:** algunos procedimientos posteriores de reproducción no son idénticos a la implementación histórica.
5. **Generalización e inferencia:** el diseño observacional y el contexto residencial específico limitan la inferencia causal y la generalización.

---

# 12. Referencias

Las referencias del cartel deberán seleccionarse de:

```text
06_REFERENCIAS.md
```

Se utilizarán únicamente las fuentes que puedan identificarse documentalmente en el corpus.

No se añadirá una bibliografía externa únicamente para completar el número de referencias.

La versión final del cartel deberá utilizar las referencias estrictamente necesarias para:

* los instrumentos principales;
* el marco conceptual directamente relacionado con el análisis;
* el método estadístico, cuando corresponda.

---

# 13. Producción de figuras

Las figuras generadas para el cartel se conservarán en:

```text
11_ABSTRACTS_POSTERS_PRESENTACIONES/
```

El script de generación se conserva en:

```text
11_ABSTRACTS_POSTERS_PRESENTACIONES/codigo_figuras/figuras_cartel.py
```

Las figuras reconstruidas deben utilizar exclusivamente coeficientes y parámetros documentados en las salidas del análisis.

No deben generarse datos sintéticos para representar resultados empíricos.

Cada figura debe permitir identificar, mediante el código o el pie correspondiente, la fuente del coeficiente utilizado.

---

# 14. Checklist de producción

* [ ] Confirmar dimensiones y orientación exigidas por el evento.
* [ ] Confirmar autores, orden y filiaciones.
* [ ] Utilizar **425 observaciones / 39 participantes** en todo el cartel.
* [ ] Verificar que ninguna figura conserve cifras correspondientes a otra versión de la base.
* [ ] Incorporar `fig1`, `fig2` y `fig3` como núcleo de resultados.
* [ ] Considerar `fig4` para documentar sensibilidad del indicador comunitario.
* [ ] Mantener identificados los análisis complementarios.
* [ ] Sustituir el diagrama histórico de baja resolución por la figura regenerada.
* [ ] Mantener la procedencia de las cifras en pies de figura o documentación asociada.
* [ ] Revisar que las referencias utilizadas estén documentadas en `06_REFERENCIAS.md`.
* [ ] Verificar legibilidad del texto y de las figuras en el tamaño final.

---

# 15. Elementos que no deben aparecer en el cartel

No incluir:

* `N = 24` como muestra de este análisis: corresponde al estudio piloto de rumiación, otra línea de trabajo;
* una afirmación de que `425 observaciones` o `39 participantes` pertenecen a otro estudio;
* afirmaciones de causalidad derivadas de la mediación;
* “moderación por flexibilidad” como conclusión;
* una afirmación de que el capital comunitario tiene un efecto único independiente de su definición;
* afirmaciones de validación psicométrica de los proxies que no estén documentadas;
* referencias bibliográficas reconstruidas;
* rutas absolutas del entorno de trabajo;
* información de usuario, equipo o sistema operativo que no sea necesaria para reproducir el análisis;
* instrucciones personales de instalación o uso de VS Code dentro del cartel.

---

# 16. Relación con la documentación del repositorio

El cartel debe ser consistente con:

```text
01_METODO.md
02_RESULTADOS.md
03_LIMITACIONES.md
04_PROCEDENCIA.md
06_REFERENCIAS.md
07_REPRODUCCION_ESTADISTICA/
```

La regla general es:

```text
MÉTODO
    ↓
qué se hizo

RESULTADOS
    ↓
qué se observó

LIMITACIONES
    ↓
qué restringe la interpretación

PROCEDENCIA
    ↓
de dónde salió cada cifra

REFERENCIAS
    ↓
qué fuentes documentales sustentan el proyecto

REPRODUCCIÓN
    ↓
qué pudo verificarse posteriormente
```
