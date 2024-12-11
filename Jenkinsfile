pipeline {
	agent any
	triggers {
		githubPush()
	}
	stages {
		stage("Checkout") {
			steps {
				echo "Checking out code..."
				checkout scm
			}
		}
	}	
}
