def test_read_all_crystals_returns_empty_list(client):
    # Act
    response = client.get("/crystals")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# client should be passed in whenever HTTP requests are required(sent)
def test_read_crystal_by_id(client, make_two_crystals):
    response = client.get("/crystals/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
                "id":2,
                "name": "Garnet",
                "color": "Red",
                "powers": "Awesome Powers"
            }


def test_create_crystal(client):
    response = client.post("/crystals", json={
        "name": "Tiger's Eye",
                "color": "Orange",
                "powers": "Tiger Powers"
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == "Crystal Tiger's Eye successfully created."