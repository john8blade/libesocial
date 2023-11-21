import esocial.xml
import esocial.client

class enviaLote():
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
    def enviaS_2220(self, xml_S_2220):

        evento1_grupo1 = esocial.xml.load_fromstring(xml_S_2220)
        #evento2_grupo1 = esocial.xml.load_fromfile('evento2.xml')

# Adicionando eventos ao lote. O evento já vai ser assinado usando o certificado fornecido e validado contra o XSD do evento
# Se gen_event_id == True, o Id do evento é gerado pela lib (default = False)
        evento1_id, evento1_assinado = self.esocial_ws.add_event(evento1_grupo1, gen_event_id=False)
#evento2_id, evento2_assinado = esocial_ws.add_event(evento2_grupo1, gen_event_id=True)

        result, batch_xml = self.esocial_ws.send(group_id=2)



# result vai ser um Element object
# <Element {http://www.esocial.gov.br/schema/lote/eventos/envio/retornoEnvio/v1_1_0}eSocial at 0x>
        print(esocial.xml.dump_tostring(result, xml_declaration=False, pretty_print=True))

# batch_xml vai ser um Element object com o XML de envio de lote
# <Element {http://www.esocial.gov.br/schema/lote/eventos/envio/v1_1_1}eSocial at 0x>
        print(esocial.xml.dump_tostring(batch_xml, xml_declaration=False, pretty_print=True))