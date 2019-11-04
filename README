## Projekt baz danych ##
### Konferencje ###

1. Stworzenie obrazu Dockerowego

   ```bash
   $ docker build -t projekt .
   Sending build context to Docker daemon  67.07kB
   Step 1/5 : FROM library/postgres
    ---> f88dfa384cc4
   Step 2/5 : ENV POSTGRES_USER docker
    ---> Using cache
    ---> 0c6f84296b9d
   Step 3/5 : ENV POSTGRES_PASSWORD docker
    ---> Using cache
    ---> 17d195467ec2
   Step 4/5 : ENV POSTGRES_DB docker
    ---> Using cache
    ---> 20b3058ae517
   Step 5/5 : COPY init.sql /docker-entrypoint-initdb.d/init.sql
    ---> 68adf29b3320
   Successfully built 68adf29b3320
   Successfully tagged proj:latest
   
   ```

2. Uruchomienie obrazu

   ```bash
   $ docker run -d -p 5432:5432 projekt
   * prints container id *
   ```

3. Sprawdzenie działania obrazu

	```bash
	$ docker ps -a
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
	6bcf6d0dbfdc        projekt             "docker-entrypoint.s…"   10 seconds ago      Up 8 seconds        0.0.0.0:5432->5432/tcp   thirsty_austin

	```

