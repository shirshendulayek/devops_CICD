{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 pipeline \{\
    agent any\
    environment \{\
        DOCKER_IMAGE = "flask-app-local"\
    \}\
    stages \{\
        stage('Checkout') \{\
            steps \{\
                checkout scm\
            \}\
        \}\
        stage('Build Image') \{\
            steps \{\
                sh "docker build -t $\{DOCKER_IMAGE\} ."\
            \}\
        \}\
        stage('Deploy Local') \{\
            steps \{\
                // Stop and remove old container if it exists\
                sh "docker stop flask-container || true && docker rm flask-container || true"\
                // Run new container\
                sh "docker run -d -p 5000:5000 --name flask-container $\{DOCKER_IMAGE\}"\
            \}\
        \}\
    \}\
\}}