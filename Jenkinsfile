pipeline{
	agent any
	
	stages {
		stage('Checkout') {
			steps {
				echo "Checking out source code..."
				checkout scm
			}
		}

		stage("Run script") {
			steps {
				echo "Running python script"
				sh "python3 main.py"
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
