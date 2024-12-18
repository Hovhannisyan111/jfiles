pipeline {
	agent any

	stages {
		stage("Using maxtrix") {
			matrix {
				axes {
					axis {
						name "PLATFORM"
						values "linux", "macos", "windows" 	
					}
					axis {
						name "PY_VERSION"
						values "2", "3", "3.9"
					}
				}
				excludes {
					exclude {
						axis {
							name "PLATFORM"
							values "macos"
						}
						axis {
							name "PY_VERSION"
							values "2"
						}
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
