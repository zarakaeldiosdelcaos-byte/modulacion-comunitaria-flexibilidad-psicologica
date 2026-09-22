# Estado del estudio

> **INVESTIGACIÓN EN PROCESO.** Este documento describe qué compone el estudio, en qué etapa se encuentra y
> hacia dónde avanza. Los resultados que publica el repositorio son **preliminares**.

**Última actualización:** 22 de septiembre de 2026

---

## 1. El estudio en una frase

Un estudio longitudinal en una comunidad terapéutica residencial que examina **cómo se articulan los procesos
psicológicos individuales y las condiciones comunitarias del entorno** en la recuperación de los trastornos
por consumo de sustancias.

En concreto, evalúa si la indefensión se asocia al malestar cognitivo **a través** de la evitación conductual
y del déficit de reforzadores ambientales, y si el **capital comunitario** y la **flexibilidad psicológica**
modifican alguna de esas relaciones.

---

## 2. Cómo está compuesto el estudio

### 2.1 Marco conceptual

| Proceso | Papel en el modelo |
|---|---|
| **Indefensión** | Variable predictora; punto de partida de la cadena |
| **Evitación conductual** | Primer mediador; reduce el contacto con fuentes de reforzamiento |
| **Reforzadores ambientales** | Segundo mediador; su déficit sostiene el malestar |
| **Malestar cognitivo** | Desenlace del modelo |
| **Capital comunitario** | Condición del entorno que modula la cadena |
| **Flexibilidad psicológica** | Proceso de aproximación conductual alternativo a la evitación |

### 2.2 Base empírica

* **425 observaciones persona-semana**
* **39 participantes** en tratamiento residencial
* Seguimiento longitudinal, con identificador de participante
* La unidad de análisis es la **observación persona-semana**, no el participante

### 2.3 Instrumentos y medidas

| Dominio | Medida |
|---|---|
| Evitación y activación conductual | BADS |
| Reforzadores ambientales | EROS |
| Malestar cognitivo | ATQ-8 |
| Rumiación | RRS-SF |
| Indefensión, capital comunitario y flexibilidad psicológica | Índices compuestos construidos para este análisis |

Los tres índices compuestos **no son escalas estandarizadas**: son construcciones específicas del estudio, y
así se reportan en toda la documentación.

### 2.4 Análisis

| Componente analítico | Técnica |
|---|---|
| Modelo principal | Mediación secuencial, ecuaciones estructurales |
| Procesos del entorno | Modelos de moderación con términos de interacción |
| Seguimiento longitudinal | Modelos mixtos con efecto aleatorio por participante |
| Exploración de no linealidad | Modelos aditivos generalizados |
| Incertidumbre de los efectos indirectos | Bootstrap de 500 réplicas |

### 2.5 Líneas de trabajo del programa

El programa de investigación comprende dos líneas que se documentan por separado:

1. **Línea principal — modulación comunitaria y flexibilidad psicológica.** Es la que documenta este
   repositorio.
2. **Línea complementaria — intervención breve sobre rumiación.** Estudio piloto controlado, con
   **N = 24** (14 tratamiento / 10 comparación). Se reporta en [`docs/02_RESULTADOS.md`](docs/02_RESULTADOS.md) §6
   y **no describe la base analítica de la línea principal**.

A ello se suman los reanálisis sobre bases complementarias y un control externo de la cadena de mediación,
todos identificados como tales en la documentación.

### 2.6 Materiales que componen el repositorio

| Bloque | Contenido |
|---|---|
| `docs/` | Método, resultados, limitaciones y procedencia de cada cifra |
| `figuras/` | Figuras del modelo: las del análisis y las regeneradas para difusión |
| `tablas/` | Coeficientes clave con su error estándar, intervalo y valor p |
| `codigo/` | Script reproducible que genera las figuras desde los coeficientes publicados |
| `difusion/` | Materiales de presentación en congresos y referencias verificadas |
| `assets/` | Imágenes de presentación del proyecto |

---

## 3. En qué etapa se encuentra

| # | Etapa | Estado |
|---|---|---|
| 1 | Recolección de datos longitudinales | **Completada** |
| 2 | Estimación de los modelos | **Completada** |
| 3 | Verificación de cada cifra contra su salida estadística | **Completada** |
| 4 | Documentación metodológica abierta | **Publicada en este repositorio** |
| 5 | Difusión científica de los resultados preliminares | **En curso** |
| 6 | Manuscrito para publicación | **Siguiente etapa** |

La etapa 3 merece una nota, porque es poco habitual y define este repositorio: **cada coeficiente publicado
aquí está trazado hasta el archivo de salida que lo produjo**, y esa correspondencia se documenta en
[`docs/04_PROCEDENCIA.md`](docs/04_PROCEDENCIA.md). Cualquiera puede seguir el rastro de una cifra hasta su
origen.

---

## 4. Hacia dónde va

### Difusión inmediata (2026)

Los resultados preliminares se presentan en el circuito científico durante este año:

* **Cartel** — XI Reunión Nacional de Investigación en Psicología.
* **Ponencia oral** — Primer Coloquio de Avances de Investigación, Capítulo México de la ACBS
  (10 de octubre de 2026).

### Cierre del análisis

* Consolidar la documentación metodológica del modelo principal.
* Publicar la versión final de los resultados agregados, con los análisis de sensibilidad ya realizados
  incorporados.
* Profundizar el estudio de los índices comunitarios: la línea de indicadores del entorno es la que más
  recorrido tiene y la que conecta con el desarrollo posterior del programa.

### Manuscrito

Preparación del manuscrito para publicación, con el modelo de mediación secuencial y los resultados de
moderación como núcleo.

---

## 5. Cómo leer los resultados

1. **Son preliminares.** Corresponden a un estudio en curso. Se recomienda citar la versión etiquetada del
   repositorio y no presentarlos como definitivos.
2. **La unidad de análisis es la observación persona-semana.** Las 425 observaciones corresponden a 39
   participantes y no equivalen a 425 participantes independientes.
3. **Los índices de capital comunitario y flexibilidad psicológica son construcciones del análisis**, no
   escalas estandarizadas.
4. **El efecto de moderación varía según la operacionalización del capital comunitario.** El repositorio
   reporta esa variación junto con el resultado principal, en lugar de presentar sólo el coeficiente más
   favorable.
5. **El análisis tiene carácter exploratorio** y su documentación metodológica se elaboró de forma paralela a
   la estimación.

Las limitaciones del diseño se detallan en [`docs/03_LIMITACIONES.md`](docs/03_LIMITACIONES.md).

---

## 6. Cómo participar

Las observaciones metodológicas son bienvenidas a través de la pestaña **Issues** del repositorio. Es la vía
más útil para hacer llegar comentarios sobre el planteamiento, la especificación de los modelos, la
construcción de los índices comunitarios o la presentación de los resultados.

El proyecto valora especialmente la discusión sobre la **medición del capital comunitario**: es la línea con
mayor margen de desarrollo y el punto donde una lectura externa resulta más provechosa.
