num = int(input('Informe um valor em segundos: '))
hr = (num // 3600)
min = int((num % 3600) / 60)
seg = int((min % 60) % 60)
print(f'O resultado é {hr} hora(s) e {min} minutos e {seg} segundos')
