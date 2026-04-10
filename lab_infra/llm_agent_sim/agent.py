from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

# Vulnerability: Agentic Exploitation via Prompt Injection
# Simulating a future Zero-Day (2026+) where LLMs have shell/system tool access.
@app.route('/')
def index():
    return "<h1>AI Support Agent (Beta)</h1><p>I can help you check system status. Send queries to /ask?query=...</p>"

@app.route('/ask')
def ask_agent():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"agent": "How can I help?"})

    # The AI agent's internal thought process is simulated here.
    # It parses natural language but is susceptible to prompt injection.
    
    # 1. Benign intent check (Simulating weak LLM Guardrails)
    if "sudo" in query or "rm -rf" in query:
        return jsonify({"agent": "I'm sorry, I cannot perform destructive actions."})

    # 2. Agent Execution Layer (The flaw)
    # The agent has a 'tool' to ping servers, but attackers can inject shell operators like ';'
    if "ping" in query.lower():
        # Extracted target from prompt (simulated weak extraction)
        target = re.search(r'ping (.*)', query.lower())
        if target:
            host = target.group(1).split()[0]
            # Danger: Concatenating AI-extracted intent directly into a shell command
            try:
                cmd = f"ping -c 1 {host}"
                output = subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)
                return jsonify({"agent": f"System replied:\n{output}"})
            except subprocess.CalledProcessError as e:
                return jsonify({"agent": f"Failed: {e.output}"})

    return jsonify({"agent": "I didn't understand the request. Try asking me to ping a server."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
