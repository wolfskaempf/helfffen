# helfffen
HelFFFen allows you to show people how they can help your organisation and let them contact you.

# Features
- Tasks overview 📝
- Tasks disappear when maximum needed helpers have applied or expiration date is hit 👻
- Contact person shown to applicant after applying to a task ☎️
- Overview of all potential helpers in the admin area, filterable by task 🧭

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
7. On your local machine run `git clone https://github.com/wolfskaempf/helfffen.git && cd helfffen` to clone this repository and change directory into it.
8. Run `npx caprover deploy` and select your server and the app you just created
   * If this command doesn't exist, make sure that you followed [Step 3 of Getting Started with Caprover](https://caprover.com/docs/get-started.html#step-3-install-caprover-cli)
