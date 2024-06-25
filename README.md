
[![Funcionamiento](https://github.com/MateoDi9z/ejercicio-practica-contabilidad/actions/workflows/python-tests.yml/badge.svg)](https://github.com/MateoDi9z/ejercicio-practica-contabilidad/actions/workflows/python-tests.yml)
# Sistema de contabilidad para practicar python

Sistema para registrar salidas y entradas de dinero.

> Modificar unicamente el archivo `main.py`

## Que hacer

- Leer este archivo para entender como funciona.
- Leer el archivo `main.py` para tener una idea de la estructura del programa.
- Leer la lista de ejercicios para realizar la cual se encuentra en [el archivo de CONSIGNAS.md](./CONSIGNAS.md)
- Resolver ejercicio por ejercicio!

## Funciones a utilizar

Los datos de nuestro programa se guardan en un archivo para que persistan aunque nuestro código termine de ejecutarse, para interactuar con este archivo se deben utilizar las siguientes funciones:

```py
# Ejemplos

## Crear registros
# def crear_nuevo_ingreso(str, str, int) -> None:
crear_nuevo_ingreso("1", "Mateo", 100)
crear_nuevo_egreso("1", "Mateo", 50)

## Ver registros
# def crear_nuevo_ingreso() -> dict:
print(ingresos())
print(gastos())

## Borrar registros
# def clear_ingresos() -> None:
clear_ingresos()
clear_gastos()
```

### ¿ Como funciona un sistema de contabilidad ?

Una tabla de contabilidad se basa en una tabla de 2 columnas, gastos e ingresos. Cada registro es un nuevo gasto o un nuevo ingreso.

Para calcular el balance de la cuenta, se deben sumar todos los ingresos y a eso restarle la suma de todos los gastos.

Si el resultado del balance es negativo, quiere decir que la cuenta debe dinero. Si es positivo el balance no tiene deudas.

```s
Gastos | Ingresos
-----------------
    10 | 5
```

> Balance: `Ingresos` - `Gastos` = `5 - 10` = `-5`

## Contacto

Si tienes alguna pregunta o necesitas ayuda, no dudes en preguntarme por discord (mi usuario es matedi9z) o por [Github](https://github.com/MateoDi9z)
