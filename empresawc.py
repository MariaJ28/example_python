empleado= input("Ingrese el nombre completo: ")
tipo_proyecto={
    "tipo a": 20000,
    "tipo b": 10000,
    "tipo c": 5000
}

print("el valor de la hora dia es de: ",tipo_proyecto["tipo c"])

horas_laborales= 8*30
sueldo_mensual= tipo_proyecto["tipo c"]*horas_laborales

print("el valor del sueldo mensual es de: ",sueldo_mensual)

tope_maximo=1500000

if sueldo_mensual > tope_maximo:
    print("su salario es mayor a tope maximo")
else:
    porcentaje=6
    valor_porcentaje=tipo_proyecto["tipo c"]*(porcentaje/100)
    total_procentaje=tipo_proyecto["tipo c"]+ valor_porcentaje

    print("el valor de hora extra es: ",total_procentaje)

    aumento_sueldo=sueldo_mensual + total_procentaje * 3

    print("su sueldo mensual con un incremento del 6% es de: ",aumento_sueldo)


