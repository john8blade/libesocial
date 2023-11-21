import esocial.xml
import esocial.utils

cert_data = esocial.utils.pkcs12_data('HT.pfx', 'ht380801')
evt2220 = esocial.xml.load_fromfile('S-2220-v2.5.0-not_signed.xml')

# Assina o XML com os algoritmos descritos na documentação do eSocial
evt2220_signed = esocial.xml.sign(evt2220, cert_data)