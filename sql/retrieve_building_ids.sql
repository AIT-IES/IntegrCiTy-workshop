SELECT
	gm.cityobject_id
FROM
	citydb.group_to_cityobject AS gm
INNER JOIN
	citydb.cityobject AS co
ON
	gm.cityobject_id = co.id
WHERE
	gm.cityobjectgroup_id = %(ogid)s AND
	co.objectclass_id = 26 -- building (object class ID = 26)
ORDER BY
	gm.cityobject_id ASC