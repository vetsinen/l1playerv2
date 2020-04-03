import hashlib

def file_hash(file):
    def file_as_bytes(file):
        with file:
            return file.read()
    return hashlib.md5(file_as_bytes(open(file, 'rb'))).hexdigest()

#print(file_hash('static/mp3/bacha-v4-excuse me-perdoname.mp3'))
