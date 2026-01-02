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
                    url: 'https://github.com/bhargavich-98/sauce_demo.git'
            }
        }

        stage('Setup, Install, Run Tests') {
            steps {
                bat """
                    python --version

                    REM Create virtual environment
                    python -m venv %VENV_DIR%

                    REM Activate venv
                    call %VENV_DIR%\\Scripts\\activate

                    REM Upgrade pip
                    pip install --upgrade pip

                    REM Install project dependencies
                    pip install -r requirements.txt

                    REM Run pytest with JUnit XML report
                    pytest --junitxml=reports/results.xml --disable-warnings --maxfail=1 -q
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/screenshots/*.png', allowEmptyArchive: true
            junit 'reports/results.xml'
        }
    }
}