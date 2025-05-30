pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                echo "Current branch: ${env.BRANCH_NAME}"
                sh 'pip install -r lesson_28/hw_28/requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest lesson_28/hw_28/tests --maxfail=1 --disable-warnings -v'
            }
        }
    }
}