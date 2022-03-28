import numpy as np
def total_marejada(M,cat):
    W= M[2,:]
    if cat ==1:
        vBool=W<100

    elif cat ==2:
        vBool=(W>=100)&(W<150)


    elif cat ==3:
        vBool=(W>=150)&(W<200)


    elif cat ==4:
        vBool=(W>=200)&(W<250)


    elif cat ==5:
        vBool=W>=250


    cumplenV = marejada[vBool]
    total = np.sum(cumplenV)

    return total

def indices_año(huracanes,año):
    yearsL=list(huracanes.keys())
    yearsL.sort() #[2000,2001,2002,2003,...]
    pos=yearsL.index(año)
    ini=0
    fin=0
    for year in yearsL[:pos-1]:
        tupla= huracanes[year]
        cantidad=len(tupla)
        ini+=cantidad
    fin=ini + len(huracanes[año])
    return (ini.fin)
def velocidad_superior(M,huracanes,año):
    ini,fin=indices_año(huracanes,año)
    Vd=M[0,:]
    VdAño=Vd[ini:fin]
    promedio=np.mean(VdAño)
    vBool=VdAño>promedio
    cantidad=np.sum(vBool)
    return cantidad
