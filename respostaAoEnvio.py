import esocial.xml
import esocial.client
import json

class ConsultaRespostaEnvioLote():
    def __init__(self):

        self.ide_empregador = {
            'tpInsc': 1,
            'nrInsc': '47622281000188' # CNPJ/CPF completo (com 14/11 dígitos)
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
    def consultaReciboLote(self, reciboLote):

        response = self.esocial_ws.retrieve(reciboLote)

        print(esocial.xml.dump_tostring(response, xml_declaration=False, pretty_print=True))

        response_decoded = esocial.xml.decode_response(response)

        print(json.dumps(response_decoded.toDict(), indent=4))