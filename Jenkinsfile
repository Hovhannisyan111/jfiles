pipeline {
	agent any

	stages {
		stage("Tests") {
			parallel {
				stage("Unit test") {
					steps {
						echo "Runnning unit tests..."
					}
				}
				stage("Integration test"){
					steps {
						echo "Running Integration test..."
						sh "exit 1"
					}
				}
			}
		}
		stage("Build") {
			steps {
				echo "Building APP"
			}
		}
	}
}
