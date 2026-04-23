pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // This tells Jenkins to pull your latest code from GitHub
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Jenkins builds the new Docker image using your Dockerfile
                sh 'docker build -t viratsonawane/my-flask-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                // Jenkins runs your pytest script INSIDE the newly built container!
                // If the test fails, the pipeline turns red and stops here.
                sh 'docker run --rm viratsonawane/my-flask-app:latest pytest test_app.py'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // If the tests pass, Jenkins uploads the verified image to the internet
                sh 'docker push viratsonawane/my-flask-app:latest'
            }
        }
    }
}