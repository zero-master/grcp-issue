## Step 1
Change all CHANGE_ME in the main.py

## Step 2
`pip -r install requirements.txt`

## Step 3
`gunicorn -c gunicorn.conf.py -b :5000 main:app`

## Step 4
`curl localhost:5000`

## Step 5
Comment `worker_class = 'gevent'` in the `gunicorn.conf.py` and try step 3 and 4 again
 