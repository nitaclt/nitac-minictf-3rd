#!/bin/sh

ruby app.rb -p 80 -o 0.0.0.0 &
node crawler.js &
