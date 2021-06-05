import json

from django.core.management import BaseCommand

from crud.models import WiFiSpot


class Command(BaseCommand):
    help = 'Загрузит данные из wifi_dataset.json в базу данных'

    def handle(self, *args, **options):
        clear = options.get('clear')
        only_initial_upload = options.get('only_initial_upload')
        if clear:
            'Полномтью очистит wi-fi spots из бд'
            WiFiSpot.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Все Wi-fi удалены'))
            return
        if only_initial_upload:
            'Позволит загрузить wifi_dataset.json только в пустую бд'
            if len(WiFiSpot.objects.all()) != 0:
                message = """
                Ты запускаешь команду upload_data_to_db с флагом "--only_initial_upload", но бд не пуская. 
                Либо убери флаг, либо почисти бд запустив команду с флагом '-с'.
                Это сделано с целью защиты от дублирования начальных данных в бд.
                Наверняка есть более интересное решение - надо подумать.
                """
                self.stdout.write(self.style.ERROR(message))
                return

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
            self.stdout.write(self.style.SUCCESS('Wi-fi точки успешно загружены!'))
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f'Тут какая-то ситуация: {ex}'))

    def add_arguments(self, parser):
        parser.add_argument(
          '-c', '--clear', action='store_const', const=True,
          help="Удаляет все записи о wi-fi точках и загрузить новые")
        parser.add_argument(
          '-oiu', '--only_initial_upload', action='store_const', const=True,
          help="Загрузит данные из датасета только на пустую базу")

    @staticmethod
    def prepare_wi_fi_spots():
        # в зависимости от потребностей бизнеса, мы может прописывать дефолтное значние и уже его писать в бд
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
                        'longitude_WGS84': float(i.get('Longitude_WGS84', 0.0)),
                        'latitude_WGS84': float(i.get('Latitude_WGS84', 0.0))}
                wi_fi_spots.append(spot)
        return wi_fi_spots
