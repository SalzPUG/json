#!/usr/bin/env python
# -*- coding: utf-8 -*-

def scalar_to_json(data):
    if data is None:
        return "null"
    if isinstance(data, bool):
        if data:
            return 'true'
        return 'false'
    if isinstance(data, basestring):
        return '"{}"'.format(data.replace('"', '\\"'))
    return str(data)


def json(data):
    output = None
    if isinstance(data, dict):
        temp = ['"{}":{}'.format(k, json(v)) for k, v in sorted(data.items())]
        output = ','.join(temp)
        output = '{{{}}}'.format(output)
    elif isinstance(data, list):
        temp = [json(item) for item in data]            
        output = ','.join(temp)
        output = '[{}]'.format(output)
    elif isinstance(data, (int, float, basestring, type(None), bool)):
        output = scalar_to_json(data)
    if output is None:
        raise TypeError, "cannot convert this shit"
    return output


if __name__ == "__main__":
    import nose
    nose.main()
