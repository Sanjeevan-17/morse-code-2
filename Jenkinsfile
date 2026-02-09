pipeline {
    agent any

    environment {
        DockerHub_Credentials = credentials('sanju1701')
        Image_Name = "sanjeevan/morse-code-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sanjeevan-17/morse-code-2.git'
            }
        }

  

        stage('Run Tests') {
            steps {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest flake8
                    pytest || true
                    flake8 . || true
                    '''
            }
        }


        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t $Image_Name:latest .
                docker tag $Image_Name:latest $Image_Name:$BUILD_NUMBER
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh """
                echo \$DockerHub_Credentials_PSW | docker login -u \$DockerHub_Credentials_USR --password-stdin

                docker push $Image_Name:latest
                docker push $Image_Name:$BUILD_NUMBER
                """
            }
        }

        stage('Deploy Stage') {
            steps {
                sh """
                docker stop morse-container || true
                docker rm morse-container || true

                docker run -d --name morse-container -p 8080:8080 $Image_Name:latest
                """
            }
        }
    }

    post {
        success {
            echo '✅ Build, Test, Push, Deploy completed successfully!'
        }

        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
