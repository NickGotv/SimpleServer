from read_json import read_json

MAP_DATA = {"Me": "121231212312",
            "D": "481148"}


def test_read_json():
    with open('db.json') as json_file:
        data = read_json(json_file)
        json_file.close()
        print(f"data:{data}")
        assert data == MAP_DATA, "Maps should be identical"
