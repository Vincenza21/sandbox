## @file conto_documentato.py
#  @brief Semplice implentazione di un conto bancario con opzioni di deposito e prelievo

## @brief Rappresenta yn conto bancario con intestatario e saldo
#  @details Consente di depositare e prelevare denaro. Il prelievo è vietato
#           se il saldo risultante sarebbe negativo.
class ContoBancario():

    ## @brief Inizializza un nuovo conto bancario.
    #  @param intestatario Nome dell'intestatario del conto.
    def __init__ (self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    ## @brief Deposita una somma di denaro sul conto.
    #  @param importo Somma da depositare.
    def deposita(self, importo):
        self.saldo += importo

    ## @brief Preleva una somma di denaro dal conto.
    #  @param importo Somma da prelevare.
    #  @exception valueError sollevata se il saldo e insufficiente
    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo
            
    def __str__ (self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print (conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata: ', e)

if __name__ == "__main__":
    main()
