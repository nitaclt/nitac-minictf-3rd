FROM ruby:2.7-alpine

RUN apk update && apk upgrade
RUN apk add build-base sqlite sqlite-libs sqlite-dev

COPY akhan /app
WORKDIR /app
RUN bundle install

EXPOSE 80

# ENTRYPOINT ["sh", "./startup.sh"]
ENTRYPOINT ["ruby", "app.rb", "-p", "80", "-o", "0.0.0.0"]
