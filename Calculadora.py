# média_visu é a média de visualizações a cada 1 real investido
media_visu= 30
# média_clq é o número de cliques para cada 100 visualizações
media_clq= 0.12
# média_compart é o compartilhamentos de cada 20 pessoas que clicaram no anúncio
media_compart= 0.15
# média_seq_compart é o número máximo de compartilhamentos em sequ6encia
media_seq_compart= 4
# média_visu_por_compart é o número de novas visualizações geradas pelos compartilhamentos
media_visu_por_compart= 40 



#invest_pub = 3.33 #coloque aqui o valor do seu investimemto inicial p 100 pessoas
while True:
    try:
        invest_pub = float(input("Coloque aqui o valor do seu investimento inicial em reais: "))

    except ValueError:
        print("Somente valores numéricos são permitidos.")
        continue
    else:
        break


qd_visualizacoes_inic = invest_pub * media_visu
qd_cliques= qd_visualizacoes_inic * media_clq
comp_vs_visu= qd_cliques * media_compart
seq_de_4_compt= comp_vs_visu * media_seq_compart
total_visualizacoes= qd_visualizacoes_inic + (media_visu_por_compart * seq_de_4_compt)

print("Com seu investimento inicial você alcançará este total de visualizações: " + str(round(total_visualizacoes)))
