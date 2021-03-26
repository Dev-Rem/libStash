#!/bin/sh

set -e


#!/bin/sh


IMAGE_ID=$(docker inspect ${HEROKU_REGISTRY_IMAGE} --format={{.Id}})
PAYLOAD='{"updates": [{"type": "web", "docker_image": "'"$IMAGE_ID"'"}]}'

curl -n -X PATCH https://api.heroku.com/apps/$HEROKU_APP_NAME/formation \
  -d "${PAYLOAD}" \
  -H "Content-Type: application/json" \
  -H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
  -H "Authorization: Bearer ${HEROKU_AUTH_TOKEN}"
  
# python3.8 manage.py collectstatic --noinput --settings=libStash.settings.production 
# python3.8 manage.py makemigrations --settings=libStash.settings.production 
# python3.8 manage.py migrate --settings=libStash.settings.production

# gunicorn libStash.wsgi:application --bind 0.0.0.0:$PORT
