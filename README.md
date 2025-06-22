# Factorización A = LU

Este proyecto es una herramienta hecha en Python que realiza la **factorización LU** de una matriz cuadrada utilizando el método de eliminación de Gauss. 
El procedimiento/desarollo se genera automáticamente en un archivo PDF utilizando LaTeX.

## Librerías utilizadas

* [SymPy](https://docs.sympy.org/latest/index.html): para el manejo simbólico de las matrices y operaciones matemáticas.
* [PyLaTeX](https://jeltef.github.io/PyLaTeX/current/#): para la creación del documento PDF en formato LaTeX que documenta la factorización.

## Requerimientos

Para ejecutar este proyecto de manera local, se necesitan algunas herramientas adicionales, especialmente para compilar el documento LaTeX generado.

### En VSCode:

* **Extensión**: [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
* **Compilador LaTeX**: [MikTeX](https://miktex.org/download) (Recomendacion personal)
* **Complemento para MikTeX**: [Strawberry Perl](https://strawberryperl.com/) (Necesario en Windows para MikTeX)

> **Nota para Linux**: En lugar de MikTeX y Perl se puede usar herramientas como **TeX Live** que incluye lo necesario para compilar documentos LaTeX.

## Ejecución del programa

1. Ejecutar el script en la terminal o desde VSCode. El programa pedirá ingresar la dimensión de la matriz y luego los valores uno por uno.
2. El script realizará la factorización LU paso a paso, aplicando reducción de Gauss, y mostrará en el documento generado cada operación realizada en notación matemática.

3. Al final, se generará un archivo `output.pdf` con:

   * La matriz original.
   * Cada paso del proceso de eliminación.
   * Las matrices `L` y `U` resultantes.
   * La ecuación final: `A = LU`.

## Ejemplo:

Al ingresar una matriz de tamaño 3x3, el programa pedirá lo siguiente:

```text
Ingresa la dimension de tu matriz cuadrada
3
Ingresa el valor para la posicion [1][1]: 2
Ingresa el valor para la posicion [1][2]: 3
Ingresa el valor para la posicion [1][3]: 1
...
```

En el PDF generado se incluirá algo similar a:

```
Matriz Ingresada:
⎡2  3  1⎤
⎢4  7  2⎥
⎣6  8  3⎦

Procedimiento:
Fila[2] - (2.0)*Fila[1]
...

Resultado:
A = L * U
```

## Archivos generados

* `output.pdf`: Documento con todo el procedimiento.
* `output.tex`: Archivo LaTeX fuente.
> El archivo LaTeX puede ser usado para revision de bugs


