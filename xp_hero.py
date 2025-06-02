nome_do_heroi = input("Informe o nome do herói: ")
xp_do_heroi = int(input("Informe a experiência do herói: "))
nivel = ""

if xp_do_heroi <= 1000:
    nivel = "Ferro"
elif xp_do_heroi <= 1001 and xp_do_heroi <= 2000:
    nivel = "Bronze"
elif xp_do_heroi <= 2001 and xp_do_heroi <= 5000:
    nivel = "Prata"
elif xp_do_heroi <= 5001 and xp_do_heroi <= 7000:
    nivel = "Ouro"
elif xp_do_heroi <= 7001 and xp_do_heroi <= 8000:
    nivel = "Platina"
elif xp_do_heroi <= 8001 and xp_do_heroi <= 9000:
    nivel = "Ascendente"
elif xp_do_heroi <= 9001 and xp_do_heroi <= 10000:
    nivel = "Imortal"
elif xp_do_heroi <= 10001:
    nivel = "Radiante"

print(f'\nO herói de nome ' + nome_do_heroi + ' está no nível de experiência ' + nivel + '.\n')