from flask import request
from lxml import etree
import esocial.xml
import respostaAoEnvio
import enviaLote

def add_routes(app):
    @app.route('/', methods=['POST'])
    def upload_xml():
        # Imprimir todos os cabeçalhos da requisição
        print("Cabeçalhos Recebidos:")
        user = request.headers.get('user')
        pw = request.headers.get('password')
        event = request.headers.get('evento')
        print(user,pw,event)
        # Verifica se há dados na requisição
        if request.data:
            xml_data = request.data  # Obtém os dados XML diretamente
            # Aqui, você pode processar o XML conforme necessário
            # Por exemplo, salvar em um arquivo, analisar, etc.
            element = esocial.xml.load_fromstring(xml_data)
            xml = etree.tostring(element, pretty_print=True).decode()
            print(xml)
            #teste = enviaLote.enviaLote()
            #teste.enviaS_2220(xml_data)
            return "XML recebido com sucesso", 200
        else:
            return "Nenhum dado XML recebido", 400


    @app.route('/consulta-envio', methods=['POST'])
    def consulta_envio():
        user = request.headers.get('user')
        pw = request.headers.get('password')
        event = request.headers.get('evento')
        print(user, pw, event)

        if request.data:
            reciboLote = request.data.decode('utf-8')
            consultaDoRecibo = respostaAoEnvio.ConsultaRespostaEnvioLote()
            consultaDoRecibo.consultaReciboLote(reciboLote)
            print('Recibo Consultado: ',reciboLote)
            return "Status", 200
        else:
            return "Erro", 400