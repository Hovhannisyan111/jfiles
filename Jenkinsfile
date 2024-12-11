def gv

pipeline {
	agent any
	triggers {
		githubPush()
	}
	stages {
		stage("Build") {
			steps {
				script {
					gv = load "script.groovy"
				}
			}
		}
	}	
}
