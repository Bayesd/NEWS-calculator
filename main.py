MAX_LAT = 90
MIN_LAT = -90
MAX_LONG = 180
MIN_LONG = -180
DEFAULT_NEWS_VALUE = 2

north_and_south_max_value = DEFAULT_NEWS_VALUE * 2
west_and_east_max_value = DEFAULT_NEWS_VALUE * 2


def calculate_value_for_north_or_south(lat):
    if lat > 0:
        north_value_percentage = ((lat + abs(MIN_LAT)) / (MAX_LAT * 2))
        north_value = north_value_percentage * (DEFAULT_NEWS_VALUE * 2)
        south_value = (DEFAULT_NEWS_VALUE * 2) - north_value
        return north_value, south_value
    elif lat < 0:
        south_value_percentage = ((lat + abs(MIN_LAT)) / (MAX_LAT * 2))
        south_value = south_value_percentage * (DEFAULT_NEWS_VALUE * 2)
        north_value = (DEFAULT_NEWS_VALUE * 2) - south_value
        return [north_value, south_value]
    else:
        return [DEFAULT_NEWS_VALUE, DEFAULT_NEWS_VALUE]


def calculate_value_for_east_and_west(long):
    if long > 0:
        east_value_percentage = ((long + abs(MIN_LAT)) / (MAX_LONG * 2))
        east_value = east_value_percentage * (DEFAULT_NEWS_VALUE * 2)
        west_value = (DEFAULT_NEWS_VALUE * 2) - east_value
        return east_value, west_value
    elif long < 0:
        west_value_percentage = ((long + abs(MIN_LAT)) / (MAX_LONG * 2))
        west_value = west_value_percentage * (DEFAULT_NEWS_VALUE * 2)
        east_value = (DEFAULT_NEWS_VALUE * 2) - west_value
        return [east_value, west_value]
    else:
        return [DEFAULT_NEWS_VALUE, DEFAULT_NEWS_VALUE]


def order_news_list(ns_values, ew_values):
    news_list = [ns_values[0], ew_values[0], ew_values[1], ns_values[1]]
    return news_list


def get_latitude_input():
    while True:
        try:
            latitude = float(input("Enter the latitudinal value: "))
            if -90 <= latitude <= 90:
                return latitude
            raise ValueError()
        except ValueError:
            print("Latitude must be a value between -90 and 90.")


def get_longitude_input():
    while True:
        try:
            longitude = float(input("Enter the longitudinal value: "))
            if -180 <= longitude <= 180:
                return longitude
            raise ValueError()
        except ValueError:
            print("Latitude must be a value between -180 and 180.")


def generate_news_values_from_input():
    print("Go to latlong.net and enter the origin of your character or the creator of the character")
    latitude = get_latitude_input()
    longitude = get_longitude_input()
    north_and_south_values = calculate_value_for_north_or_south(latitude)
    east_and_west_values = calculate_value_for_east_and_west(longitude)
    attack_values = order_news_list(north_and_south_values, east_and_west_values)
    print(
        f"North:\t{attack_values[0]}\nEast:\t{attack_values[1]}\nWest:\t{attack_values[2]}\nSouth:\t{attack_values[3]}")
    return attack_values


generate_news_values_from_input()
