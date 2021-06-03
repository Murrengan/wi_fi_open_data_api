import json

from crud.models import WiFiSpot

with open('wifi_dataset.json', 'r') as f:
    data = json.load(f)
    for i in data:
        # в зависимости от потребностей бизнеса, мы может прописывать дефолтное значние и уже его писать в бд
        external_id = int(i.get('ID', 0))
        name = i.get('Name', '')
        adm_aria = i.get('AdmArea', '')
        district = i.get('District', '')
        park_name = i.get('ParkName', '')
        wi_fi_name = i.get('WiFiName', '')
        coverage_area = int(i.get('CoverageArea', ''))
        function_flag = i.get('FunctionFlag', '')
        access_flag = i.get('AccessFlag', '')
        longitude_WGS84 = float(i.get('Longitude_WGS84', 0))
        latitude_WGS84 = float(i.get('Latitude_WGS84', 0))
        try:
            wi_fi_spot, created = WiFiSpot.objects.get_or_create(
                external_id=external_id,
                name=name,
                adm_aria=adm_aria,
                district=district,
                park_name=park_name,
                wi_fi_name=wi_fi_name,
                coverage_area=coverage_area,
                function_flag=function_flag,
                access_flag=access_flag,
                longitude_WGS84=longitude_WGS84,
                latitude_WGS84=latitude_WGS84
            )
            if created:
                wi_fi_spot.save()
            print(f"Wi-fi точка {wi_fi_spot} создана.\n")
        except Exception as ex:
            print(f'Тут какая-то ситуация при создании wi-fi точки - {name}: \n{ex}')
