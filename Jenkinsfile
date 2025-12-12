pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.13"
        VENV_DIR = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/bhargavich-98/sauce_demo.git', branch: 'main'
            }
        }

        stage('Set up Python') {
            steps {
                sh """
                    python --version
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    pytest --disable-warnings --maxfail=1 -q
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/screenshots/*.png', allowEmptyArchive: true
            junit '**/reports/*.xml'
        }
    }
}