import esocial.xml
import esocial.client
import json

class ConsultaRespostaEnvioLote():
    def __init__(self):

        self.ide_empregador = {
            'tpInsc': 1,
            'nrInsc': ''  # CNPJ/CPF completo (com 14/11 dígitos)
        }

        self.ide_transmissor = {
            'tpInsc': 1,
            'nrInsc': '21969023000189' # CNPJ/CPF completo (com 14/11 dígitos)
        }

        self.esocial_ws = esocial.client.WSClient(
            pfx_file='HT.pfx',
            pfx_passw='ht380801',
            employer_id=self.ide_empregador,
            # Se o transmissor é o próprio empregador, não precisa informar o "sender_id"
            sender_id=self.ide_transmissor,
            target='production'
        )
    def consultaReciboLote(self, reciboLote, nrInsc):
        self.ide_empregador['nrInsc'] = nrInsc
        response = self.esocial_ws.retrieve(reciboLote)

        #print(esocial.xml.dump_tostring(response, xml_declaration=False, pretty_print=True))

        response_decoded = esocial.xml.decode_response(response)

        dados = response_decoded.toDict()

        # Acessando a lista de 'eventos'
        for evento in dados.get('eventos', []):
            # Convertendo todo o dicionário 'processamento' em uma string de texto
            esocial_consulta_lote_api_processamento = json.dumps(evento.get('processamento', {}), indent=4)

            # Obtendo o valor de 'recibo', mesmo que seja None (null)
            esocial_consulta_lote_api_recibo = evento.get('recibo')

        return esocial_consulta_lote_api_processamento, esocial_consulta_lote_api_recibo

if __name__ == '__main__':
    consulta = ConsultaRespostaEnvioLote()
    esocial_consulta_lote_api_processamento, esocial_consulta_lote_api_recibo = consulta.consultaReciboLote("1.2.202311.0000000000145487334")

    # Imprimindo os valores
    print("Processamento:")
    print(esocial_consulta_lote_api_processamento)
    print("\nRecibo:")
    print(esocial_consulta_lote_api_recibo)