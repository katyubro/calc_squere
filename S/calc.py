def circleS(radius):
    if(radius <= 0):
        raise ValueError('Не существует круга с введенными параметрами')
    square = 3.1415*radius**2
    return square


def triangleS(fSide, sSide, tSide):
    if(fSide+sSide<=tSide or
       tSide+sSide<=fSide or
       fSide+tSide<=sSide or
       fSide <= 0 or sSide <= 0 or tSide <=0):
        raise ValueError('Не существует треугольника с введенными параметрами!')
    else:
        p=(fSide+sSide+tSide)/2 
        square =(p*(p-fSide)*(p-sSide)*(p-tSide))**(1/2)
        return square

def triangleR(fSide, sSide, tSide):
    if(fSide+sSide<=tSide or
       tSide+sSide<=fSide or
       fSide+tSide<=sSide or
       fSide <= 0 or sSide <= 0 or tSide <=0):
        raise ValueError('Не существует треугольника с введенными параметрами!')
    elif(fSide**2+sSide**2==tSide**2 or
           tSide**2+sSide**2==fSide**2 or
           fSide**2+tSide**2==sSide**2):
        return True
    else:
        return False

print(triangleS(70, 130, 110))
