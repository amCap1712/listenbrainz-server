import os

# Parent directory containing listens and data driven from ListenBrainz.
LISTENBRAINZ_DATA_DIRECTORY = os.path.join('/', 'data', 'listenbrainz')
# Directory containing similar artist relation.
# (This is a temporary path till incremental dumps for similar artists are prepared)
SIMILAR_ARTIST_DIR = '/similar_artists'


# Parent directory containing data used in and generated by recommendation engine.
RECOMMENDATION_PARENT_DIR = os.path.join('/', 'recommendation')
# Directory containing dataframes to be used in generating recommendations (not necessarily).
DATAFRAME_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'dataframe')
# Directory containing model metadata and the real models to be used for generating recommendations.
MODEL_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'model')
# Directory containing candidate sets to be used for generating recommendations.
CANDIDATE_SET_DIR = os.path.join(RECOMMENDATION_PARENT_DIR, 'candidate_set')
# Directory containing RDD checkpoints to break lineage while using iterative algorithms.
CHECKPOINT_DIR = os.path.join('/', 'checkpoint')
# Directory to save best models
DATA_DIR = os.path.join(MODEL_DIR, 'data')

# Absolute path to dataframes used in processing raw data/listens.
USERS_DATAFRAME_PATH = DATAFRAME_DIR + '/' + 'users_df.parquet'
RECORDINGS_DATAFRAME_PATH = DATAFRAME_DIR + '/' + 'recordings_df.parquet'
# Absolute path to processed data/listens ready to be trained.
PLAYCOUNTS_DATAFRAME_PATH = DATAFRAME_DIR + '/' + 'playcounts_df.parquet'
# Absolute path to similar artist relation.
SIMILAR_ARTIST_DATAFRAME_PATH = SIMILAR_ARTIST_DIR + '/' + 'artist_credit_artist_credit_relations.parquet'
# Absolute path to candidate sets.
TOP_ARTIST_CANDIDATE_SET = os.path.join(CANDIDATE_SET_DIR, 'top_artist', 'top_artist.parquet')
SIMILAR_ARTIST_CANDIDATE_SET = os.path.join(CANDIDATE_SET_DIR, 'similar_artist', 'similar_artist.parquet')
# Absolute path to model metadata.
MODEL_METADATA = MODEL_DIR + '/' + 'model_metadata.parquet'
# Absolute path to recording mbid->msid and artist mbid-msid mapping.
MBID_MSID_MAPPING = os.path.join('/', 'mapping', 'msid_mbid_mapping.parquet')
# Absolute path to mapped listens.
MAPPED_LISTENS = DATAFRAME_DIR + '/' + 'mapped_listens_df.parquet'
# Absolute path to save dataframe metadata
DATAFRAME_METADATA = DATAFRAME_DIR + '/' + 'dataframe_metadata.parquet'

# Absolute path to save import metadata
IMPORT_METADATA = "/import_metadata.parquet"

# Path to files downloaded from FTP.
FTP_FILES_PATH = '/rec/listenbrainz_spark'
