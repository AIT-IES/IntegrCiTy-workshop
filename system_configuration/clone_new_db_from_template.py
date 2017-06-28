# High level PostgreSQL client library.
import postgres

#
# Connect to database.
#

pg_user = 'postgres'
pg_password = 'postgres'
pg_host = 'localhost'
pg_port = '5432'
db_name_template = 'integrcity_template_25833'
db_name_new = 'integrcity_workshop'

# Construct connection string.
db_connection_string = ''.join( ( 'postgres://', pg_user, ':', pg_password, '@', pg_host, ':', pg_port, '/postgres' ) )

# Make connection
db = postgres.Postgres( db_connection_string )

# Construct 'clean' table names (avoid injection by just accepting alphanumerics and underscores, stripping out all punctuation).
db_name_template_clean = ''.join( c for c in db_name_template if ( c.isalnum() or c == '_' ) )
db_name_new_clean = ''.join( c for c in db_name_new if ( c.isalnum() or c == '_' ) )

with db.get_connection() as connection:
	# Retrieve cursor with adequate privileges.
	connection.set_isolation_level(0)
	cursor = connection.cursor()

	# Create new database from template.
	create_statement = 'CREATE DATABASE ' + db_name_new_clean + ' WITH TEMPLATE ' + db_name_template_clean + ' OWNER postgres'
	cursor.run( create_statement )

	# Set search path permanently.
	search_path_statement = 'ALTER DATABASE ' + db_name_new + ' SET search_path TO citydb, citydb_pkg, public'
	cursor.run( search_path_statement )
