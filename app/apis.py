#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app
from flask import jsonify, abort, make_response

persons = [
    {
        'id': 1,
        'name': 'zhang',
        'age': 12
    },
    {
        'id': 2,
        'name': 'wang',
        'age': 23
    }
]


@app.route('/api/v1/persons', methods=['GET'])
def getPersons():
    return jsonify({'persons': persons})


@app.route('/api/v1/persons/<int:person_id>', methods=['GET'])
def getPersonById(person_id):
    person = list(filter(lambda p : p['id']==person_id, persons))
    if len(person) == 0:
        abort(404)
    return jsonify({'person': person[0]})
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)