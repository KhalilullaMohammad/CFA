from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(username,seconds):
    s=Serializer('*cd@htl',seconds)
    return s.dumps({'user':username}).decode('utf-8')
