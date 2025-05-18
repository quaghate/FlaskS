from flask import Flask, request, abort
from functools import wraps
from cryptography.fernet import Fernet
import hashlib

class FlaskS:
    def __init__(self, app=None):
        self._key = Fernet.generate_key()
        self._cipher_suite = Fernet(self._key)
        self.app = app
        if app is not None:
            self.init_app(app)

    @property
    def key(self):
        return self._key

    @property
    def cipher_suite(self):
        return self._cipher_suite

    def hash_do_pacote(self, data: bytes):
        return hashlib.sha256(data).hexdigest()

    def encrypt(self, content: str) -> bytes:
        return self.cipher_suite.encrypt(content.encode())

    def decrypt(self, content: bytes) -> str:
        return self.cipher_suite.decrypt(content).decode()

    def security_route(self, route, methods=['POST']):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                encrypted_data = request.headers.get('X-Encrypted-Data')
                if not encrypted_data:
                    abort(403, "Encrypted data missing")

                try:
                    decrypted = self.cipher_suite.decrypt(encrypted_data.encode())
                    # Validação extra poderia ficar aqui
                except Exception:
                    abort(403, "Failed to decrypt data")

                return func(*args, **kwargs)
            self.app.route(route, methods=methods)(wrapper)
            return wrapper
        return decorator

    def init_app(self, app):
        self.app = app