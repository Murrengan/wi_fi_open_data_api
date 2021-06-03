import json

from django.core.management import BaseCommand

from crud.models import WiFiSpot


class Command(BaseCommand):
    help = 'Загрузить данные в базу данных'

    def handle(self, *args, **options):
        clear = options.get('clear')
        if clear:
            WiFiSpot.objects.all().delete()

        wi_fi_spots = self.prepare_wi_fi_spots()
        try:
            WiFiSpot.objects.bulk_create(
                [WiFiSpot(
                    external_id=spot['external_id'],
                    name=spot['name'],
                    adm_aria=spot['adm_aria'],
                    district=spot['district'],
                    park_name=spot['park_name'],
                    wi_fi_name=spot['wi_fi_name'],
                    coverage_area=spot['coverage_area'],
                    function_flag=spot['function_flag'],
                    access_flag=spot['access_flag'],
                    longitude_WGS84=spot['longitude_WGS84'],
                    latitude_WGS84=spot['latitude_WGS84']
                ) for spot in wi_fi_spots]
            )
        except Exception as ex:
            print(ex)
        self.stdout.write(self.style.SUCCESS('Wi-fi точки успешно загружены>'))

    def add_arguments(self, parser):
        parser.add_argument(
          '-c', '--clear', action='store_const', const=True,
          help="Удаляет все записи о wi-fi точках и загрузить новые")

    @staticmethod
    def prepare_wi_fi_spots():
        wi_fi_spots = []
        with open('wifi_dataset.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                spot = {'external_id': int(i.get('ID', 0)),
                        'name': i.get('Name', ''),
                        'adm_aria': i.get('AdmArea', ''),
                        'district': i.get('District', ''),
                        'park_name': i.get('ParkName', ''),
                        'wi_fi_name': i.get('WiFiName', ''),
                        'coverage_area': int(i.get('CoverageArea', '')),
                        'function_flag': i.get('FunctionFlag', ''),
                        'access_flag': i.get('AccessFlag', ''),
                        'longitude_WGS84': float(i.get('Longitude_WGS84', 0)),
                        'latitude_WGS84': float(i.get('Latitude_WGS84', 0))}
                wi_fi_spots.append(spot)
        return wi_fi_spots
