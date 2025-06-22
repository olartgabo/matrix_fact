from pylatex import Document, Section, Subsection,Math, NoEscape
from sympy import Matrix, latex
doc = Document()

def reduccionGauss(drow, urow,column):
    selec = drow[column]/urow[column]
    
    newrow = selec*urow
    showrow= drow-newrow
    return showrow, selec
    
def clean_matrix(mat):
    cleaned = []
    for row in mat:
        cleaned_row = []
        for val in row:
            if isinstance(val, float) and val.is_integer():
                cleaned_row.append(int(val))
            else:
                cleaned_row.append(val)
        cleaned.append(cleaned_row)
    return cleaned
 

print("Ingresa la dimension de tu matriz cuadrada")
dim = int(input())

matrix=[]
iden=[]
for i in range(dim):
    row = []
    fil = []
    for j in range(dim):
        val = float(input(f"Ingresa el valor para la posicion [{i+1}][{j+1}]: "))
        row.append(val)
        if(i==j):
            valo=1
            fil.append(valo)
        else:
            valo =0
            fil.append(valo)
    matrix.append(row)
    iden.append(fil)


matrix = clean_matrix(matrix)
iden = clean_matrix(iden)

matrix_sym = Matrix(matrix)
matrix_latex = latex(matrix_sym)
origmat=matrix_latex
iden_sym = Matrix(iden)
iden_latex = latex(iden_sym)

doc.append(Math(data=[]))

with doc.create(Section(" Factorización A=LU ")):
    doc.append("Vamos a hacer reduccion de Gauss tomando en cuenta la siguiente estructura:")
    doc.append(Math(data=["\nFila[x]-(k)Fila[y]"]))
    doc.append("Siendo:") 
    doc.append(Math(data=["\nFila[x]"]))
    doc.append("La fila la cual queremos reducir")
    doc.append(Math(data=["\nFila[y]"]))
    doc.append("La fila a la cual pertenece el pivot\n")
    doc.append(Math(data=["\n(k)"]))
    doc.append("El numero a ser multiplicado para permitir la reduccion\n")
    with doc.create(Subsection("Matriz Ingresada: ")):
        doc.append(Math(data=[NoEscape(matrix_latex)]))
    with doc.create(Subsection("Procedimiento")):
        numbers= []
        for pivot in range (dim-1):
            for indexcol in range(1,dim):
                if pivot==indexcol or pivot>indexcol:
                    continue
                impo, selec = reduccionGauss(matrix_sym.row(indexcol), matrix_sym.row(pivot),pivot)
                numbers.append(selec)
                matrix_sym[indexcol, :] = impo
                iden[indexcol][pivot]=selec
                iden_sym = Matrix(iden)
                iden_latex = latex(iden_sym)
                doc.append(Math(data=[f"Fila[{indexcol+1}]-({selec})*Fila[{pivot+1}]"]))
                matrix_latex = latex(matrix_sym)
                doc.append(Math(data=[NoEscape(iden_latex),NoEscape(matrix_latex)]))
        
        print(numbers)
       
    with doc.create(Subsection("Resultado")):
        doc.append("Factorizacion matricial:")
        doc.append(Math(data=["\n A     = L       U"]))
        doc.append(Math(data=[NoEscape(origmat), "=",NoEscape(iden_latex),NoEscape(matrix_latex)]))
        
        

        






#compile to PDF
doc.generate_pdf("output", clean_tex=False)
