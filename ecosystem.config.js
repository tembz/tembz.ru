module.exports = {
  apps: [
    {
      name: "usercard",
      script: "venv/bin/gunicorn",
      args: "-c gunicorn.conf.py run:app",
      interpreter: "none",
      autorestart: true,
      watch: false,
    },
  ],
};
