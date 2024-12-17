pipeline {
    agent any

    environment {
        DEPLOY_ENV = BRANCH_NAME == 'main' ? 'Production' : 'Staging'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out branch: ${BRANCH_NAME}"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building project for branch: ${BRANCH_NAME}"
                sh './gradlew clean build' // Replace with your build command
            }
        }

        stage('Test') {
            steps {
                echo "Running tests for branch: ${BRANCH_NAME}"
                sh './gradlew test' // Replace with your test command
            }
        }

        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch 'dev'
                }
            }
            steps {
                echo "Deploying to ${DEPLOY_ENV} environment..."
                script {
                    if (DEPLOY_ENV == 'Production') {
                        sh './deploy-prod.sh' // Replace with your production deployment script
                    } else {
                        sh './deploy-staging.sh' // Replace with your staging deployment script
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Build succeeded for branch: ${BRANCH_NAME}"
        }
        failure {
            echo "Build failed for branch: ${BRANCH_NAME}"
        }
    }
}
