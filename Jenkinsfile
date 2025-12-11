pipeline {
    agent {
        label 'linux'   // Use a Linux Jenkins agent
    }

    environment {
        PYTHON_ENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv ${PYTHON_ENV}
                    . ${PYTHON_ENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Chrome and ChromeDriver') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y wget unzip

                    # Install Google Chrome
                    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                    sudo apt install -y ./google-chrome-stable_current_amd64.deb

                    # Install ChromeDriver (version matches installed Chrome)
                    CHROME_VERSION=$(google-chrome --version | sed 's/Google Chrome //; s/ .*//')
                    CHROME_MAJOR=$(echo $CHROME_VERSION | cut -d '.' -f 1)

                    DRIVER_URL=$(wget -qO- https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json \
                        | jq -r ".milestones.\"$CHROME_MAJOR\".downloads.chromedriver[0].url")

                    wget "$DRIVER_URL" -O chromedriver.zip
                    unzip chromedriver.zip -d chromedriver_folder
                    sudo mv chromedriver_folder/chromedriver-linux64/chromedriver /usr/local/bin/
                    sudo chmod +x /usr/local/bin/chromedriver
                '''
            }
        }

        stage('Run Pytest Tests') {
            steps {
                sh '''
                    . ${PYTHON_ENV}/bin/activate
                    pytest --html=reports/test_report.html --self-contained-html
                '''
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
