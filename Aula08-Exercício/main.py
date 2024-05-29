from Desktop import Desktop
from Notebook import Notebook
from Categoria import Categoria

cat01 = Categoria( 1 , "Gamer" )
cat02 = Categoria( 2 , "Escritório" )


n1 = Notebook("Seila","2000","10", cat01, "50")
n2 = Notebook("tomagap","5002","30", cat02 , "60")
n3 = Notebook("opa","2020","56",cat01, "90")

d1 = Desktop("samsung","verde","2500",cat01,  "500w")
d2 = Desktop("dell", "amarelo", "3500",cat02,  "750w")
d3 = Desktop("corsair", "preto", "8000",cat01,  "1000w")

print(n1.getInformacoes())
print(n2.getInformacoes())
print(n3.getInformacoes())
print(d1.getInformacoes())
print(d2.getInformacoes())
print(d3.getInformacoes())