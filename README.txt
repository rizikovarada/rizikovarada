=== rizikovarada bot ===
this bot has limited functionality, but it's fully sufficient. it also includes a Dockerfile that runs on the server. the installation and startup instructions are very simple and can be launched almost anywhere.

=== startup ===
to start, you need the Dockerfile if you're using Docker, or python 3 if running it directly with python.

if using Docker, here's the instruction ->
docker build -t rizikovarada .
docker run -d rizikovarada

if running directly with Python ->
pip install -r requirements.txt
python run.py


=== license ===
license: apache-license-2.0
author: risknu  

copyright (c) risknu 2024
