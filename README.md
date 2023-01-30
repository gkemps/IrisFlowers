# IrisFlowers

API to classify the morphologic variation of Iris flowers of three
related species, namely Setosa, Versicolor & Virginica.

API can be deployed locally with Docker and is also already deployed on GCE. Reachable through following url: https://flowers-ouiwou46jq-ez.a.run.app

Example of request:

```
curl --location --request POST 'https://flowers-ouiwou46jq-ez.a.run.app/GetFlowerIrisClass' \
--header 'Content-Type: application/json' \
--data-raw '{
    "FlowerIrisRequestData": {
        "FlowerID": "0001",
        "SepalLength": "5.1",
        "SepalWidth": "3.5",
        "PetalLength": "1.4",
        "PetalWidth": "0.2"
    }
}'
```

Documentation can be found [here](https://flowers-ouiwou46jq-ez.a.run.app/docs)
