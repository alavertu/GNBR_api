import os

from neo4j.v1 import GraphDatabase, basic_auth
from flask import abort

driver = None

def run(query, param={}):
    return get_session().run(query, param)

def get_session():
    global driver
    if driver is None:
        try:
            neo4j_auth = os.environ.get('NEO4J_AUTH')
            username, password = neo4j_auth.split('/', 1)
            driver = GraphDatabase.driver('bolt://db:7687', auth=basic_auth(username, password))
        except Exception as e:
            abort(500, e)
    return driver.session()

def close_session():
    get_session.close()
