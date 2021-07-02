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

def calcula(invest_pub): 
    estimativas = dict()
    estimativas['qd_visualizacoes_inic']=invest_pub * media_visu
    estimativas['qd_cliques']=estimativas['qd_visualizacoes_inic'] * media_clq
    estimativas['comp_vs_visu']= estimativas['qd_cliques'] * media_compart
    estimativas['seq_de_4_compt'] = estimativas['comp_vs_visu'] * media_seq_compart
    estimativas['total_visualizacoes']= estimativas['qd_visualizacoes_inic'] + (media_visu_por_compart * estimativas['seq_de_4_compt'])
    return estimativas

def imprime(invest_pub):
    estimativas = calcula(invest_pub)
    print("Com seu investimento inicial você alcançará este total de visualizações: " + str(round(estimativas['total_visualizacoes'])))
    print("Com seu investimento inicial alcançará até: " + str(round(estimativas['qd_cliques'])))
    print("Com seu investimento inicial você alcançará esta quantidade máxima de compartilhamentos : " + str(round(estimativas['seq_de_4_compt'])))
    

def main():
    



    #invest_pub = 3.33 #coloque aqui o valor do seu investimemto inicial p 100 pessoas
    while True:
        try:
            invest_pub = float(input("Coloque aqui o valor do seu investimento inicial em reais: "))
        except ValueError:
            print("Somente valores numéricos são permitidos.")
            continue
        else:
            break

    imprime(invest_pub)

if __name__ == "__main__":
    main()





