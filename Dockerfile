#Docker image for Python 3 latest i.e 3.6 at the time of writing this
FROM python:3.6

# Install gpg
RUN apt-get update && apt-get install gnupg2 -y
RUN apt-get install -y ca-certificates wget

WORKDIR /app
COPY . .

# compensate for ioctl error
# RUN export GPG_TTY=$(tty) 
# Add keys to gpg
RUN gpg2 --list-keys

# RUN gpg2 -v --batch --import <(echo "$LAUNCHPAD_GPG_PRIVATE_KEY")
# RUN gpg2 --import public.key
# RUN gpg2 --import private.key
# COPY ${HOME}/.gnupg/private.asc /root/.gnupg
# COPY ${HOME}/.gnupg/public.gpg /root/.gnupg

RUN echo "$LAUNCHPAD_GPG_PRIVATE_KEY" > /root/.gnupg/private.asc
RUN echo "$LAUNCHPAD_GPG_PUBLIC_KEY" > /root/.gnupg/public.gpg


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# fixing windows line endings problems.
COPY ./entrypoint.sh entrypoint.sh.raw
# RUN sed 's/\r$//' entrypoint.sh.raw > entrypoint.sh \
#     && rm entrypoint.sh.raw

# These env variables must be added on staging and production env
# ENV PYTHONUNBUFFERED=1 \
#     DJANGO_SETTINGS_MODULE='base.settings.local' \
#     SECRET_KEY='y9+vd#2($(qwpk@a(dn7n7!2k*)49i#^)+uywsujgs7\$o##f5r' \
#     RUN_MIGRATE=1 \
#     DEBUG=1 \
#     ADMIN_EMAIL='admin@gmail.com' \
#     ADMIN_PASSWORD='admin123' \
#     DATABASE_URL='postgres://bynde:123@db:5432/bynde' \
#     CELERY_BROKER_URL='redis://redis:6379' \
#     CELERY_RESULT_BACKEND='django-db'


EXPOSE 7000
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
CMD ["serve"]
