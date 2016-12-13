#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from json import json

def test_json_basestring():
    assert_equals(json("Hello World"), '"Hello World"')

def test_json_integer():
    assert_equals(json(9), "9")

def test_json_float():
    assert_equals(json(1.234), "1.234")
    
def test_json_array():
    data = [1, 2, 3]
    assert_equals(json(data), '[1,2,3]')

def test_json_array02():
    data = ['bla', 1, 1.2]
    assert_equals(json(data), '["bla",1,1.2]')

def test_json_dict():
    data = { 'foo': 'bar' }
    assert_equals(json(data), '{"foo":"bar"}')
    
def test_json_dict_list():
    data = { 'foo': [1, 2, 3] }
    assert_equals(json(data), '{"foo":[1,2,3]}')
    
def test_json_dict_int_key():
    data = {1:[1, 2, 3] }
    assert_equals(json(data), '{"1":[1,2,3]}')
 
def test_json_dictindict():
    data = { 'foo': {'fizz' : 'buzz'} }
    assert_equals(json(data), '{"foo":{"fizz":"buzz"}}')

def test_json_2_dict():
    data = { 'foo': 'fizz', 'bar' : 'buzz'}
    assert_equals(json(data), '{"bar":"buzz","foo":"fizz"}')

def test_json_2_dict_2():
    data = { 'foo': 'fizz', 'bar' : 'buzz', 'a': [1, 2, 3]}
    assert_equals(json(data), '{"a":[1,2,3],"bar":"buzz","foo":"fizz"}')

def test_empty_list():
    data = []
    assert_equals(json(data), "[]")
    
def test_empty_dict():
    data = {}
    assert_equals(json(data), "{}")
    
def test_list_with_empty_dict():
    data = [{}]
    assert_equals(json(data), "[{}]")
    
def test_rangie2():
    data = {"": 0}
    assert_equals(json(data), '{"":0}')
    
def test_none():
    assert_equals(json(None), "null")

def test_object():
    def closure():
        json(object())
    assert_raises(TypeError, closure)
    
def test_bool():
    assert_equals(json(True), 'true')
    
def test_object_in_array():
    def closure():
        json([object()])
    assert_raises(TypeError, closure)

def test_object_in_dict():
    def closure():
        json({'a': object()})
    assert_raises(TypeError, closure)
    
def test_object_class():
    def closure():
        json(object)
    assert_raises(TypeError, closure)

def test_escape():
    assert_equals(json('"') , '"\\""')
        
