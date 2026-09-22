# Limitaciones

## 1. La base analítica principal no está disponible como archivo exportado

La base utilizada para el análisis principal corresponde a **425 observaciones de 39 residentes**, pero no se dispone actualmente de una exportación independiente de esa base que permita ejecutar nuevamente el modelo completo desde cero.

La reconstrucción depende parcialmente de salidas históricas y de checkpoints del entorno original. Por ello, los tres coeficientes principales están **verificados en las salidas primarias**, pero no fueron reejecutados de manera independiente sobre la base original.

---

## 2. Existe una discrepancia documental en el tamaño de muestra

El resumen histórico reporta **N = 24**, mientras que las salidas primarias del modelo principal corresponden a **425 observaciones de 39 residentes**.

El `N = 24` sí corresponde a un estudio piloto independiente de rumiación y fue reproducido exactamente.

Por tanto, no es posible atribuir sin reserva el tamaño muestral de 24 al análisis principal.

---

## 3. La construcción de los proxies no coincide completamente con la descripción del resumen

El resumen histórico describe la construcción de los proxies de capital comunitario y flexibilidad mediante **PCA y suavizado exponencial**.

El código recuperado muestra que:

* el proxy de **capital comunitario** sí utiliza PCA y suavizado exponencial con `α = 0.3`;
* el proxy de **flexibilidad psicológica** no utiliza PCA, sino una combinación de componentes con pesos fijos y posteriormente suavizado exponencial con `α = 0.3`.

Además, la varianza explicada utilizada para la selección/combinación de componentes del PCA no quedó conservada como salida persistente, y la justificación documental de los pesos del índice de flexibilidad no fue localizada.

---

## 4. La reproducción independiente no constituye una réplica exacta del procedimiento original

El análisis histórico fue implementado mediante `lavaan::sem`, con agrupamiento por `ID`, estimador `MLR`, `missing = "listwise"`, `se = "boot"` y 500 réplicas bootstrap, con `set.seed(2025)`.

La reconstrucción independiente realizada posteriormente utilizó, cuando fue necesario, productos de coeficientes y **bootstrap percentil de 500 réplicas**, con una semilla distinta.

Por ello, los resultados de las corridas de reconstrucción no deben interpretarse como equivalentes a una nueva ejecución del procedimiento estadístico original.

---

## 5. Las observaciones longitudinales y el diseño limitan la inferencia

El estudio utiliza observaciones repetidas por residente dentro de una comunidad terapéutica residencial.

El modelo histórico de ecuaciones estructurales incorporó `ID` como agrupamiento; sin embargo, la corrida externa de mediación realizada durante la reconstrucción utilizó observaciones por fila mediante modelos OLS y bootstrap, lo que puede producir una estimación de incertidumbre distinta cuando existen observaciones repetidas dentro de participante.

Además, el diseño observacional y la realización del estudio en un contexto comunitario residencial específico no permiten interpretar los coeficientes de mediación como demostración experimental de causalidad ni asumir automáticamente su generalización a otras poblaciones o contextos terapéuticos.
