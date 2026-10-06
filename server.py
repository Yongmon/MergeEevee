from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import mimetypes

mimetypes.add_type("image/webp", ".webp")

server = ThreadingHTTPServer(
    ("localhost", 8000),
    SimpleHTTPRequestHandler
)

print("http://localhost:8000")
server.serve_forever()