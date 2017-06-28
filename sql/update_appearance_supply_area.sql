UPDATE
	citydb.surface_data
SET
	x3d_diffuse_color = %(rgb)s
WHERE
	id 
IN (
	SELECT
		sd.id AS id
	FROM
		citydb.appearance AS ap
	INNER JOIN
		citydb.appear_to_surface_data AS apsd
	ON
		apsd.appearance_id = ap.id
	INNER JOIN
		citydb.surface_data AS sd
	ON
		sd.id = apsd.surface_data_id
	INNER JOIN
		citydb.cityobject AS co
	ON
		co.id = ap.cityobject_id
	INNER JOIN
		citydb.group_to_cityobject AS gm
	ON
		gm.cityobject_id = co.id
	INNER JOIN
		citydb.cityobjectgroup AS og
	ON
		og.id = gm.cityobjectgroup_id
	WHERE
		sd.name = 'displayResultsAttributes' AND
		ap.theme = 'displayResults' AND
		co.objectclass_id = 26 AND -- building (object class ID = 26)
		og.function = %(cog)s
)