from aatools.cds.area import AreaFromStations, Station

FFWC_STATIONS = {
    "Bahadurabad": Station(lon=89.65, lat=25.15),
}


def main():
    area = AreaFromStations(stations=FFWC_STATIONS)
    return area


if __name__ == "__main__":
    main()
