pipeline{
	agent any

	environment {
		ARTIFACT_DIR = "build/artifacts"
	}
	
	stages {
		stage('Checkout') {
			steps {
				echo "Checking out source code..."
				checkout scm
			}
		}

		stage("Run script") {
			steps {
				script {
					sh "bash build.sh"
				}
			}
		}

		stage("Archive artifact") {
			steps {
				echo "Arachiving the script output..."
				archiveArtifacts artifacts: "output.log", fingerprint: true
			}
		}
	}

	post {
		success {
			echo "Pipeline compieted successfully!"
		}
		failure {
			echo "Pipline failed!"
		}
	}
}
