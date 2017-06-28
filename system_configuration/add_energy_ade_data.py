# High level PostgreSQL client library.
import postgres

#
# Connect to database.
#

pg_user = 'postgres'
pg_password = 'postgres'
pg_host = 'localhost'
pg_port = '5432'
db_name = 'integrcity_workshop'

# Construct connection string.
db_connection_string = ''.join( ( 'postgres://', pg_user, ':', pg_password, '@', pg_host, ':', pg_port, '/', db_name ) )

# Make connection
db = postgres.Postgres( db_connection_string )


#
# Retrieve building IDs.
#

building_gml_ids = [
	'BLDG_0003000e0057a463',
	'BLDG_00030009007e0ee6',
	'BLDG_00030009007e0ec8',
	'BLDG_00030009007e0ebe',
	'BLDG_00030009007e0eb5',
	'BLDG_00030009007ef00b',
	'BLDG_0003000a00250cb4',
	'BLDG_00030009007eefff',
	'BLDG_0003000a00250cb6',
	'BLDG_0003000a00223f58',
	'BLDG_0003000a00223fa2',
	'BLDG_0003000a00223f9f',
	'BLDG_0003000a00223f6a',
	'BLDG_0003000a00250de8',
	'BLDG_00030009007e1097'
]

building_types = [
	'Single-Family House',
	'Apartment Block',
	'Single-Family House',
	'Single-Family House',
	'Apartment Block',
	'Multi-Family House',
	'Single-Family House',
	'Apartment Block',
	'Multi-Family House',
	'Multi-Family House',
	'Multi-Family House',
	'Single-Family House',
	'Apartment Block',
	'Multi-Family House',
	'Apartment Block',
]

building_ids = []

select_statement = 'SELECT co.id FROM citydb.cityobject AS co WHERE co.gmlid = %(gmlid)s'

for gml_id in  building_gml_ids:
	id = db.one( select_statement, { 'gmlid' : gml_id } )
	building_ids.append( id )

#
# Define time series.
#

time_series = [
	[2.39, 2.68, 2.98, 3.04, 3.04, 3.2, 3.82, 4.95, 7, 8.33, 8.87, 8.91, 8.89, 8.49, 8.25, 7.86, 6.68, 3.58, 2.83, 3.1, 3.46, 3.67, 3.86, 4.34],
	[129.01, 128.5, 127.91, 124.73, 121.1, 122.48, 133.96, 158.81, 170.5, 179.64, 181.8, 192.07, 194.03, 188.57, 187.1, 181.1, 171.19, 156.9, 135.97, 127.69, 128.59, 125.63, 121.12, 110.46],
	[1.54, 1.59, 1.61, 1.62, 1.6, 1.55, 2.49, 3.99, 6.56, 8.45, 9.24, 9.46, 9.6, 9.59, 9.33, 8.74, 7.35, 4.21, 3.1, 2.79, 2.77, 2.76, 2.76, 2.76],
	[1.2, 1.34, 1.57, 1.72, 1.74, 1.78, 1.96, 2.86, 4.92, 6.47, 7.37, 7.87, 8.06, 8.18, 8.15, 7.91, 6.77, 3.67, 2.59, 2.22, 2.18, 2.17, 2.17, 2.17],
	[89.67, 91.09, 91.32, 92.98, 93.27, 93.37, 94.05, 95.41, 91.61, 90.32, 88.06, 85.31, 82.24, 76.96, 74.56, 70.37, 70.34, 71.41, 71.67, 73.68, 75.37, 75.34, 72.8, 64.48],
	[11.03, 10.42, 10.28, 10.18, 10.16, 10.28, 10.42, 11.52, 13.18, 15.34, 17.32, 17.45, 17.13, 17.32, 13.36, 12.9, 10.62, 10.16, 7.52, 6.75, 6.73, 6.05, 5.37, 5.46],
	[1.78, 1.66, 1.55, 1.51, 1.48, 1.63, 2.38, 3.91, 6.4, 7.99, 8.58, 9.09, 9.47, 9.33, 9.46, 9.32, 7.81, 4.47, 3.01, 2.66, 2.3, 2.05, 1.9, 1.68],
	[49.28, 48.77, 48.17, 48.19, 48.39, 50.59, 54.73, 68.94, 85.24, 131.21, 149.75, 157.48, 161.94, 159.8, 162.21, 157, 147.3, 129.85, 107.93, 102.52, 90.73, 88.66, 52.76, 45.48],
	[7.56, 9.9, 11.15, 11.73, 12.2, 12.46, 14.01, 16.48, 17.46, 19, 19.94, 19.93, 20.54, 21.23, 21.59, 21.47, 21.69, 21.99, 22.23, 22.04, 18.94, 16.98, 17.01, 17.3],
	[5.72, 6.12, 6.58, 7.93, 8.65, 8.93, 8.19, 6.97, 6.69, 9.07, 10.94, 11.8, 12.78, 13.02, 13.04, 13.44, 13.42, 12.44, 8.9, 6.36, 6.09, 7.38, 9.04, 9.72],
	[13.47, 13.05, 12.97, 12.9, 12.88, 13.05, 14.19, 16.44, 18.14, 21.85, 23.09, 23.94, 24.94, 25.15, 24.71, 22.66, 22.69, 23.09, 22.68, 21.69, 18.43, 15.88, 14.89, 14.04],
	[0.84, 0.84, 1.75, 2.03, 2.11, 2.15, 2.51, 3.56, 5.57, 6.81, 7.66, 7.89, 7.98, 7.94, 7.97, 7.62, 6.46, 3.36, 2.28, 2.13, 2.13, 2.13, 2.13, 1.45],
	[69.49, 56.96, 50.54, 47.25, 34.16, 34.36, 53.35, 63.85, 84.3, 93.85, 104.14, 109.09, 113.09, 105.44, 91.57, 87.7, 83.29, 82.67, 79.1, 78.47, 78.26, 75.86, 80.75, 87.84],
	[12.46, 11.87, 11.74, 11.65, 11.11, 11.18, 12.38, 14.73, 16.43, 20.12, 22.23, 22.8, 22.89, 22.91, 22.86, 23.08, 23.11, 22.7, 21.67, 20.55, 16.39, 13.68, 12.59, 11.9],
	[72.91, 72.92, 53.08, 49.96, 48.69, 48.69, 46.56, 43.22, 50.33, 56.22, 58.5, 58.97, 75.98, 76.3, 76.15, 76.01, 75.66, 69.91, 58.95, 51.63, 47.43, 42.74, 41.49, 42.82]
]

time_series_gml_ids = [
	'id_timeseries_energydemand_01',
	'id_timeseries_energydemand_02',
	'id_timeseries_energydemand_03',
	'id_timeseries_energydemand_04',
	'id_timeseries_energydemand_05',
	'id_timeseries_energydemand_06',
	'id_timeseries_energydemand_07',
	'id_timeseries_energydemand_08',
	'id_timeseries_energydemand_09',
	'id_timeseries_energydemand_10',
	'id_timeseries_energydemand_11',
	'id_timeseries_energydemand_12',
	'id_timeseries_energydemand_13',
	'id_timeseries_energydemand_14',
	'id_timeseries_energydemand_15'
]

energy_demand_gml_ids = [
	'id_energydemand_building_01',
	'id_energydemand_building_02',
	'id_energydemand_building_03',
	'id_energydemand_building_04',
	'id_energydemand_building_05',
	'id_energydemand_building_06',
	'id_energydemand_building_07',
	'id_energydemand_building_08',
	'id_energydemand_building_09',
	'id_energydemand_building_10',
	'id_energydemand_building_11',
	'id_energydemand_building_12',
	'id_energydemand_building_13',
	'id_energydemand_building_14',
	'id_energydemand_building_15'
]

#
# Add Energy ADE buildings.
#

db.run( 'TRUNCATE citydb.nrg8a_building CASCADE' )

nrg_buildings_insert_statement = 'INSERT INTO citydb.nrg8a_building(id, objectclass_id, type, type_codespace, constr_weight, is_landmarked, ref_point) VALUES ( %(bid)s, 26, %(type)s, NULL, \'Medium\', NULL, NULL )'

for i in range( 0, 15 ):
	db.run( nrg_buildings_insert_statement, { 'bid' : building_ids[i], 'type' : building_types[i] } )


#
# Insert time series and associate them to energy demand of buildings.
# 

db.run( 'TRUNCATE citydb.nrg8a_time_series CASCADE' )
db.run( 'TRUNCATE citydb.nrg8a_energy_demand CASCADE' )

time_series_insert_statement = 'INSERT INTO citydb.nrg8a_time_series(id, objectclass_id, gmlid, gmlid_codespace, name, name_codespace, acquisition_method, interpolation_type, quality_description, source, time_array, values_array, values_unit, array_length, temporal_extent_begin, temporal_extent_end, time_interval, time_interval_unit) VALUES ( %(tsid)s, 202, %(tsgmlid)s, NULL, NULL, NULL, \'SyntheticTestProfile\', \'AverageInSucceedingInterval\', NULL, NULL, NULL, %(ts)s, \'kWh\', 24,\'2017-01-01\'::timestamp(0) with time zone, \'2017-01-02\'::timestamp(0) with time zone, 1, \'hour\' )'

energy_demand_insert_statement = 'INSERT INTO citydb.nrg8a_energy_demand( id, objectclass_id, gmlid, gmlid_codespace, name, name_codespace, description, end_use, max_load, max_load_unit, time_series_id, cityobject_id ) VALUES ( %(edid)s, 232, %(edgmlid)s, NULL, NULL, NULL, \'energy demand for space heating\', \'SpaceHeating\', NULL, NULL, %(tsid)s, %(bid)s ) '

for i in range( 0, 15 ):
	db.run( time_series_insert_statement, { 'tsid' : i+1, 'tsgmlid' : time_series_gml_ids[i], 'ts' : time_series[i] } )
	db.run( energy_demand_insert_statement, { 'edid' : i, 'edgmlid' : energy_demand_gml_ids[i], 'tsid' : i+1, 'bid' : building_ids[i] } )


#
# Add city object groups (representing space heating supply areas)
#

max_oid_query = 'SELECT id FROM citydb.cityobject ORDER BY id DESC LIMIT 1'
max_oid = db.one( max_oid_query )

city_object_ids = [ max_oid + 1, max_oid + 2 ]

city_object_insert_statement = 'INSERT INTO citydb.cityobject( id, objectclass_id, gmlid, gmlid_codespace, name, name_codespace, description, envelope, creation_date, termination_date, relative_to_terrain, relative_to_water, last_modification_date, updating_person, reason_for_update, lineage, xml_source ) VALUES ( %(ogid)s, 23, %(gmlid)s, NULL, NULL, NULL, NULL, NULL, now()::timestamp, NULL, NULL, NULL, now()::timestamp, %(user)s, NULL, NULL, NULL )'

db.run( city_object_insert_statement, { 'ogid' : city_object_ids[0], 'gmlid' : 'OBJGRP_1', 'user' : pg_user } )
db.run( city_object_insert_statement, { 'ogid' : city_object_ids[1], 'gmlid' : 'OBJGRP_2', 'user' : pg_user } )

db.run( 'TRUNCATE citydb.cityobjectgroup CASCADE' )

object_group_insert_statement = 'INSERT INTO citydb.cityobjectgroup( id, class, class_codespace, function, function_codespace, usage, usage_codespace, brep_id, other_geom, parent_cityobject_id ) VALUES ( %(ogid)s, NULL, NULL, %(func)s, NULL, NULL, NULL, NULL, NULL, NULL ) '

db.run( object_group_insert_statement, { 'ogid' : city_object_ids[0], 'func' : 'space_heating_supply_area_1' } )
db.run( object_group_insert_statement, { 'ogid' : city_object_ids[1], 'func' : 'space_heating_supply_area_2' } )


#
# Associate buildings to city object groups.
#

db.run( 'TRUNCATE citydb.group_to_cityobject CASCADE' )

group_member_insert_statement = 'INSERT INTO citydb.group_to_cityobject( cityobject_id, cityobjectgroup_id, role ) VALUES ( %(coid)s, %(ogid)s, \'space_heating_consumer\' ) '

for i in range( 0, 8 ):
	db.run( group_member_insert_statement, { 'coid' : building_ids[i], 'ogid' : city_object_ids[0] } )

for i in range( 8, 15 ):
	db.run( group_member_insert_statement, { 'coid' : building_ids[i], 'ogid' : city_object_ids[1] } )

