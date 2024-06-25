# Ejercicios de practica - Programación Python

Ejercicios para hacer para practicar programación, basados en un sistema de contabilidad financiero.

## Para tener en cuenta

El programa simula ser un sistema para llevar registro de las entradas y salidas de dinero de una empresa o individuo, con el fin de con cada ejercicio agregar funcionalidad a este para que sea mas completo.

> Modificar SOLO el archivo `main.py`

## Consignas

Checklist:

- [ ] [Ejercicio 01 - Crear una entrada de dinero](#ejercicio-01---crear-una-entrada-de-dinero)
- [ ] [Ejercicio 02 - Crear una salida de dinero](#ejercicio-02---crear-una-salida-de-dinero)
- [ ] [Ejercicio 03 - Ver los ingresos](#ejercicio-03---ver-los-ingresos)
- [ ] [Ejercicio 04 - Ver los gastos separados por destino](#ejercicio-04---ver-los-gastos-separados-por-destino)
- [ ] [Ejercicio 05 - Ver suma de ingresos](#ejercicio-05---ver-suma-de-ingresos)
- [ ] [Ejercicio 06 - Ver suma de gastos](#ejercicio-06---ver-suma-de-gastos)
- [ ] [Ejercicio 07 - Calcular balance](#ejercicio-07---calcular-balance)
- [ ] [Ejercicio 08 - Ver Movimientos de una persona](#ejercicio-08---ver-movimientos-de-una-persona)
- [ ] [Ejercicio 09 - Ver movimientos separados por inicial de nombre](#ejercicio-09---ver-movimientos-separados-por-inicial-de-nombre)
- [ ] [Ejercicio 10 - Borrar movimientos de una persona](#ejercicio-10---borrar-movimientos-de-una-persona)

### Ejercicio 01 - Crear una entrada de dinero

Implementa una función llamada `crear_entrada` que no tome parámetros y permita registrar una nueva entrada de dinero en el sistema. La función debe pedirle al usuario los datos requeridos para crear un registro utilizando la función `input` (un id, el nombre del remitente y el monto de la entrada).

### Ejercicio 02 - Crear una salida de dinero

Implementa una función llamada `crear_gasto` que no tome parámetros y permita registrar una nueva salida de dinero en el sistema. La función debe pedirle al usuario los datos requeridos para crear un registro utilizando la función `input` (un id, el nombre del receptor y el monto de la entrada).

### Ejercicio 03 - Ver los ingresos

Implementa una función llamada `ver_ingresos` que tomando el valor que devuelve la función `ingresos()`
muestre en pantalla todos los ingresos registrados en el sistema en formato:

```s
Ingresos:
 - #1 - Persona1 +$50
 - #2 - Persona1 +$10
 - #3 - Persona2 +$50
```

La función `ingresos()` devuelve un diccionario con esta estructura:

```py
{
  "Persona1": [
    ("1", "Persona1", 50),
    ("2", "Persona1", 10),
  ],
  "Persona2": [
    ("3", "Persona2", 50)
  ]
}

```

### Ejercicio 04 - Ver los gastos separados por destino

Implementa una función llamada `ver_gastos` que tomando el valor que devuelve la función `gastos()`
muestre en pantalla todos los gastos registrados en el sistema separados por el nombre del receptor en el siguiente formato:

```s
Gastos:
  Persona1:
    -$50
    -$10
  Persona2:
    -$50
```

La función `gastos()` devuelve un diccionario con la misma estructura que la función `ingresos()`

### Ejercicio 05 - Ver suma de ingresos

Implementa una función llamada `ver_total_ingresos` que utilizando la función `ingresos()` calcule la suma de todos los ingresos de dinero y la muestre en pantalla. Ejemplo:

> Aclaración: El signo `+` simboliza que se trata de dinero entrante a la cuenta, no hace referencia al valor del numero

```s
Total de ingresos: +$5000
```

### Ejercicio 06 - Ver suma de gastos

Implementa una función llamada `ver_total_gastos` que utilizando la función `gastos()` calcule la suma de todos los gastos de dinero y la muestre en pantalla. Ejemplo:

> Aclaración: El signo `-` simboliza que se trata de dinero saliente de la cuenta, no hace referencia al valor del numero

```s
Total de gastos: -$5000
```

### Ejercicio 07 - Calcular balance

Implementa una función llamada `ver_balance` que calcule el balance de la cuenta, es decir que muestre en pantalla la diferencia de ingresos menos gastos. Ejemplos:

```s
Balance de cuenta: $60
```

```s
Balance de cuenta: $0
```

```s
Balance de cuenta: $-500
```

### Ejercicio 08 - Ver Movimientos de una persona

Implementa una función llamada `ver_movimientos_nombre` que sin tomar parámetros, pregunte al usuario un nombre y muestre todos los movimientos que este realizo (id y monto), identificando si se trata de un ingreso o egreso de dinero (con `+` y `-`). Ejemplo:

```s
Ingrese el nombre: Alma

Movimientos de Alma:
  #1 | +$1000
  #6 | -$2000
  #5 | -$20
  #3 | +$3000
```

### Ejercicio 09 - Ver movimientos separados por inicial de nombre

Implementa una función llamada `ver_movimientos_por_inicial` que muestre en pantalla los ingresos y gastos registrados en el sistema separados por la inicial (en mayúsculas) del nombre del remitente.

Tener en cuenta que hay que calcular el total para cada letra (ingresos - gastos) y poner si el total de la letra es positiva o negativa (ingreso o gasto).
Ejemplo:

```s
Movimientos:
  A: +$1000
  B: -$2000
  C: +$3000
```

### Ejercicio 10 - Borrar movimientos de una persona

Implementa una función llamada `borrar_movimientos_de` que pida al usuario el nombre de una persona, borre todos los movimientos de esta persona y cuente cuantos registros borro. Finalmente mostrar cuantos movimientos se borraron y el nombre.

> Tener en cuenta la función `clear_ingresos()` y `clear_gastos()` que al invocarlas, borran todos los registros de su respectivo tipo.

Ejemplo:

```s
Ingrese el nombre: Alma

Se borraron 5 movimientos de Alma.
```
