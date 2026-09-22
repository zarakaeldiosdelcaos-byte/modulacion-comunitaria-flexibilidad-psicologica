# Limitaciones

> **Investigación en proceso.** Las limitaciones se enuncian como propiedades del diseño y de los datos
> disponibles, y se presentan junto con los resultados para facilitar su lectura crítica.

## 1. La base analítica no se distribuye como archivo independiente

La base analítica del proyecto comprende **425 observaciones persona-semana correspondientes a 39 participantes**.

Por tratarse de información clínica de personas en tratamiento residencial, la base no se publica como archivo independiente. La verificación de los resultados se apoya en las salidas estadísticas conservadas del análisis, que se documentan en `04_PROCEDENCIA.md` y quedan disponibles para su cotejo.

Por ello, algunos resultados del análisis se sustentan en las salidas estadísticas del proyecto y no en una nueva ejecución independiente sobre una copia de la base original.

---

## 2. El tamaño muestral es reducido para la complejidad del modelo

El análisis se realizó con **39 participantes**, con observaciones repetidas que suman **425 registros**.

Aunque las observaciones longitudinales aumentan el número de registros disponibles para el análisis, no equivalen a 425 participantes independientes. Por tanto, la información efectiva para la inferencia entre individuos continúa estando limitada por el número de participantes.

Esto restringe la precisión con la que pueden estimarse modelos con múltiples rutas de mediación, covariables y términos de interacción.

---

## 3. La construcción de los índices no coincide completamente con la descripción del resumen

El resumen del proyecto describe la construcción de los índices de capital comunitario y flexibilidad mediante **PCA y suavizado exponencial**.

El código del análisis muestra que:

* el índice de **capital comunitario** utiliza PCA y suavizado exponencial con `α = 0.3`;
* el índice de **flexibilidad psicológica** no utiliza PCA, sino una combinación de componentes con pesos fijos, seguida de suavizado exponencial con `α = 0.3`.

Además, la varianza explicada utilizada para la selección o combinación de componentes del PCA no quedó conservada como salida persistente, y no se localizó una justificación documental de los pesos utilizados en el índice de flexibilidad.

---

## 4. La reproducción independiente no constituye una réplica exacta del procedimiento original

El análisis fue implementado mediante `lavaan::sem`, con agrupamiento por `ID`, estimador `MLR`, `missing = "listwise"`, `se = "boot"` y 500 réplicas bootstrap, con `set.seed(2025)`.

La reconstrucción independiente realizada posteriormente utilizó, cuando fue necesario, productos de coeficientes y **bootstrap percentil de 500 réplicas**, con una semilla distinta.

Por ello, los resultados de las corridas de reconstrucción se presentan como procedimientos de verificación y no como una nueva ejecución del procedimiento estadístico original.

---

## 5. El diseño longitudinal y observacional limita la inferencia causal y la generalización

Las 425 observaciones corresponden a mediciones repetidas de **39 participantes** dentro de una comunidad terapéutica residencial.

Aunque el modelo incorporó el agrupamiento por `ID`, la estructura longitudinal implica dependencia entre observaciones del mismo participante y limita la interpretación de los registros como unidades independientes.

Además, el diseño observacional no permite interpretar los coeficientes de mediación como demostración experimental de causalidad.

Finalmente, los resultados proceden de una comunidad terapéutica residencial específica y, por tanto, su generalización a otras poblaciones, instituciones o modalidades de tratamiento requiere evidencia adicional.

---

## 6. Sin registro previo del análisis

El análisis no fue registrado previamente. Su documentación metodológica se elaboró de forma paralela y
posterior a la estimación. Se trata, por tanto, de un análisis de carácter exploratorio, y los resultados se
presentan como tales.
