nombre_cliente=input("digita tu nombre completo: ")
docuento=input("digita tu numero de documento:")

productos={
    "jabon liquido": 10000,
    "sal": 5000,
    "papel higienico": 20000,
    "aceite":12000,
    "mecato":25000
}

print (productos)
precio=productos["aceite"]+ productos["jabon liquido"]+productos["mecato"]+productos["papel higienico"]+productos["sal"]
print("total del mercado: ",precio)

saldo=900000
valor_domicilio=10000
total_compra=precio + valor_domicilio

if saldo >= total_compra:
    print("tu compra sera entregada por un domiciliario con un total de: ",total_compra)
else:
    print("no te alcanza para llevarlo en domicilio ya que tu presupuesto es de: ",saldo)

sum=0
num=5
a=0
while(a<num):
    sum=sum*a
    a=a+1
    print(sum)


if edad<15