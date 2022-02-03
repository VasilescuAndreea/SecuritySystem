# Smart Security

## folder structure

In "main.py" is the mqtt api.

In "app.py" is the flask api.

In "docs/" are the docs in swagger, asyncapi.

In "imgs/" are the cctv picure.

In "iots/" are the iot with the mqtt requets.

In "restler/" are the files generated by RESTler.

In "tests/" are the files for unit / integration tests. 

"currentStatus.json, logs.json" are the local database for the application.

## prerequisites

```shell
pip install requests
pip install paho-mqtt
pip install flask
```

# running

For the web server use:

```shell
flask run
```

For the mqtt listener use:

```shell
python main.py
```

To start the iot, select the iot and run:

```shell
python <iot-name>.py
```

## use

The server is running on 127.0.0.1:5000

All api requests are found in swagger.yaml

## testing

```shell
cd tests
python -m unitttest test_unit.py
python -m unitttest test_integration.py
```

## docs

Docs are available in Swagger for HTTP, AsyncAPI for MQTT.
