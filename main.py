from pylatex import Document, Section, Subsection,Math, NoEscape
from sympy import Matrix, latex
import latexify

#x=input()
matrix = Matrix([[2, 3], [3, 4]])
matrix_latex = latex(matrix)  #this is a raw LaTeX string
#sopenc
#latexify-py for symbolic function representation
@latexify.function
def row_op(x):
    return 2 * x

doc = Document()
with doc.create(Section("Reduccion y factorizacion de matriz")):
    doc.append(Math(data=[NoEscape(matrix_latex)]))   
    doc.append(Math(data=[NoEscape(str(row_op))]))    

#compile to PDF
doc.generate_pdf("output", clean_tex=False)
