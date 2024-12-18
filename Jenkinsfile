pipeline {
	agent any

	stages {
		stage("Using maxtrix") {
			matrix {
				axes {
					axis {
						name "PLATFORM"
						values "linux", "macos"	
					}
					axis {
						name "PY_VERSION"
						values "2", "3", "3.9"
					}
				}
				stages {
					stage("Print") {
						steps{
							echo "Running on ${PLATFORM} with Python ${PY_VERSION}"
						}
					}
				}
			}			
		}
	}
}
