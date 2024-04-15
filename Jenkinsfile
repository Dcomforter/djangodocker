pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Dcomforter/djangodocker.git'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}