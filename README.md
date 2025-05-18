# FlaskS
## O que é?
FlaskS é uma biblioteca desenvolvida por mim, quaghate, enquanto estava entediado. Ela serve para propositos educativos, e não substitui o HTTPS. Sempre use ele caso queira fazer um projeto de produção.
Eu ainda não testei ele, então essa biblioteca não poderá estar funcional ou pode ter bugs. Por favor, mandem DM no reddit que eu já respondo e trabalho nas atualizações

---
## Como instalar?
Atualmente, só copiando e colando o arquivo. Se quizerem, eu posso subir para o PyPI.

---
## Como posso te ajudar?
Se quizer ser meu colaborador, a melhor forma é você contribuir com pull requests. Se contribuir com muitas, posso te tornar um colaborador, mas não tenho regra fixa contra isso.
Por enquanto não tem mecanismos para me apoiar financeiramente. Depois posso criar um.

## Como usar?
Se você não tiver a lib no mesmo arquivo que o seu projeto, vai precisar de um `import FlaskS`, senão só seguir este código:
```python

app = Flask(__name__) # Instancia o Flask
secure = FlaskS(app) # O FlaskS precisa da instancia do Flask para funcionar.

@secure.security_route # depois é só colocar isso que ele faz a rota criptografada automáticamente.
def rota_segura():
    return jsonify({"mensagem": "Essa rota foi acessada com segurança!"})

if __name__ == '__main__':
    app.run()

```

Para descriptografar dados com a mesma criptografia, use `secure.decrypt(criptografada)`, uma observação muito importante é que ele vai usar a mesma chave para a descriptografia.

---

## Notas do autor.
Esse projeto é basico e só serve para fins educativos. Sempre prefira HTTPS ao invés da minha lib. Do resto, espero que tentem explodir a minha biblioteca (E me contem depois o que causou isso).
