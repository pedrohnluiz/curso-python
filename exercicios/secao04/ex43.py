vt = float(input('Informe o valor total: R$'))
print(f'O total a pagar com 10% de desconto: R${vt * 0.9:.2f}')
print(f'O valor de cada parcela em 3x sem juros: R${vt / 3:.2f}')
print(f'A comissão do vendedor, caso à vista (5% com desconto): R${(vt * 0.9) * 0.05}')
print(f'A comissão do vendedor, caso à parcelado (5% valor total): R${vt * 0.05:.2f}')
