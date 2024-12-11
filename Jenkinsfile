pipeline {
	agent {
		docker {
			image 'python:3.10'
		}
	}
	
	environment {
		PYTHONUNBUFFERED = 1
	}
	
	stages {
		stage('Clone repo') {
			steps {
				git 'https://github.com/Hovhannisyan111/jfiles.git'
			}
		}

		stage('Install deps') {
			steps {
				sh 'pip install -r requirements.txt'
			}
		}
		
		stage('Run test') {
			steps {
				sh 'pytest --junitxml=report.xml'
			}
			post{
				always {
					junit 'report.xml'
				}
			}
		}
	}

	post {
		always {
			cleanWs()
		}
	}
}
