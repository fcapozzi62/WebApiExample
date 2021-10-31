import flask
from flask import request, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
import sqlite3

app = flask.Flask(__name__)
auth = HTTPBasicAuth()
app.config["DEBUG"] = True

users = {
    "fabio": generate_password_hash("hello"),
    "massimo": generate_password_hash("bye")
}

apikey = {
    "fabio": "abcd1234ffgghh",
    "massimo": "12345abcdffaa"
}

remotes = [
    {
        "id": 1,
        "name": "remote_1",
        "parent_id": 1,
        "sn": 1250,
        "scpc_peer_id": -1,
        "did": 1,
        "network_id": 10,
        "model_type": "x7",
        "mgmt_ip_address": "10.10.11.36",
        "mgmt_subnet_mask": "10.10.11.0/24",
        "mgmt_gateway": "10.10.11.1",
        "lan_ip_address": "192.168.10.2",
        "lan_subnet_mask": "192.168.10.0/25",
        "user_password": "iDirect_remote_1",
        "admin_password": "Password",
        "os_password": "iDirect_0000!!",
        "modcod": "QPSK",
        "is_scpc": False,
        "active": True,
        "tcp_compression": False,
        "udp_hdr_compression": False,
        "link_encryption": True,
        "crtp": False,
        "antenna_tx_handshake": True,
        "is_mobile": False,
        "is_roaming": False,
        "rx_only": True,
        "rx_only_multicast": False,
        "local_telnet_only": True,
        "v_lan_tagging": False,
        "inroute_group_id": 5,
        "spreading_factor": -1,
        "payload_size": 16830,
        "rx_only_mc_timeout": 200,
        "rx_carrier_id": 2,
        "tx_carrier_id":1,
        "lat": 41.1256,
        "lon": 12.542,
        "up_cir": 512,
        "up_mir": 2048,
        "up_min": 2,
        "down_cir": 1024,
        "down_mir": 4096,
        "down_min": 2,
        "symbol_rate": 256,
        "initial_power": -25,
        "max_power": -5,
        "_1_db": 5,
        "pool_license": "pool_1",
    }
]


carriers = [
    {
        "id": 21,
        "name": "trasponder_1",
        "parent_id": 11,
        "spacecraft_id": 122,
        "trasponder_id": 1026,
        "bandwidth_id": 33,
        "type": "typeA",
        "inbound_mode": "12A2",
        "spreading_factor": "2",
        "fec_rate": "3/4",
        "modulation_type": "F3A",
        "min_modcod": "A2",
        "max_modcod": "B4",
        "uplink_freq": 1531.234e6,
        "downlink_freq": 10344.500e6,
        "power": 50.3,
        "symbol_rate": 27500.0,
        "carrier_spacing": 10e6,
        "superburst": True,
        "spread_acq_enabled": False
    },
    {
        "id": 36,
        "name": "trasponder_2",
        "parent_id": 10,
        "spacecraft_id": 233,
        "trasponder_id": 2055,
        "bandwidth_id": 12,
        "type": "typeG",
        "inbound_mode": "12A6",
        "spreading_factor": "4",
        "fec_rate": "5/6",
        "modulation_type": "F2J",
        "min_modcod": "A9",
        "max_modcod": "B7",
        "uplink_freq": 2433.500e6,
        "downlink_freq": 11233.500e6,
        "power": 10.4,
        "symbol_rate": 29950.0,
        "carrier_spacing": 8e6,
        "superburst": False,
        "spread_acq_enabled": False
    }
]


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users.get(username),password):
        return username

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
@auth.login_required
def home():
    message = "<h1>iVantage API server Stub</h1><p>This program emulate iVantage API server answers </p> \
            Hello, {}!".format(auth.current_user())
    resp = make_response(message)
    resp.set_cookie('Session', apikey.get(auth.current_user()))
    return resp


@app.route('/carrierCarrierGet/', methods=['GET'])
@auth.login_required
def carrierCarrierGet():
    key = request.cookies.get("Session")
    usr = auth.current_user()
    lkey = apikey.get(usr)
    if key == lkey :
        if 'carrier_id' in flask.request.args:
            carrier_id = int(flask.request.args['carrier_id'])
        results = []
        for carrier in carriers :
            if carrier['id'] == carrier_id:
                results.append(carrier)
    else :
        results = "401 Not Authorized"
    return flask.jsonify(results)


@app.route('/carrierCarrierGet1/',methods=['GET'])
@auth.login_required()
def carrierCarrierGet1():
    key = request.cookies.get("Session")
    usr = auth.current_user()
    lkey = apikey.get(usr)
    if key == lkey :
        if 'carrier_id' in flask.request.args:
            carrier_id = int(flask.request.args['carrier_id'])
        results = []
        conn = sqlite3.connect('./ivantage.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        query = 'SELECT * FROM carriers WHERE carriers.id = ' + str(carrier_id) + ";"
        carrier = cur.execute(query).fetchall()
        results.append(carrier)
    else:
        results = '401 Not Authorized'
    return flask.jsonify(results)

@app.route('/remoteRemoteIdGet/', methods=['GET'])
@auth.login_required
def remoteRemoteIdGet():
    key = request.cookies.get("Session")
    usr = auth.current_user()
    lkey = apikey.get(usr)
    if key == lkey :
        if 'remote_id' in flask.request.args:
            remote_id = int(flask.request.args['remote_id'])
        results = []
        for remote in remotes:
            if remote['id'] == remote_id:
                results.append(remote)
    else:
        results = "401 Not Authorized"
    return flask.jsonify(results)


@app.route('/applicationservicegroupGet',methods=['GET'])
@auth.login_required
def applicationservicegroupGet():
    key = request.cookies.get("Session")
    usr = auth.current_user()
    lkey = apikey.get(usr)
    if lkey == key:
        res = {'id': 34,
            'parent_id': 11,
            'name': 'satlink_a',
            'parent_name': 'satlink',
            'qos_mode': 'enabled',
            'qos_mode_type': 'adaptive',
            'downstream': True}
    else :
        res = "401 Authentication Error"
    return flask.jsonify(res)

@app.route('/get-cookie/')
def get_cookie():
    cookie = "Cookie = {}".format(request.cookies.get('Session'))
    return cookie

@app.route('/logout/')
@auth.login_required
def logout():
    resp = make_response(redirect('http://log:out@localhost:5010/loggedout'))
    resp.set_cookie('Session', "none")
    return resp

@app.route('/loggedout')
def loggedout():
    message = "User logged out !!"
    return message


# with the host declaration it is possible to connect from any interface
app.run(host='0.0.0.0', port=5010)