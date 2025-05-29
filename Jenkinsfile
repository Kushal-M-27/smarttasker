pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Run SonarQube scanner here'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'bandit -r app'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d --build'
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
