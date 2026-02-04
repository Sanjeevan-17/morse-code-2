pipeline {
    agent any

    environment {
        DockerHub_Credentials = credentials('sanju1701')
        Image_Name = "sanjeevan/morse-code-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/Sanjeevan-17/morse-code-2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 . || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $Image_Name:$BUILD_NUMBER ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                echo \$DockerHub_Credentials_PSW | docker login -u \$DockerHub_Credentials_USR --password-stdin
                docker push $Image_Name:$BUILD_NUMBER
                """
            }
        }

        stage('Deploy Stage') {
            steps {
                sh "docker run -d -p 8080:8080 $Image_Name:$BUILD_NUMBER"
            }
        }
    }

    post {
        success {
            echo 'Build, Test, Deploy completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
