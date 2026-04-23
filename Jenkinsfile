pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t viratsonawane/my-flask-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm viratsonawane/my-flask-app:latest pytest test_app.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // This pulls the tool we just installed
                    def scannerHome = tool 'sonar-scanner'
                    // This uses the server we configured
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=studypath-api -Dsonar.sources=."
                    }
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'docker push viratsonawane/my-flask-app:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl rollout restart deployment studypath-api-deployment'
                sh 'kubectl get pods'
            }
        }
    }
}