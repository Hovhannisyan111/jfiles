pipeline {
	agent any
	triggers {
		githubPush()
	}
	stages {
		stage('Checkout') {
			steps {
				echo 'Cheking out code...'
			}
		}

		stage('Build') {
			steps {
				echo 'Building the application...'
			}
		}
		
		stage('Deploy') {
			steps {
				echo 'deploying the application...'
			}
		}
	}

	post {
		success {
			echo 'Build is succeeded'
		}
		failure {
			echo 'Build is failed'
		}
	}
}
