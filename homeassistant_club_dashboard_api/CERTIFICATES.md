# Certificate files for Homeassistant Sports Club Dashboard API

Do not store real certificate files in this repository if the repository is public.

Place the required files manually in Home Assistant here:

```text
/addon_configs/homeassistant_club_dashboard_api/cert/
```

Required filenames:

```text
AmazonRootCA1.pem
e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-certificate.pem.crt
e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-private.pem.key
```

Inside the add-on container, Home Assistant mounts that folder as:

```text
/addon_config/cert/
```

At startup, `run.sh` creates a symlink from `/cert` to `/addon_config/cert` so the existing Python code can continue using the current `/cert/...` paths.

If any file is missing, the add-on stops with a clear error in the logs.
