pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        CHROME_DRIVER_ZIP = "chromedriver.zip"
        CHROME_DRIVER_EXE = "chromedriver.exe"
        PYTHON = "python"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/bhargavich-98/sauce_demo.git', branch: 'main'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                ${env.PYTHON} -m venv ${env.VENV_DIR}
                call ${env.VENV_DIR}\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Install Chrome') {
            steps {
                bat """
                IF NOT EXIST "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" (
                    powershell -Command "Start-Process 'https://dl.google.com/chrome/install/375.126/chrome_installer.exe' -Wait"
                )
                """
            }
        }

        stage('Install ChromeDriver') {
            steps {
                bat """
                powershell -Command "Invoke-WebRequest -Uri https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip -OutFile ${env.CHROME_DRIVER_ZIP}"
                powershell -Command "Expand-Archive -Force -Path ${env.CHROME_DRIVER_ZIP} -DestinationPath ."
                """
            }
        }

        stage('Run Pytest Tests') {
            steps {
                bat """
                call ${env.VENV_DIR}\\Scripts\\activate.bat
                pytest --html=report.html --self-contained-html
                """
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'CI Pipeline completed.'
        }
        success {
            echo 'Tests passed successfully.'
        }
        failure {
            echo 'Tests failed. Screenshots and logs archived for debugging.'
        }
    }
}
