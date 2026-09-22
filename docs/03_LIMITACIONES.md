# Limitaciones

## 1. La base analítica principal no está disponible como archivo exportado independiente

La muestra analítica del proyecto comprende **24 pacientes y 124 observaciones longitudinales**. Actualmente no se dispone de una exportación independiente de la base completa que permita volver a ejecutar íntegramente el análisis desde cero en las mismas condiciones originales.

Por ello, algunos resultados del análisis principal se sustentan en las salidas estadísticas históricas recuperadas y no en una nueva ejecución independiente sobre una copia de la base original.

---

## 2. El tamaño muestral es reducido para la complejidad del modelo

El análisis principal se realizó con **24 pacientes**, con observaciones repetidas que suman **124 registros**.

Aunque las observaciones longitudinales aumentan el número de registros disponibles para el análisis, no equivalen a 124 participantes independientes. Por tanto, la información efectiva para la inferencia entre individuos continúa estando limitada por el número de pacientes.

Esto restringe la precisión con la que pueden estimarse modelos con múltiples rutas de mediación, covariables y términos de interacción.

---

## 3. La construcción de los proxies no coincide completamente con la descripción del resumen

El resumen histórico describe la construcción de los proxies de capital comunitario y flexibilidad mediante **PCA y suavizado exponencial**.

El código recuperado muestra que:

* el proxy de **capital comunitario** utiliza PCA y suavizado exponencial con `α = 0.3`;
* el proxy de **flexibilidad psicológica** no utiliza PCA, sino una combinación de componentes con pesos fijos, seguida de suavizado exponencial con `α = 0.3`.

Además, la varianza explicada utilizada para la selección o combinación de componentes del PCA no quedó conservada como salida persistente, y no se localizó una justificación documental de los pesos utilizados en el índice de flexibilidad.

---

## 4. La reproducción independiente no constituye una réplica exacta del procedimiento original

El análisis histórico fue implementado mediante `lavaan::sem`, con agrupamiento por `ID`, estimador `MLR`, `missing = "listwise"`, `se = "boot"` y 500 réplicas bootstrap, con `set.seed(2025)`.

La reconstrucción independiente realizada posteriormente utilizó, cuando fue necesario, productos de coeficientes y **bootstrap percentil de 500 réplicas**, con una semilla distinta.

Por ello, los resultados de las corridas de reconstrucción no deben interpretarse como equivalentes a una nueva ejecución del procedimiento estadístico original.

---

## 5. El diseño longitudinal y observacional limita la inferencia causal y la generalización

Las 124 observaciones corresponden a mediciones repetidas de **24 pacientes** dentro de una comunidad terapéutica residencial.

Aunque el modelo histórico incorporó el agrupamiento por `ID`, la estructura longitudinal implica dependencia entre observaciones del mismo paciente y limita la interpretación de los registros como unidades independientes.

Además, el diseño observacional no permite interpretar los coeficientes de mediación como demostración experimental de causalidad.

Finalmente, los resultados proceden de una comunidad terapéutica residencial específica y, por tanto, su generalización a otras poblaciones, instituciones o modalidades de tratamiento requiere evidencia adicional.
