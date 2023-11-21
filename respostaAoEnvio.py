import esocial.xml
import esocial.client
import json

ide_empregador = {
    'tpInsc': 1,
    'nrInsc': '47622281000188' # CNPJ/CPF completo (com 14/11 dígitos)
}

ide_transmissor = {
    'tpInsc': 1,
    'nrInsc': '21969023000189' # CNPJ/CPF completo (com 14/11 dígitos)
}

esocial_ws = esocial.client.WSClient(
    pfx_file='HT.pfx',
    pfx_passw='ht380801',
    employer_id=ide_empregador,
    # Se o transmissor é o próprio empregador, não precisa informar o "sender_id"
    sender_id=ide_transmissor,
    target='production'
)

# De posse do número do protocolo de envio
#1400068440000002023111907493500002
response = esocial_ws.retrieve('1.1.202311.0000000007117098642')

# response vai ser um Element object
#<Element {http://www.esocial.gov.br/schema/lote/eventos/envio/retornoProcessamento/v1_3_0}eSocial at 0x>
print(esocial.xml.dump_tostring(response, xml_declaration=False, pretty_print=True))

response_decoded = esocial.xml.decode_response(response)

print(json.dumps(response_decoded.toDict(), indent=4))