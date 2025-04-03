import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1714538606442 = glueContext.create_dynamic_frame.from_catalog(database="staxdb", table_name="output_parquet_file", transformation_ctx="AWSGlueDataCatalog_node1714538606442")

# Script generated for node Amazon Redshift
AmazonRedshift_node1714538654898 = glueContext.write_dynamic_frame.from_options(frame=AWSGlueDataCatalog_node1714538606442, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://aws-glue-assets-159886730810-us-west-1/temporary/", "useConnectionProperties": "true", "dbtable": "pg_catalog.pg_namespace", "connectionName": "Redshift-connection", "preactions": "CREATE TABLE IF NOT EXISTS pg_catalog.pg_namespace (id BIGINT, creation_date TIMESTAMP, title VARCHAR, body VARCHAR, comments BIGINT, accepted_answer_id BIGINT, answers BIGINT, favorite_count BIGINT, owner_display_name VARCHAR, user_id BIGINT, parent_id BIGINT, post_type_id BIGINT, score BIGINT, tags VARCHAR, views BIGINT);"}, transformation_ctx="AmazonRedshift_node1714538654898")

job.commit()