import mysql.connector
import unidecode



class Banco:

    def __init__(self):
        self.conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='banco'
        )


    def procurarMedicamento(self, palavra):
        cursor = self.conexao.cursor()
        #comando = """select Nome, Indicacao, Posologia, efeitosColaterais, Contraindicacoes
        #from medicamento where Nome = %s"""
        #comando = """select * from medicamento where Nome = %s"""
        palavra = "%" + unidecode.unidecode(palavra) + "%"
        print("Palavra: " + palavra)
        comando = """select * from medicamento where Nome like %s"""
        cursor.execute(comando, (palavra,))
        resultado = cursor.fetchall()
        cursor.close()
        self.conexao.close()
        return resultado


    def listarMedicamento(self, tipo):
        cursor = self.conexao.cursor()
        comando = """select Nome from medicamento where tipoMedicamento = %s"""
        cursor.execute(comando, (tipo,))
        resultado = cursor.fetchone()
        cursor.close()
        self.conexao.close()
        for x in resultado:
            print(resultado[x][0])


    def tipoQtde(self, tipo):
        cursor = self.conexao.cursor()
        comando = """select count(tipoMedicamento) FROM medicamento WHERE tipoMedicamento = %s"""
        cursor.execute(comando, (tipo,))
        resultado = cursor.fetchall()
        cursor.close()
        self.conexao.close()
        return f'{resultado[0][0]} MEDICAMENTOS DISPONÍVEIS'


# banco = Banco()
#
#
#
# resultado = banco.procurarMedicamento("Dipirona")
#
# print(resultado)




