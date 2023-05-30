# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Database

All instances of the app use Azure's CosmosDB, a [MongoDB](https://www.mongodb.com/)-compatible database.
## Running the App 

### Running locally

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Running in a Docker Container - Development

To create the image, run the command:
```
docker build --target development --tag todo-app:dev .
```

To run the container, run:
```
docker run --env-file ./.env --publish 8000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app -it todo-app:dev
```

Now visit [`http://localhost:8000/`](http://localhost:8000/) in your web browser to view the app.

### Running in a Docker Container - Production

To create the image, run the command:
```
docker build --target production --tag todo-app:prod .
```

To run the container, run:
```
docker run -p 8000:8000 --env-file ./.env -it todo-app:prod
```

Now visit [`http://localhost:8000/`](http://localhost:8000/) in your web browser to view the app.

### Running in a VM

To Provision a VM from an Ansible Control Node:

- SSH into the control node
- Run:
```
ansible-playbook my-ansible-playbook.yml -i my-ansible-inventory
```

- Visit `http://host.ip.address:5000/` in your browser to view the app


## Running the Tests

### Running locally

To run the tests (integration and unit), use the command 
```
poetry run pytest tests
``` 
in the DevOps-Course-Starter directory. This will search the "tests" directory for files starting in `test_` or ending in `_test`. Inside those files, any function starting with `test_` will be considered a test.

### Running in a Docker Container

To create the image, run the command:
```
docker build --target test --tag todo-app:test .
```

To run the tests, run:
```
docker run todo-app:test
```

### Running in a VM

To run the test suite in VS code, you need to set up the virtual environment. Press `Cmd/Ctrl + Shift + P` and select `Python: Select Interpreter`. Select the Python executable in the new `.venv` directory, which is `./.venv/Scripts/python.exe` on Windows.

## Dockerhub
### Push Docker image to Dockerhub

Login to DockerHub locally using:
```
docker login
```
Build the image using
```
docker build --target production --tag <image-tag> .
```
Push the image using
```
docker push <image-tag>
```
where `<image-tag>` has the format `<username>/<image_name>:<tag>`.

### Pull Docker image from Dockerhub

The production image is stored in Dockerhub [here](https://hub.docker.com/repository/docker/frasto/todo-app/general).
Run the following command to pull the image from Dockerhub:
```
docker pull frasto/todo-app:latest
```

## Hosting on Azure Web App

The app is hosted at [`http://frasto-todo-app.azurewebsites.net/`](http://frasto-todo-app.azurewebsites.net/)

### Updating the container

Post requests to the webhook URL set up by the Azure App Service will restart and pull the latest version of the container image from Dockerhub, to do this:
- Find the webhook URL in the Deployment Center in the Azure portal.
- Run the command `curl -dH -X POST "<webhook>"` escaping the dollar sign with a backslash, eg. `\$`