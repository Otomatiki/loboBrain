# Tennis Court Lighting/Door - Home Assistant Integration

## Installation

**We recommend having a backup of your home assistant system before begining this process.**

### Install Studio Code Server in HA

1. Go to `http://homeassistant.local:8123/` to access Home Assistant Web UI.
2. Go to your Profile in Home Assistant and switch on **Advanced mode**
   ![image](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/ea8b1ee8-2877-4e0f-b21c-dac8935d5c30)

3. Go to **Settings->Add-ons->ADD-ON STORE**.
4. Search for **Studio Code Server** and click **Studio Code Server Add-on** in search results.
   ![image](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/3f286e82-816f-4dbf-b36c-a76ba7d19e58)
   
5. Click **Install**. Do not leave this page until installation is completed. 
   ![image](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/d8844568-0421-4e53-a79e-88289244a0f8)

6. Enable **Start on boot** and **Show in sidebar**. Do not start the Add-on now.
   ![tempsnip](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/36c2a8f6-a903-4236-89c1-46bdcb87305e)

7. Next, Go to **Settings->Menu->Restart Home Assistant**.
   ![tempsnip2](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/b5c36958-861d-4369-971e-d5f3967f2e4c)

8. Open **Advanced Options** and **Reboot system**.
    ![image](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/f4f88968-2b30-4565-83e9-d213dda2cf24)

9. Once Rebooted, click **Studio Code Server** from the left sidebar to open Visual Studio Code in Home Assistant. Visual Studio Code will be shown as follows:
    ![image](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/629ffdb6-5cc3-4e8b-9efa-223476b0b318)

### Add Local Add-on Files into HA

1. Download the source files from Git repository.
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/25674bae-d458-4a08-a86d-9bff4609179a)

2. Click **Studio Code Server** from the left sidebar to open Visual Studio Code in Home Assistant.
3. Then, click **File->Open Folder...**
   ![tempsnip3](https://github.com/jware-automation/tennis-court-home-assistant-integration/assets/83968050/3a22822c-5273-4cd1-b2e6-cc91b6d346f0)

4. Next, Click **addons** and press **Enter**.
   ![tempsnip1111](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/40f039ed-ab7e-4b92-b66e-e251e77869c4)

5. Copy the downloaded zip folder into **addons** folder. (You may drag and drop the file from your computer.)
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/28cc1d03-a8ef-4b61-8f31-52ffd76c8da5)

6. Open **Terminal**.
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/dc81c663-6629-4c41-a1cc-f657451b1874)

7. Run the following command in the terminal to extract the add-ons file.
   ```
   unzip club_dashboard_ha_add-ons-main.zip && mv club_dashboard_ha_add-ons-main/* ./ && rm -r club_dashboard_ha_add-ons-main
   ```

8. Place the Root CA, Certificate and Private Key files in `homeassistant_club_dashboard_api/cert/` directory. Drag and Drop files in HA Studio code is possible.

### Installing the add-on in HA

1. Open the Home Assistant frontend
2. Go to **Settings->Add-ons**
3. Click **ADD-ON STORE** in the bottom right corner.
4. On the top right overflow menu, click the **Check for updates** button
5. You should now see a new section at the top of the store called **Local add-ons** that lists two add-ons!
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/252d6a71-5677-4283-a483-5f89f5231bc0)

6. Click on **Homeassistant Sports Club Dashboard Add-On** and **Homeassistant Sports Club Dashboard API** add-ons and install both add-ons.
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/c4ba7ba0-4117-4fb3-9a10-c3a79c0f952b)

7. After installation, Open **Homeassistant Sports Club Dashboard API** and go to **Configuration** page of the Add-on.
   ![image](https://github.com/jware-automation/club_dashboard_ha_add-ons/assets/83968050/57f8099d-498c-4cde-a0d6-16ceadbd8796)

8. Fill the details accordingly and click **Save**. Then click **Restart**.
    - To abtain the ok_cloud_access_token, open the relevent club in admin.outomatiki.xyz and click get Token.
    - If there are no facilities in your club, use `0` as the facility ID.
    - If the club is NOT integrated to Syltek, use OK Cloud Club ID in the Club UUID field.
10. Go to **Homeassistant Sports Club Dashboard** add-on and **Start**.
11. Visit `http://homeassistant.local:8000/` and enjoy the new dashboard.
