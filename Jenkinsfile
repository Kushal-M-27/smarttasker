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
                bat '"C:\\Python312\\python.exe" -m bandit -r app || exit 0'
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

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Please check errors above.'
        }
        always {
            echo '🧹 Final cleanup if required.'
        }
    }
}
