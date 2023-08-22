"""
Estruturas Condicionais
if (Se), else, elif (else if)
"""

idade = 26

"""
# Estritura condicional if, else em C

if(idade < 18){
    printf("Menor de idade\n");
}else if(idade == 18){
    printf("Tem 18 anos\n");
}else{
    printf("Maior de idade\n");
}
"""

"""
# Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Maior de idade");
}
"""

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
elif idade == 16:
    print("Tem 26 anos")
else:
    print("Maior de idade")


if idade < 18:
    print("Menor de idade")

if idade == 18:
    print("Tem 18 anos")

if idade == 26:
    print("Tem 26 anos")

if idade > 18:
    print("Maior de idade")
