pipeline {
    agent any  // Run on any available agent (Windows)

    environment {
        PYTHON_ENV = "venv"
        CHROME_INSTALL_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        CHROMEDRIVER_PATH = "C:\\chromedriver\\chromedriver.exe"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                    python -m venv %PYTHON_ENV%
                    call %PYTHON_ENV%\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Install Chrome') {
            steps {
                bat """
                    REM Install Google Chrome if not installed
                    IF NOT EXIST "%CHROME_INSTALL_PATH%" (
                        powershell -Command "Start-Process 'https://dl.google.com/chrome/install/375.126/chrome_installer.exe' -Wait"
                    )
                """
            }
        }

        stage('Install ChromeDriver') {
            steps {
                bat """
                    REM Create folder for chromedriver
                    if not exist C:\\chromedriver mkdir C:\\chromedriver

                    REM Download ChromeDriver matching installed Chrome version
                    powershell -Command "\
                        $chrome = Get-Item '%CHROME_INSTALL_PATH%'; \
                        $version = (& $chrome --version).Split(' ')[2]; \
                        $major = $version.Split('.')[0]; \
                        Invoke-WebRequest https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$major -OutFile C:\\chromedriver\\version.txt; \
                        $driver_version = Get-Content C:\\chromedriver\\version.txt; \
                        Invoke-WebRequest https://chromedriver.storage.googleapis.com/$driver_version/chromedriver_win32.zip -OutFile C:\\chromedriver\\chromedriver.zip; \
                        Expand-Archive C:\\chromedriver\\chromedriver.zip -DestinationPath C:\\chromedriver; \
                    "
                """
            }
        }

        stage('Run Pytest Tests') {
            steps {
                bat """
                    call %PYTHON_ENV%\\Scripts\\activate.bat
                    pytest --html=reports\\test_report.html --self-contained-html
                """
            }
            post {
                always {
                    echo "Tests finished. Proceeding to archive artifacts."
                }
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'reports/**/*.html', allowEmptyArchive: true
                archiveArtifacts artifacts: 'reports/screenshots/**/*.png', allowEmptyArchive: true
                archiveArtifacts artifacts: 'reports/logs/**/*.log', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo "CI Pipeline completed."
        }
        failure {
            echo "Tests failed. Screenshots and logs archived for debugging."
        }
    }
}
