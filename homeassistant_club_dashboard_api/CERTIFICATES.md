# Certificate files for Homeassistant Sports Club Dashboard API

Do not store real certificate files in this repository if the repository is public.

**As of 2026-09-14:** `run.sh` fetches these automatically from the backend
(`GET /api/homeassistant/certificates`, authenticated with the add-on's own
`ok_cloud_access_token`) at startup if they're missing, so manual upload is
no longer the normal path. This is a stop-gap for the current v1.0 fleet
only, since every club currently shares the same certificate -- see ADR-017
in `srlobo-2.0` for the v2.0 replacement (per-installation credentials via
`automation_bridge`'s bootstrap, no shared secret).

If the automatic fetch fails (backend unreachable, endpoint misconfigured),
place the required files manually in Home Assistant here:

```text
/ssl/lobobrain/cert/
```

Required filenames:

```text
AmazonRootCA1.pem
e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-certificate.pem.crt
e85bd3ae03a42f7c060129714775af0c8a2e9d3aa57f42a3e3ece6738b4be4e9-private.pem.key
```

Inside the add-on container, the folder is mounted as:

```text
/ssl/lobobrain/cert/
```

At startup, `run.sh` creates a symlink from `/cert` to `/ssl/lobobrain/cert` so the existing Python code can continue using the current `/cert/...` paths.

If any file is still missing after the automatic fetch, the add-on stops with a clear error in the logs.
