import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

# Do not use gevent worker class, see: https://github.com/GoogleCloudPlatform/google-cloud-python/issues/3486
# It runs into weird issues with Datastore, seems to work fine with BigQuery tho.
worker_class = 'gevent'

