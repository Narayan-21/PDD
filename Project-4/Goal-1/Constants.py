from parse import date_parse

fname_personal = 'personal_info.csv'
fname_employment = 'employment.csv'
fname_vehicles = 'vehicles.csv'
fname_update_status = 'update_status.csv'

fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

personal_parser = (str, str, str, str, str)
employment_parser = (str, str, str, str)
vehicles_parser = (str, str, str, int)
update_status_parser = (str, date_parse, date_parse)

parsers = personal_parser, employment_parser, vehicles_parser, update_status_parser

personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_status_class_name = 'UpdateStatus'
class_names = personal_class_name, employment_class_name, vehicle_class_name, update_status_class_name
