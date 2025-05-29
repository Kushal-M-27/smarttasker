pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover tests'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Run SonarQube scanner here'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'bandit -r app'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose up -d --build'
            }
        }

        stage('Release') {
            when {
                branch 'main'
            }
            steps {
                echo 'Release to production simulated'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring available at /metrics'
            }
        }
    }
}
