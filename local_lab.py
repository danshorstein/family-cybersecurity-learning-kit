#!/usr/bin/env python3
"""Fictional, localhost-only lab for Learner's weeks 5 and 7. No external services."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from threading import Lock
import json
import time

HOST = '127.0.0.1'
PORT = 8765
lock = Lock()
state = {'mode': 'vulnerable', 'balance': 10, 'events': []}
cases = {
    '101': {'owner': 'Agent A', 'title': 'Blue comet', 'note': 'The telescope needs a clean lens.'},
    '102': {'owner': 'Agent B', 'title': 'Red nebula', 'note': 'The chart contains a fictional secret: ORBIT-42.'},
}

PAGE = '''<!doctype html><html lang="en"><meta charset="utf-8"><title>Learner Lab</title>
<style>body{font:18px system-ui;max-width:800px;margin:2rem auto;padding:0 1rem;line-height:1.5}button{font:inherit;padding:.4rem .7rem;margin:.2rem}code,pre{background:#f1f1f1;padding:.3rem}pre{white-space:pre-wrap}section{border-top:1px solid #aaa;padding:1rem 0}</style>
<h1>Learner Lab</h1><p>Fictional data. This server listens only on this computer.</p>
<section><h2>Case file test</h2><p>You are Agent A. Open <a href="/case/101">case 101</a>. Then change the last number in the address to 102. Who decides whether you may read it?</p></section>
<section><h2>Double-spend test</h2><p>Balance: <strong id="balance"></strong> fictional tokens. Each spend costs 8.</p><button onclick="spend(false)">Spend once</button><button onclick="spend(true)">Spend twice together</button><button onclick="reset()">Reset balance</button>
<p id="result"></p></section>
<section><h2>Repair switch</h2><p>Current mode: <strong id="mode"></strong></p><button onclick="mode('vulnerable')">Vulnerable version</button><button onclick="mode('protected')">Protected version</button></section>
<section><h2>Event log</h2><pre id="events"></pre></section>
<script>
async function j(url,options){let r=await fetch(url,options);return r.json()}
async function refresh(){let s=await j('/api/state');document.getElementById('balance').textContent=s.balance;document.getElementById('mode').textContent=s.mode;document.getElementById('events').textContent=s.events.join('\\n')}
async function spend(twice){let n=twice?2:1;let a=await Promise.all(Array.from({length:n},()=>j('/api/spend',{method:'POST'})));document.getElementById('result').textContent=JSON.stringify(a);await refresh()}
async function reset(){await j('/api/reset',{method:'POST'});await refresh()}
async function mode(m){await j('/api/mode?value='+m,{method:'POST'});await refresh()}
refresh();
</script></html>'''

class Handler(BaseHTTPRequestHandler):
    def send_json(self, obj, status=200):
        data = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def send_html(self, html, status=200):
        data = html.encode()
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/':
            return self.send_html(PAGE)
        if path == '/api/state':
            with lock:
                return self.send_json(dict(state))
        if path.startswith('/case/'):
            ident = path.rsplit('/', 1)[-1]
            item = cases.get(ident)
            if not item:
                return self.send_html('<h1>Not found</h1>', 404)
            with lock:
                allowed = state['mode'] == 'vulnerable' or item['owner'] == 'Agent A'
                state['events'].append(f'Agent A requested case {ident}: {"allowed" if allowed else "denied"}')
            if not allowed:
                return self.send_html('<h1>Access denied</h1><p><a href="/">Home</a></p>', 403)
            return self.send_html(f'<h1>Case {ident}: {item["title"]}</h1><p>Owner: {item["owner"]}</p><p>{item["note"]}</p><p><a href="/">Home</a></p>')
        self.send_json({'error': 'not found'}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/mode':
            value = parse_qs(parsed.query).get('value', [''])[0]
            if value not in ('vulnerable', 'protected'):
                return self.send_json({'error': 'invalid mode'}, 400)
            with lock:
                state['mode'] = value
                state['events'].append(f'Mode changed to {value}')
            return self.send_json({'mode': value})
        if parsed.path == '/api/reset':
            with lock:
                state['balance'] = 10
                state['events'].append('Balance reset to 10')
            return self.send_json({'balance': 10})
        if parsed.path == '/api/spend':
            if state['mode'] == 'protected':
                with lock:
                    if state['balance'] < 8:
                        state['events'].append('Protected spend denied')
                        return self.send_json({'ok': False, 'balance': state['balance']})
                    state['balance'] -= 8
                    state['events'].append('Protected spend accepted')
                    return self.send_json({'ok': True, 'balance': state['balance']})
            old = state['balance']
            if old < 8:
                with lock:
                    state['events'].append('Vulnerable spend denied')
                return self.send_json({'ok': False, 'balance': old})
            time.sleep(0.5)  # educational pause between the check and update
            with lock:
                state['balance'] -= 8
                state['events'].append(f'Vulnerable spend accepted after reading {old}')
                now = state['balance']
            return self.send_json({'ok': True, 'balance': now})
        self.send_json({'error': 'not found'}, 404)

if __name__ == '__main__':
    print(f'Learner Lab: http://{HOST}:{PORT}/  (Ctrl+C to stop)', flush=True)
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
