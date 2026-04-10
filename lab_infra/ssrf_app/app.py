from flask import Flask, request
import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>VPN/Proxy Gateway</h1><p>Use /fetch?url=... to proxy requests.</p>"

# Vulnerability: Server-Side Request Forgery (SSRF)
# Simulates enterprise VPN/Gateway flaws (e.g., Ivanti, Citrix, ProxyNotShell)
@app.route('/fetch')
def fetch_url():
    target_url = request.args.get('url')
    if not target_url:
        return "Missing URL parameter.", 400

    # Weak blocklist (Bypassable)
    if "localhost" in target_url or "127.0.0.1" in target_url:
        return "Access denied: Localhost is forbidden.", 403

    try:
        # The server fetches the URL on behalf of the user
        # Attackers can bypass the filter using 'internal_admin_api' or '0.0.0.0'
        req = urllib.request.Request(target_url, headers=request.headers)
        response = urllib.request.urlopen(req, timeout=5)
        return response.read()
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
