from pylatex import Document, Section, Subsection,Math, NoEscape
from sympy import Matrix, latex
import latexify
doc = Document()
"""
print("Que tipo de matriz cuadrada quieres ingresar? 2x2 o 3x3")
decs = input();
if decs == "2":
    #matriz 2x2
    dim= "2x2"
    print("Perfecto, por favor ingresa tu matriz de dimension "+dim +" de manera horizontal")
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    matrix = Matrix([[a, b], [c, d]])
    matrix_latex = latex(matrix)
    with doc.create(Section("Reduccion y factorizacion de matriz")):
        doc.append(Math(data=[NoEscape(matrix_latex)]))
        with doc.create(Subsection("Procedimiento")):
         for i in range(10):
            matrix = Matrix([[i, b], [c, d]])
            matrix_latex = latex(matrix)
            doc.append(Math(data=[NoEscape(matrix_latex)]))
    
else:
    #matriz 3x3
    dim= "3x3"
    print("Perfecto, por favor ingresa tu matriz de dimension "+dim +" de manera horizontal")
    a, b, c = map(int, input().split())
    d, e, f = map(int, input().split())
    g, h, i = map(int, input().split())

    matrix = Matrix([[a, b, c], [d, e, f], [g, h, i]])
    matrix_latex = latex(matrix)


"""
"""
#x=input()
matrix = Matrix([[2, 3], [3, 4]])
matrix_latex = latex(matrix)  #this is a raw LaTeX string
#sopenc
#latexify-py for symbolic function representation

@latexify.function
def row_op(x):
    return 2 * x
"""

   
    #doc.append(Math(data=[NoEscape(str(row_op))]))    

print("Ingresa la dimension de tu matriz cuadrada")
dim = int(input())

matrix=[]
for i in range(dim):
    row = []
    for j in range(dim):
        val = int(input(f"Ingresa el valor para la posicion [{i+1}][{j+1}]: "))
        row.append(val)
    matrix.append(row)
    
matrix_sym = Matrix(matrix)
matrix_latex = latex(matrix_sym)

with doc.create(Section("Reduccion y factorizacion de matriz")):
        doc.append(Math(data=[NoEscape(matrix_latex)]))
        






#compile to PDF
doc.generate_pdf("output", clean_tex=False)
