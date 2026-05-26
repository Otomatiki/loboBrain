#!/usr/bin/with-contenv bashio

echo "Hello world!"
cat /etc/os-release 

UUID="$(bashio::config 'club_uuid')"
echo "$(bashio::config 'club_uuid')"

club_name="$(bashio::config 'club_name')"
echo "$(bashio::config 'club_name')"

ha_token="$(bashio::config 'home_assistant_access_token')"
echo "$(bashio::config 'home_assistant_access_token')"

mqtt_broker="$(bashio::config 'mqtt_broker')"
echo "$(bashio::config 'mqtt_broker')"

mqtt_port="$(bashio::config 'mqtt_port')"
echo "$(bashio::config 'mqtt_port')"

club_id="$(bashio::config 'club_id')"
echo "$(bashio::config 'club_id')"

back_end_url="$(bashio::config 'back_end_url')"
echo "$(bashio::config 'back_end_url')"

ok_cloud_access_token="$(bashio::config 'ok_cloud_access_token')"
echo "$(bashio::config 'ok_cloud_access_token')"

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


CONFIG_PATH=/data/options.json
python3 -m homeassistant_club_dashboard_api ${UUID} ${ha_token} ${mqtt_broker} ${mqtt_port} "${club_name}" ${ok_cloud_access_token} ${back_end_url} ${club_id} ${facility_id} ${integrated_club} ${integrated_club_mode} 
# ${mqtt_user_name} ${mqtt_user_password}
# python3 -m http.server 5000
