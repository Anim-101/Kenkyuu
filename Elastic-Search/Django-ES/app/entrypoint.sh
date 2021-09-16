#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgress..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL Started"
fi

#python manage.py flush --no-input
#python manage.py migrate

exec "$@"


var childTicket = [1, , 3, 4]

watcher.something {
    for child in childTicket {
        fetch(API)
        name
    }
}


{
    name: 'akash',
    name: 'anim',
    name: 'muhahaha',
    name: 'ouhhoisosososso'
}
