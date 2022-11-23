# -*- coding: utf-8 -*-
import multiprocessing
import logging
from flask import Flask
from flask import request
import json
from ServiceFace import *
from config import *
app = Flask(__name__)

def set_logger():
    gunicorn_logger = logging.getLogger('gunicorn.error')
    if gunicorn_logger is not None:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    logger = logging.getLogger()
    logger.setLevel(app.logger.level)
    logger.handlers = app.logger.handlers

def init_application():
    set_logger()

@app.route('/sign_send', methods=['POST'])
def sign_send():
    face = ServiceFace()
    peFac = ''
    incoming_json = request.get_json()
    params = incoming_json.get("params")

    for param in params:
        p_cert = param['cert']
        p_alias = param['alias']
        p_xml = param['file']
        try:
            fac = face.sendInvoice(
                face.getInvoiceSigned(p_cert, p_alias, p_xml), 
                'jdmelian@hospiten.es')
        except Exception as ex:
            logging.exception(str(ex))
            return str(ex), 500
    
    return fac, 200

@app.route('/get_status_group', methods=['POST'])
def get_status_group():
  
    face = ServiceFace()
    peFac = ''
    incoming_json = request.get_json()
    params = incoming_json.get("params")

    for param in params:
        p_cert = param['cert']
        p_idgr = param['idgr']
        try:
            peFac = face.getStatusGroup(p_cert, p_idgr)

        except Exception as ex:
            logging.exception(str(ex))
            return str(ex), 500
    
    response = { "fullresponse": peFac }  
    return json.dumps(response), 200

@app.route('/get_comprobante', methods=['POST'])
def get_comprobante():
  
    face = ServiceFace()
    peFac = ''
    incoming_json = request.get_json()
    params = incoming_json.get("params")

    for param in params:
        p_cert = param['cert']
        p_id = param['id']
        try:
            peFac = face.getComprobante(p_cert, p_id)

        except Exception as ex:
            logging.exception(str(ex))
            return str(ex), 500
    
    return peFac

@app.route('/set_anulada', methods=['POST'])
def set_anulada():
  
    face = ServiceFace()
    peFac = ''
    incoming_json = request.get_json()
    params = incoming_json.get("params")

    for param in params:
        p_cert = param['cert']
        p_id = param['id']
        p_motiv = param['motiv']
        try:
            peFac = face.setAnulada(p_cert, p_id, p_motiv)

        except Exception as ex:
            logging.exception(str(ex))
            return str(ex), 500
    
    return peFac, 200

if __name__ == '__main__':
    app.run(host=config.get_by_env(config.FLASK_CONFIG)['ip'],
            port=config.get_by_env(config.FLASK_CONFIG)['port'],
            debug=config.get_by_env(config.FLASK_CONFIG)['debug'])
    init_application()

if __name__ != '__main__':
    init_application()