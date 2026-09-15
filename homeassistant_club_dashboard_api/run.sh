#!/usr/bin/with-contenv bashio

echo "Hello world!"
cat /etc/os-release 

UUID="$(bashio::config 'club_uuid')"
echo "$(bashio::config 'club_uuid')"

club_name="$(bashio::config 'club_name')"
echo "$(bashio::config 'club_name')"

ha_token="$(bashio::config 'home_assistant_access_token')"
# Removed 2026-09-11: was `echo "$(bashio::config 'home_assistant_access_token')"` -- printed the secret in plaintext to the add-on log

mqtt_broker="$(bashio::config 'mqtt_broker')"
echo "$(bashio::config 'mqtt_broker')"

mqtt_port="$(bashio::config 'mqtt_port')"
echo "$(bashio::config 'mqtt_port')"

club_id="$(bashio::config 'club_id')"
echo "$(bashio::config 'club_id')"

back_end_url="$(bashio::config 'back_end_url')"
echo "$(bashio::config 'back_end_url')"

ok_cloud_access_token="$(bashio::config 'ok_cloud_access_token')"
# Removed 2026-09-11: was `echo "$(bashio::config 'ok_cloud_access_token')"` -- printed the secret in plaintext to the add-on log

facility_id="$(bashio::config 'facility_id')"
echo "$(bashio::config 'facility_id')"

integrated_club="$(bashio::config 'integrated_club')"
echo "$(bashio::config 'integrated_club')"

integrated_club_mode="$(bashio::config 'integrated_club_mode')"
echo "$(bashio::config 'integrated_club_mode')"

# mqtt_user_name="$(bashio::config 'mqtt_user_name')"
# echo "$(bashio::config 'mqtt_user_name')"

# mqtt_user_password="$(bashio::config 'mqtt_user_password')"
# echo "$(bashio::config 'mqtt_user_password')"

ls
cd /
ls
cd /homeassistant_club_dashboard_api
ls
cd /
pip3 --version



# Certificates are NOT bundled in the public repository.
# They live in the stable Home Assistant SSL folder:
#   /ssl/lobobrain/cert/   (from Home Assistant / Studio Code Server)
# Inside the add-on container this folder is available as:
#   /ssl/lobobrain/cert/
# The existing Python code expects /cert, so we create a runtime symlink.
CERT_DIR="/ssl/lobobrain/cert"
LEGACY_CERT_DIR="/cert"

mkdir -p "$CERT_DIR"
rm -rf "$LEGACY_CERT_DIR"
ln -s "$CERT_DIR" "$LEGACY_CERT_DIR"

# Added 2026-09-14: if any certificate file is missing, fetch the bundle
# from the backend instead of requiring a manual upload per installation.
# Stop-gap for the current v1.0 fleet only (all clubs share one cert) --
# see ADR-017 in srlobo-2.0 for the v2.0 replacement (per-installation
# credentials, no shared secret). No curl in this image, so this uses the
# python3 + requests that are already installed for the add-on itself.
python3 - "$CERT_DIR" "$back_end_url" "$ok_cloud_access_token" <<'PYEOF'
import sys, os, requests

cert_dir, back_end_url, token = sys.argv[1], sys.argv[2], sys.argv[3]
required = {
    "root_ca": "AmazonRootCA1.pem",
    "certificate": "e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-certificate.pem.crt",
    "private_key": "e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-private.pem.key",
}

missing = [name for name in required.values() if not os.path.exists(f"{cert_dir}/{name}")]
if not missing:
    print("Certificates already present, nothing to fetch.")
    sys.exit(0)

print(f"Missing {len(missing)} certificate file(s), fetching from backend...")
try:
    url = back_end_url.rstrip("/") + "/api/homeassistant/certificates"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=(3, 10),
    )
    if response.status_code != 200:
        print(f"ERROR: backend returned {response.status_code} fetching certificates: {response.text}")
        sys.exit(1)
    data = response.json()
    for key, filename in required.items():
        with open(f"{cert_dir}/{filename}", "w") as f:
            f.write(data[key])
    print("Certificates fetched and saved successfully.")
except Exception as e:
    print(f"ERROR: could not fetch certificates from backend: {e}")
    sys.exit(1)
PYEOF

for required_file in \
  "AmazonRootCA1.pem" \
  "e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-certificate.pem.crt" \
  "e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-private.pem.key"
do
  if [ ! -f "$CERT_DIR/$required_file" ]; then
    echo "ERROR: Missing certificate file: $CERT_DIR/$required_file"
    echo "Automatic fetch from the backend failed or was incomplete -- see the log above for the reason. As a fallback, upload the required AWS IoT certificate files to /ssl/lobobrain/cert/ manually and restart the add-on."
    exit 1
  fi
done

CONFIG_PATH=/data/options.json
python3 -m homeassistant_club_dashboard_api ${UUID} ${ha_token} ${mqtt_broker} ${mqtt_port} "${club_name}" ${ok_cloud_access_token} ${back_end_url} ${club_id} ${facility_id} ${integrated_club} ${integrated_club_mode} 
# ${mqtt_user_name} ${mqtt_user_password}
# python3 -m http.server 5000
