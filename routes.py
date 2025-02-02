from flask import request, jsonify
from lxml import etree
import esocial.xml
import respostaAoEnvio
import enviaLote


def add_routes(app):
    @app.route('/', methods=['POST'])
    def upload_xml():
        # Imprimir todos os cabeçalhos da requisição
        #print("Cabeçalhos Recebidos:")
        user = request.headers.get('user')
        pw = request.headers.get('password')
        event = request.headers.get('evento')
        nrInsc = request.headers.get('nrInsc')
        #print(user,pw,event,nrInsc)
        # Verifica se há dados na requisição
        if request.data:
            print(request.data)
            xml_data = request.data  # Obtém os dados XML diretamente
            # Aqui, você pode processar o XML conforme necessário
            # Por exemplo, salvar em um arquivo, analisar, etc.
            element = esocial.xml.load_fromstring(xml_data)
            xml = etree.tostring(element, pretty_print=True).decode()
            #print(xml)
            teste = enviaLote.enviaLote()
            status, dados_recepcao_lote, xml_data = teste.enviaS_2220(nrInsc, xml_data)
            print(status)
            print(dados_recepcao_lote)
            return jsonify({'status': status, 'dadosRecepcaoLote': dados_recepcao_lote, 'esocial_envio_retorno' : xml_data}), 200
        else:
            return "Nenhum dado XML recebido", 400


    @app.route('/consulta-envio', methods=['POST'])
    def consulta_envio():
        user = request.headers.get('user')
        pw = request.headers.get('password')
        event = request.headers.get('evento')
        empregador_cnpj = request.headers.get('nrInsc')
        protocoloEnvio = request.headers.get('protocoloEnvio')


        consultaDoRecibo = respostaAoEnvio.ConsultaRespostaEnvioLote()
        resultadoConsutlaLoteesocial_consulta_lote_api_processamento, esocial_consulta_lote_api_recibo = consultaDoRecibo.consultaReciboLote(protocoloEnvio, empregador_cnpj)

        return jsonify({'resultadoConsutlaLoteesocial_consulta_lote_api_processamento': resultadoConsutlaLoteesocial_consulta_lote_api_processamento, 'esocial_consulta_lote_api_recibo': esocial_consulta_lote_api_recibo }), 200
