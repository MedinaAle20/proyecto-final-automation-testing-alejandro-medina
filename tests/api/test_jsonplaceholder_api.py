import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_lista_usuarios():
    # GET: valida que la API devuelva usuarios con campos basicos.
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) > 0
    assert {"id", "name", "email"}.issubset(body[0].keys())


def test_post_crear_usuario():
    # POST: envia un usuario de ejemplo y valida la respuesta.
    payload = {
        "name": "Alejandro Medina",
        "username": "amedina",
        "email": "alejandro.medina@example.com",
    }

    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)
    body = response.json()

    assert response.status_code == 201
    assert body["name"] == payload["name"]
    assert body["username"] == payload["username"]
    assert body["email"] == payload["email"]
    assert "id" in body


def test_delete_usuario():
    # DELETE: en esta API demo se valida el status esperado.
    response = requests.delete(f"{BASE_URL}/users/1", timeout=10)

    assert response.status_code == 200
