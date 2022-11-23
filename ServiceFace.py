from wsse_signature import MemorySignature
import base64
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import requests
import subprocess
from zeep import Client
import zeep
import os
import sys
from zeep.transports import Transport
import logging 
from json2xml import json2xml
from json2xml.utils import readfromstring
import calendar
import time
ALMACEN = 'certificados/'
FILES = 'tempfiles/'
WSDLFILE = "face.wsdl"
MIME = 'application/xml'
PASSWORD = '//mastes7s'

class ServiceFace:
    def getMemorySignature(self):
        #CARGAMOS CERTIFICADO Y CLAVE PRIVADA
        #EL CERTIFICADO LO HACEMOS CON EL PFX DESDE EL KEYSTORE Y LO GENERAMOS
        with open(ALMACEN + 'cert2.cer', "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read(), backend=default_backend())
        with open(ALMACEN + 'clis.key', "rb") as f:
            key = serialization.load_pem_private_key(
                f.read(), None, backend=default_backend()
            )
        memory = MemorySignature(
            cert,
            key,
            cert,
        )

        return memory

    def getInvoiceSigned(self, pCert, pAlias, pFileContent):

        try:
            gmT = time.gmtime()
            ts = calendar.timegm(gmT)
            xmlFileName = str(ts)
            pfxFile = ALMACEN + pCert + ".pfx"
            xmlFileIn = FILES + xmlFileName + "_input.xml"
            xmlFileOut = FILES + xmlFileName + "_output.xml"
            

    # Generamos fichero xml base con el contenido recibido en formato json
            data = readfromstring(pFileContent)
            facturae = 'fe:Facturae xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:fe="http://www.facturae.es/Facturae/2009/v3.2/Facturae"'
            xmlString = json2xml.Json2xml(data, item_wrap=False, wrapper="Facturae", pretty=True, attr_type=False).to_xml()
            xmlDef = xmlString.replace("Facturae", "fe:Facturae")
            xmlDef2 = xmlDef.replace("fe:Facturae", facturae, 1)
            baseFile = open(xmlFileIn,'w')
            baseFile.write(xmlDef2)
            baseFile.close()

            # Borramos ficheros viejunos
            now = time.time()
            fLockTo = float('21600') # 6 horas
            antiguedad = now - (fLockTo)
            files = os.listdir(FILES)
            for xfile in files:
                fullXfile = FILES + xfile
                if os.path.isfile( fullXfile ):
                    t = os.stat( fullXfile )
                    c = t.st_ctime
                    if c < antiguedad:
                        try:
                            os.remove(fullXfile)
                        except Exception as e:
                            pass

            # Firma del XML
            arg0 = 'sign'
            arg1 = '-i'
            arg2 = xmlFileIn
            arg3 = '-o'
            arg4 = xmlFileOut
            arg5 = '-format'
            arg6 = 'facturae'
            arg7 = '-store'
            arg8 = 'pkcs12:' + pfxFile
            arg9 = '-password'
            arg10 = PASSWORD
            arg11 = '-alias'
            arg12 = pAlias
            arg13 = '-xml'
            subprocess.call(['java', '-jar', 'autofirma.jar', arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13])

            #DEVUELVO EL FICHERO
            return xmlFileOut
        except Exception as e:
            print("EXCEPCION1: " , e)
            print("mal")

    def sendInvoice(self, xmlFile, mail):
        try:
            fic = open(xmlFile, "r")
            file = fic.read()

            client = ServiceFace().getClient()
            invoice_file = client.get_type("ns0:FacturaFile")(
                base64.b64encode(file.encode("UTF-8")),
                os.path.basename(xmlFile),
                MIME,
            )
            invoice_call = client.get_type("ns0:EnviarFacturaRequest")(
                mail, invoice_file
            )

            response = client.service.enviarFactura(invoice_call)

            return response
        except Exception as e:
            return e

    def getClient(self):
        client = Client(WSDLFILE,  wsse=ServiceFace().getMemorySignature())
        return client

    def anularFactura(self, numReg, motive):
        try:
            response = ServiceFace().getClient().service.anularFactura(numReg, motive)
            return response
        except Exception as e:
            return e

    def getStatus(self, numReg):
        try:
            print('ver estado')
            response = ServiceFace().getClient().service.consultarFactura(numReg)
            return response
        except Exception as e:
            return e