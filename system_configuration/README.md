# Database setup

Instructions for creating the database used for this tutorial from scratch:
- Create new server/database (including the PostGIS extension)
    - PostgreSQL database: http://www.postgresql.org/download
    - PostgreSQL database administration tool: http://www.pgadmin.org/download
    - PostGIS extension: http://postgis.net/install
- Add the CityGML schema with the help of [3DCityDB](http://www.3dcitydb.org/) tools (script *CREATE_DB.bat*)
- Add [EnergyADE schema](https://github.com/gioagu/3dcitydb_energy_ade).
- *Optional*: Use this newly created database as a template, clone it with the help of script *clone_new_db_from_template.py* (edit connection parameters in script).
- Use the [3DCityDB Importer/Exporter](http://www.3dcitydb.org/3dcitydb/3dimpexp/) to import file *system_configuration.gml*.
- Run script *add_energy_ade_data.py*' to add additional data mostly related to the EnergyADE (edit connection parameters in script).
 