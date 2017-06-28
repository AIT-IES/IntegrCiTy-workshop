SELECT
	EXTRACT( YEAR FROM cb.year_of_construction) AS year_of_construction,
	nb.type,
	nb.id,
	ts.values_array,
	ts.values_unit,
	ts.array_length,
	ts.time_interval,
	ts.time_interval_unit
FROM
	citydb.nrg8a_time_series AS ts 
INNER JOIN
	citydb.nrg8a_energy_demand AS ed
ON
	ts.id = ed.time_series_id
INNER JOIN
	citydb.nrg8a_building AS nb
ON
	nb.id = ed.cityobject_id
INNER JOIN
	citydb.building AS cb
ON
	cb.id = ed.cityobject_id
WHERE
	ts.objectclass_id = 202 AND -- type RegularTimeSeries (object class ID = 202)
	ed.objectclass_id = 232 AND -- energy demand (object class ID = 232)
	ed.end_use = 'SpaceHeating' AND -- space heating (end_use = SpaceHeating)
	ed.cityobject_id = %(coid)s
ORDER BY
	nb.id ASC