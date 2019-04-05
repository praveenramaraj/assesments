node {
   stage('Preparation') { // for display purposes
      // Get some code from a GitHub repository
      git 'https://github.com/praveenramaraj/assesments.git'
      
   }
   stage('input1') {
      // Run ip_print with input1

     echo 'Executing ip_print with input1'
     sh './ip_print.py --json input1.json'
   }
   stage('input2') {
      // Run ip_print with input2
      
     echo 'Executing ip_print with input1'
     sh './ip_print.py --json input2.json'
   }
}
