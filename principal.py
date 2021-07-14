from src.leilao.dominio import Usuario, Lance, Leilao
# para comparar shortcuts
# https://www.jetbrains.com/help/rider/Reference_Keyboard_Shortcuts_Index.html#context_navigation
mat = Usuario('Mateus')
re = Usuario('Regina')

lance_mat = Lance(mat, 100.00)
lance_re = Lance(re, 150.00)

leilao = Leilao('Celular')

leilao.lances.append(lance_mat)
leilao.lances.append(lance_re)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')
