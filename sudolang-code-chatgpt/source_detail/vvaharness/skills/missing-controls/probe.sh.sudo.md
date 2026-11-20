# vvaharness/skills/missing-controls/probe.sh

Role: optional executable shell script; not assumed invoked.

Exact source asset: `assets/original/vvaharness/skills/missing-controls/probe.sh`. SHA-256 `382050e785cc2ad07bc9e09b4ce65eb31846f4aa2aecdce59067d3bec5632eb9`.

```sudo
// Source: vvaharness/skills/missing-controls/probe.sh:1-163
fn source_shell_procedure(arguments, environment) {
  Interpret the exact source asset using its declared shell, preserving argument expansion,
    command substitutions, pipeline/status rules, redirects, function scopes and command order.
  Use the helper/gate/cap descriptions in representation/shell-probes.sudo.md.
  The ordered source-command appendix below retains every pattern, include/exclude flag,
    conditional and cutoff; it is the detailed procedure, not a claim this tool was invoked.
}
```

## Ordered source-command evidence

These exact shell fragments disambiguate lexical/regex details; they are inert evidence.

Source: `vvaharness/skills/missing-controls/probe.sh:1-3`

````sh
#!/bin/sh
# Absent-control probe: enumerates every site a control belongs (routes, cookie writes, storage,
# config) and every place the control is actually present, so absence can be proven per site.
````

Source: `vvaharness/skills/missing-controls/probe.sh:5-17`

````sh
# Copyright 2026 Visa, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
````

Source: `vvaharness/skills/missing-controls/probe.sh:19-27`

````sh
set -f
ROOT=${1:-.}
CAP=${MC_PROBE_CAP:-12}
WIDTH=140
EX="--exclude-dir=.git --exclude-dir=node_modules --exclude-dir=.venv --exclude-dir=venv
--exclude-dir=.tox --exclude-dir=dist --exclude-dir=build --exclude-dir=__pycache__
--exclude-dir=site-packages --exclude-dir=.mypy_cache --exclude-dir=target
--exclude-dir=.next --exclude-dir=coverage
--exclude-dir=.vvaharness --exclude-dir=security-scan --exclude=SKILL.md --exclude=probe.sh"
````

Source: `vvaharness/skills/missing-controls/probe.sh:29-46`

````sh
# scan LABEL "INCLUDE_GLOBS" "ERE" — capped path:line hits, or (none).
scan() {
	_label=$1
	_globs=$2
	_pat=$3
	_inc=
	for _g in $_globs; do _inc="$_inc --include=$_g"; done
	echo "== $_label =="
	_out=$(grep -rEn --binary-files=without-match $_inc $EX -- "$_pat" "$ROOT" 2>/dev/null || true)
	if [ -z "$_out" ]; then
		echo "(none)"
	else
		_n=$(printf '%s\n' "$_out" | wc -l | tr -d ' ')
		printf '%s\n' "$_out" | head -n "$CAP" | cut -c1-$WIDTH
		[ "$_n" -gt "$CAP" ] && echo "... $_n hits total, showing $CAP - grep this pattern yourself for the rest"
	fi
	echo ""
}
````

Source: `vvaharness/skills/missing-controls/probe.sh:48-67`

````sh
# scan2 LABEL "INCLUDE_GLOBS" "ERE" "ERE2" — hits matching both patterns (site AND keyword).
scan2() {
	_label=$1
	_globs=$2
	_pat=$3
	_pat2=$4
	_inc=
	for _g in $_globs; do _inc="$_inc --include=$_g"; done
	echo "== $_label =="
	_out=$(grep -rEn --binary-files=without-match $_inc $EX -- "$_pat" "$ROOT" 2>/dev/null |
		grep -iE -- "$_pat2" || true)
	if [ -z "$_out" ]; then
		echo "(none)"
	else
		_n=$(printf '%s\n' "$_out" | wc -l | tr -d ' ')
		printf '%s\n' "$_out" | head -n "$CAP" | cut -c1-$WIDTH
		[ "$_n" -gt "$CAP" ] && echo "... $_n hits total, showing $CAP - grep this pattern yourself for the rest"
	fi
	echo ""
}
````

Source: `vvaharness/skills/missing-controls/probe.sh:69-86`

````sh
# files LABEL "INCLUDE_GLOBS" "ERE" — file names only (existence is the answer, not the lines).
files() {
	_label=$1
	_globs=$2
	_pat=$3
	_inc=
	for _g in $_globs; do _inc="$_inc --include=$_g"; done
	echo "== $_label =="
	_out=$(grep -rlE --binary-files=without-match $_inc $EX -- "$_pat" "$ROOT" 2>/dev/null || true)
	if [ -z "$_out" ]; then
		echo "(none)"
	else
		_n=$(printf '%s\n' "$_out" | wc -l | tr -d ' ')
		printf '%s\n' "$_out" | head -n 15
		[ "$_n" -gt 15 ] && echo "... $_n files total, showing 15"
	fi
	echo ""
}
````

Source: `vvaharness/skills/missing-controls/probe.sh:88-89`

````sh
ROUTE='@[a-zA-Z_.]*\.(route|get|post|put|patch|delete)\(|@(Get|Post|Put|Patch|Delete|Request)Mapping|(app|router|api|server)\.(get|post|put|patch|delete|all)\(|path\(|re_path\(|url\(|def (get|post|put|patch|delete)\(|\[Http(Get|Post|Put|Delete)\]'
SENSITIVE='ssn|social_security|national_id|tax_id|passport|dob|date_of_birth|birth|card_number|cardnum|pan\b|cvv|cvc|iban|routing|account_number|salary|income|health|diagnosis|medical|insurance|address|phone|mobile|email|api_key|apikey|secret|token|password|passwd|pin\b|license'
````

Source: `vvaharness/skills/missing-controls/probe.sh:91-92`

````sh
echo "### MISSING-CONTROLS PROBE root=$ROOT"
echo ""
````

Source: `vvaharness/skills/missing-controls/probe.sh:94-96`

````sh
CAP=15
echo "--- SITES: enumerate these, then judge each ---"
echo ""
````

Source: `vvaharness/skills/missing-controls/probe.sh:98-98`

````sh
scan "ALL ROUTE/HANDLER SITES (total count is your enumeration denominator)" "" "$ROUTE"
````

Source: `vvaharness/skills/missing-controls/probe.sh:100-101`

````sh
scan2 "CREDENTIAL AND COST ENDPOINTS (rate-limit sites)" "" "$ROUTE" \
	'login|signin|sign_in|logout|signout|register|signup|sign_up|password|reset|forgot|otp|mfa|2fa|verify|token|refresh|confirm|invite|upload|import|export|search|send|mail|sms|pay|charge|checkout|transfer|withdraw'
````

Source: `vvaharness/skills/missing-controls/probe.sh:103-104`

````sh
scan2 "STATE-CHANGING HANDLERS (CSRF / authz enumeration sites)" "" "$ROUTE" \
	'post|put|patch|delete|create|update|edit|save|add|remove|transfer|change|reset'
````

Source: `vvaharness/skills/missing-controls/probe.sh:106-107`

````sh
scan "COOKIE WRITE SITES (one finding per write; config default does not cover these)" "" \
	'set_cookie|Set-Cookie|res\.cookie|response\.cookies|addCookie|new Cookie\(|HttpCookie|cookies\.set|\.cookie\s*='
````

Source: `vvaharness/skills/missing-controls/probe.sh:109-110`

````sh
scan "SESSION AND TOKEN CONFIG SITES" "" \
	'SESSION_COOKIE_[A-Z]+|CSRF_COOKIE_[A-Z]+|REMEMBER_COOKIE_[A-Z]+|PERMANENT_SESSION_LIFETIME|SESSION_COOKIE_AGE|SESSION_EXPIRE|session\.permanent|JWT_|jwt\.(encode|sign)|expires_delta|exp[\"'\'']?\s*[:=]|maxAge|max_age|SECRET_KEY|secret\s*[:=]'
````

Source: `vvaharness/skills/missing-controls/probe.sh:112-114`

````sh
scan2 "STORAGE SITES HOLDING SENSITIVE FIELDS (cleartext-at-rest sites)" "" \
	'Column\(|db\.Column|models\.[A-Za-z]+Field\(|@Column|Schema\(|Field\(|CREATE TABLE|ALTER TABLE|ADD COLUMN|add_column|INSERT INTO' \
	"$SENSITIVE"
````

Source: `vvaharness/skills/missing-controls/probe.sh:116-118`

````sh
files "SEED / FIXTURE / SAMPLE DATA FILES (synthetic only refutes if never seeded)" \
	"*seed* *fixture* *sample* *demo* *.sql *.csv" \
	'INSERT INTO|password|api_key|secret|ssn|card|token'
````

Source: `vvaharness/skills/missing-controls/probe.sh:120-122`

````sh
files "CONFIG AND DEPLOYMENT FILES PRESENT (open these for posture)" \
	"Dockerfile* docker-compose* *.yml *.yaml *.ini *.cfg *.toml *.env* Procfile *.tf settings*.py config*.py" \
	'DEBUG|debug|host|HOST|port|PORT|ENV|environment|image:|command:'
````

Source: `vvaharness/skills/missing-controls/probe.sh:124-126`

````sh
CAP=6
echo "--- CONTROLS: where each is actually present ---"
echo ""
````

Source: `vvaharness/skills/missing-controls/probe.sh:128-129`

````sh
scan "RATE LIMIT / ANTI-AUTOMATION PRESENT" "" \
	'limiter|Limiter|@ratelimit|ratelimit|RateLimit|rate_limit|throttle|Throttle|slowapi|express-rate-limit|Bucket4j|resilience4j|captcha|recaptcha|hcaptcha|turnstile|failed_(attempt|count|login)s?|login_attempt|LoginAttempt|lockout|locked_until|backoff'
````

Source: `vvaharness/skills/missing-controls/probe.sh:131-132`

````sh
scan "AUTH / AUTHZ GUARDS PRESENT" "" \
	'login_required|@login|jwt_required|token_required|auth_required|requires_auth|requireAuth|isAuthenticated|IsAuthenticated|permission_classes|has_permission|@PreAuthorize|@Secured|@RolesAllowed|before_request|Depends\(|middleware\.[Aa]uth|passport\.|ensureLoggedIn|current_user|\[Authorize\]'
````

Source: `vvaharness/skills/missing-controls/probe.sh:134-135`

````sh
scan "SESSION TERMINATION / REVOCATION PRESENT" "" \
	'session\.(clear|flush|pop|destroy|invalidate)|logout_user|destroy_session|invalidateSession|revoke|revocation|jti|token_version|password_changed_at|denylist|blocklist|blacklist|deleted_tokens|refresh_token_rotation'
````

Source: `vvaharness/skills/missing-controls/probe.sh:137-138`

````sh
scan "COOKIE FLAGS AND TRANSPORT SECURITY PRESENT" "" \
	'httponly|HttpOnly|[Ss]ecure\s*[:=]|samesite|SameSite|SECURE_SSL_REDIRECT|SECURE_HSTS|Strict-Transport-Security|HSTS|force_https|SESSION_COOKIE_SECURE|PREFERRED_URL_SCHEME'
````

Source: `vvaharness/skills/missing-controls/probe.sh:140-141`

````sh
scan "CSRF PROTECTION PRESENT" "" \
	'CSRFProtect|CsrfViewMiddleware|csrf_token|csrf_exempt|WTF_CSRF|csurf|csrf-token|X-CSRF|XSRF|AntiForgery|@csrf'
````

Source: `vvaharness/skills/missing-controls/probe.sh:143-144`

````sh
scan "SECURITY HEADERS PRESENT" "" \
	'Content-Security-Policy|X-Frame-Options|X-Content-Type-Options|Referrer-Policy|Permissions-Policy|Talisman|helmet|frame_options|X-XSS-Protection'
````

Source: `vvaharness/skills/missing-controls/probe.sh:146-147`

````sh
scan "PASSWORD / FIELD ENCRYPTION PRIMITIVES PRESENT" "" \
	'bcrypt|argon2|pbkdf2|scrypt|generate_password_hash|check_password_hash|werkzeug\.security|passlib|PasswordEncoder|Fernet|AES|KMS|encrypt|EncryptedType|pgcrypto'
````

Source: `vvaharness/skills/missing-controls/probe.sh:149-151`

````sh
CAP=12
echo "--- POSTURE HOLES: these hits are usually findings on sight ---"
echo ""
````

Source: `vvaharness/skills/missing-controls/probe.sh:153-154`

````sh
scan "DEBUG / EXPOSURE POSTURE" "" \
	'debug\s*=\s*True|DEBUG\s*=\s*True|debug:\s*true|app\.run\(|ALLOWED_HOSTS\s*=|\*.{0,3}ALLOWED|host\s*=\s*.0\.0\.0\.0|--reload|FLASK_ENV|FLASK_DEBUG|NODE_ENV|display_errors|expose_php|printStackTrace|print_exc|traceback\.format_exc|autoreload|werkzeug'
````

Source: `vvaharness/skills/missing-controls/probe.sh:156-157`

````sh
scan "TLS VERIFICATION DISABLED" "" \
	'verify\s*=\s*False|verify_ssl\s*=\s*False|rejectUnauthorized\s*:\s*false|CURLOPT_SSL_VERIFY(PEER|HOST)\s*,\s*(0|false)|InsecureSkipVerify|_create_unverified|check_hostname\s*=\s*False|NODE_TLS_REJECT_UNAUTHORIZED|TrustAllCerts|ALLOW_ALL_HOSTNAME'
````

Source: `vvaharness/skills/missing-controls/probe.sh:159-160`

````sh
scan "WEAK HASH OR NO HASH ON CREDENTIALS" "" \
	'hashlib\.(md5|sha1)\(|MD5|SHA1|password\s*=\s*(request|req|\$_|body|data|params)|password\s*==\s*|plain_?password|raw_password'
````

Source: `vvaharness/skills/missing-controls/probe.sh:162-163`

````sh
echo "### END MISSING-CONTROLS PROBE"
exit 0
````

