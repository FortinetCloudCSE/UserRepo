void setBuildStatus(String message, String state, String repo_url) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: repo_url],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

pipeline {
    agent any

    stages {

       stage('Checking for question/discussion section in content folders'){
            when { expression { false } }
            steps {
              script {
                def warningFound = false
                try {
                  sh '''
                  for dir in content/*/; do
                    found=false
                    for file in "$dir"/*; do
                      if grep -qiE 'discussion|questions|q&a' "$file" >/dev/null 2>&1; then
                        found=true
                        break
                      fi
                    done
                    if [ "$found" == "true" ]; then
                      echo "$dir: relevant section found"
                    else
                      echo "$dir: sections not found"
                      warningFound=true
                    fi
                  done
                  if [ "$warningFound" == "true" ]; then
                    echo "Warning: some content directories did not contain any files with a discussion/questions/q&a section."
                  fi
                  '''
                } catch (Exception e) {
                   echo "An error occurred: ${e.message}"
                }
              }
            }
       }
    }
    post {
     success {
        setBuildStatus("Build succeeded", "SUCCESS", "${GIT_URL}");
     }
     failure {
        setBuildStatus("Build failed", "FAILURE", "${GIT_URL}");
     }
  }
}
