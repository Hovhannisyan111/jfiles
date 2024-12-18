pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Simulate a build step (e.g., running a build tool like Maven or Gradle)
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    // Simulate running tests and capturing results
                    def testResult = false // Simulate test failure
                    if (!testResult) {
                        currentBuild.result = 'UNSTABLE' // Mark build as unstable
                        echo 'Some tests failed, marking the build as unstable.'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Deployment logic
            }
        }
    }
    post {
        always {
            script {
                if (currentBuild.result == 'UNSTABLE') {
                    echo 'Build marked as UNSTABLE.'
                } else {
                    echo 'Build completed successfully.'
                }
            }
        }
    }
}

