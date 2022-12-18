# helfffen
HelFFFen allows you to show people how they can help your organisation and let them contact you.

# Features
- Tasks overview 📝
- Tasks disappear when maximum needed helpers have applied or expiration date is hit 👻
- Contact person shown to applicant after applying to a task ☎️
- Overview of all potential helpers in the admin area, filterable by task 🧭

# Deploy using container image 🚢
Two types of container images are built automatically from this repository.
1. Each release is built and tagged with its version when it is released.
    - These are the most stable but if they are older than one month you should consider using the next type, which always contains the latest security fixes.
2. Every time `main` is updated, an image is built and tagged `latest`.
    - Additionally, the image tagged `latest` is rebuilt once a week to incorporate the latest updates from the base image.

You need to provide a PostgreSQL database connection and other information using the environment variables described in [`src/example.env`](./src/example.env).

You can deploy this image anywhere OCI container images are supported using Kubernetes, Docker Swarm or any other tool of your choosing.

## Instantly run a local demo
Instantly run a local instance of `helfffen` using `podman`, `docker` or any other container engine.

First, start the container.
```bash
docker run --rm -e HELFFFEN_USE_SQLITE=True -e HELFFFEN_ALLOWED_HOSTS=localhost -e HELFFFEN_CSRF_TRUSTED_ORIGINS=http://localhost:8082 -v helfffen-db:/app/src/persistent_db --name helfffen-localhost -p 8082:80 ghcr.io/wolfskaempf/helfffen:latest
```

Then, in a separate shell window you'll need to run database migrations to initialise the SQLite database and create an administrative account by running the following command.

```bash
docker exec -i -t helfffen-localhost /bin/sh -c "python manage.py migrate && python manage.py createsuperuser"
```

# Deploy using Caprover
[Caprover](https://caprover.com/) is a tool that turns your personal VPS into a Platform as a Service comparable to [dokku](https://dokku.com/) or Heroku.

1. [Get started with Caprover on your VPS and your CLI](https://caprover.com/docs/get-started.html)
2. Create a One-Click-Postgres app and remember the data you chose (app name, default database, user and password).
3. Create a new app named anything you like in the Caprover interface. This tutorial will go with `helfen` for the app name.
4. Inside the `HTTP Settings` section of the new app enable HTTPS and select `Force HTTPS by redirecting all HTTP traffic to HTTPS`
5. Inside the `App Configs` section of the new app configure the app specific environment variables described in [src/example.env](./src/example.env)
  - Ensure you have added all environment variables that start with `HELFFFEN` (do not copy the `POSTGRES` variables into the `App Configs` section of the `helfen` app)
  - Ensure the database connection information matches the database you created earlier
    - The `HELFFFEN_POSTGRES_HOST` can be found in the app overview of the database you created earlier
    - It should look something like this `srv-captain--helfffen-db` where `helfffen-db` is the name you selected for your database
    - Ensure you include only the hostname and no protocol (such as https://) in `HELFFFEN_POSTGRES_HOST`
6. On your local machine run `git clone https://github.com/wolfskaempf/helfffen.git && cd helfffen` to clone this repository and change directory into it.
7. Run `npx caprover deploy` and select your server and the app you just created
   * If this command doesn't exist, make sure that you followed [Step 3 of Getting Started with Caprover](https://caprover.com/docs/get-started.html#step-3-install-caprover-cli)
