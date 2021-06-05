# Wi-Fi open data api

wi_fi_open_data is REST API application provides easy management for working with wi-fi open data spots.

### Current features

* CRUD to work with wi-fi spots
* Search for existing wi-fi spots
* Parser for loading prepared data from a json file
* Convenient launch via docker-compose
* Simple protection by nginx from dos attacks

### For development used:

* [Python](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/) 
* [Postgresql 11](https://www.postgresql.org/) 
* [Nginx](https://www.nginx.com/) 

### Installation
```bash
git clone https://github.com/Murrengan/wi_fi_open_data_api.git
cd wi_fi_open_data_api
docker-compose up
```

### Create admin
If you want to get access to base admin panel, create admin user
```bash
docker ps # for find wi_fi_open_data_core container id
docker exec -it __container_id__ python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
```

### API

#### Create Wi-fi spots

```bash
POST /api/crud/
```
Creates a wi-fi spot object with a unique id.  The request body is ```application/json``` with a wi-fi pont object.

Wi-fi pont it's an object of this type:

```bash
{
    "id": 1,
    "external_id": 792, 
    "name": "Точка доступа №792",
    "adm_aria": "Южный административный округ",
    "district": "район Нагатинский Затон",
    "park_name": "Государственное бюджетное учреждение культуры города Москвы «Московский государственный объединенный художественный историко-архитектурный и природно-ландшафтный музей-заповедник»",
    "wi_fi_name": "Moscow_WiFi_Free",
    "coverage_area": 20,
    "function_flag": "действует",
    "access_flag": "открытая сеть",
    "longitude_WGS84": 37.660503,
    "latitude_WGS84": 55.664444
}
```

Required fields:
```bash
{
  "external_id": 1586,
  "name": "Имя точки wi-fi"
}
```
Returns JSON:
```bash
{
    "id": 1186,
    "external_id": 1586,
    "name": "Имя точки wi-fi",
    "adm_aria": null,
    "district": null,
    "park_name": null,
    "wi_fi_name": null,
    "coverage_area": null,
    "function_flag": null,
    "access_flag": null,
    "longitude_WGS84": null,
    "latitude_WGS84": null
}
```

#### Find Wi-fi spots
```bash
GET /api/search/?search=Точка доступа №792
GET /api/search/?search=950
```
The search works by entering the text in ```external_id``` and ```name``` spot fields.
Results-an array of search results in this format:
```bash
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 418,
            "external_id": 950,
            "name": "Точка доступа №950",
            "adm_aria": "Восточный административный округ",
            "district": "район Сокольники",
            "park_name": "Государственное автономное учреждение культуры города Москвы «Парк культуры и отдыха «Сокольники»",
            "wi_fi_name": "Moscow_WiFi_Free",
            "coverage_area": 20,
            "function_flag": "действует",
            "access_flag": "открытая сеть",
            "longitude_WGS84": 37.675569,
            "latitude_WGS84": 55.793707
        }
    ]
}
```

### Other api endpoints you can find in Swagger
```bash
http://127.0.0.1/api/schema
```

# 🌟If you like this code, and you from artlebedev team, please smash on star. 🌟 
