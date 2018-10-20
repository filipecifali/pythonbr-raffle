# Requirements

`Docker-CE >18.06`

User in docker group or prefix sudo to each following command

# Install

```sh
$ docker-compose build
```

# Run

```sh
$ docker-compose up
```

# Import CSV

```sh
$ docker run -v /home/pythonbr-raffle:/src -it pythonbrraffle_web /bin/bash
# python manage.py import -s ',' -e 8 "sample.csv"
```


