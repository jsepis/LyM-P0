import re

specialWords=["defvar","=","turn","move","face","put","pick",":left",":right",":around",":north",":south","east",":front",":back","move-dir","run-dirs","move-face","skip"]

#Divide la instruccion en sus componentes individuales
def instructionDivider(linea: str) -> list():
    lineaList=re.split(r'[ ()]',linea)
    for i in lineaList:
        if i=='':
            lineaList.remove(i)
    return lineaList

#Revisa si el indice se sale de la lista 
def checkIndex(lineaList: list, index: int())->bool:
    try:
        lineaList[index]
        b=True
    except IndexError:
        b=False
    return b


#Revisa si una innstruccion con estructura Tipo Nombre Variable esta bien
def insTNV(lineaList: list, specialWords: list())->bool:
    if (lineaList[0] == "defvar" or lineaList[0] == "=" or lineaList[0] == "mov-dir" or lineaList[0] == "pick" or lineaList[0] == "put") and (checkIndex(lineaList, 0)):
        if (lineaList[1] not in specialWords) and (checkIndex(lineaList, 1)):
            if (lineaList[2].isdigit()) and (checkIndex(lineaList, 2)):
                if checkIndex(lineaList, 3)==False:
                    return True
    return False



def main(linea: str)->bool:
    lineaList=instructionDivider(linea)
    r=insTNV(lineaList, specialWords)
    print (r)

linea="(put x 1)"
main(linea)


