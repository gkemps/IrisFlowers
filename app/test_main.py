from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_request1():
    response = client.post(
        "/GetFlowerIrisClass",
        json={"FlowerIrisRequestData": {
            "FlowerID": "0001",
            "SepalLength": "5.1",
            "SepalWidth": "3.5",
            "PetalLength": "1.4",
            "PetalWidth": "0.2"
        }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
    "FlowerIrisResponseData": {
        "FlowerID": "0001",
        "ReturnCode": 0,
        "IrisClass": "Setosa"
    }
}

def test_create_request1_float():
    response = client.post(
        "/GetFlowerIrisClass",
        json={"FlowerIrisRequestData": {
            "FlowerID": "0001",
            "SepalLength": 5.1,
            "SepalWidth": 3.5,
            "PetalLength": 1.4,
            "PetalWidth": 0.2
        }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
    "FlowerIrisResponseData": {
        "FlowerID": "0001",
        "ReturnCode": 0,
        "IrisClass": "Setosa"
    }
}


def test_create_request2():
    response = client.post(
        "/GetFlowerIrisClass",
        json={
            "FlowerIrisRequestData": {
                "FlowerID": "0002",
                "SepalLength": "7",
                "SepalWidth": "3.2",
                "PetalLength": "4.7",
                "PetalWidth": "1.4"
            }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
    "FlowerIrisResponseData": {
        "FlowerID": "0002",
        "ReturnCode": 0,
        "IrisClass": "Versicolor"
    }
}


def test_create_request3():
    response = client.post(
        "/GetFlowerIrisClass",
        json={
            "FlowerIrisRequestData": {
                "FlowerID": "0003",
                "SepalLength": "6.3",
                "SepalWidth": "3.3",
                "PetalLength": "6",
                "PetalWidth": "2.5"
            }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "FlowerIrisResponseData": {
            "FlowerID": "0003",
            "ReturnCode": 0,
            "IrisClass": "Virginica"
        }
    }

def test_all_zero():
    response = client.post(
        "/GetFlowerIrisClass",
        json={
            "FlowerIrisRequestData": {
                "FlowerID": "0004",
                "SepalLength": "0.0",
                "SepalWidth": "0.0",
                "PetalLength": "0.0",
                "PetalWidth": "0.0"
            }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "FlowerIrisResponseData": {
            "FlowerID": "0004",
            "ReturnCode": 0,
            "IrisClass": "Setosa"
        }
    }    

def test_missing_field():
    response = client.post(
        "/GetFlowerIrisClass",
        json={"FlowerIrisRequestData": {
            "FlowerID": "0001",
            "SepalLength": "5.1",
            "PetalLength": "1.4",
            "PetalWidth": "0.2"
        }
        },
    )
    assert response.status_code == 422

def test_wrong_type():
    response = client.post(
        "/GetFlowerIrisClass",
        json={"FlowerIrisRequestData": {
            "FlowerID": "0001",
            "SepalLength": "sometext",
            "PetalLength": "1.4",
            "PetalWidth": "0.2"
        }
        },
    )
    assert response.status_code == 422    

def test_long_flower_id():
    response = client.post(
        "/GetFlowerIrisClass",
        json={
            "FlowerIrisRequestData": {
                "FlowerID": "00012",
                "SepalLength": "5.1",
                "SepalWidth": "3.5",
                "PetalLength": "1.4",
                "PetalWidth": "0.2"
            }
        },
    )
    assert response.status_code == 422

def test_negative_values():
    response = client.post(
        "/GetFlowerIrisClass",
        json={
            "FlowerIrisRequestData": {
                "FlowerID": "0001",
                "SepalLength": "-5.1",
                "SepalWidth": "-3.5",
                "PetalLength": "-1.4",
                "PetalWidth": "-0.2"
            }
        },
    )
    assert response.status_code == 422
