from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints


class FormPage(Resource):
    def render_GET(self, request):
        return b"""\
            <!DOCTYPE html>
            <html>
            <head><meta charset="utf-8"></head>
            <body>
                <form method="post">
                    Nombre:<br>
                    <input type="text" name="name">
                    <br>
                    Email:<br>
                    <input type="text" name="email">
                    <br>
                    Mensaje:<br>
                    <textarea name="message"></textarea>
                    <br><br>
                    <input type="submit" value="Enviar">
                </form> 
            </body>
            </html>\
        """

    def render_POST(self, request):
        if all((request.args[f][0] for f in (b"name", b"email", b"message"))):
            output = "¡Mensaje enviado correctamente!"
        else:
            output = "Complete todos los campos."
        return """\
            <!DOCTYPE html>
            <html>
            <head><meta charset="utf-8"></head>
            <body>{}</body>
            </html>\
        """.format(output).encode("utf-8")


root = Resource()
root.putChild(b"form", FormPage())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()
