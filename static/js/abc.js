function checksymp() {
  upper = document.getElementById('user_input').value;
  upper = upper.toUpperCase();
  if(upper === 'COUGH'){
    document.getElementById('display').innerHTML = 'You may have COMMON COLD <br> You may have ASTHMA';
  }if(upper === 'FEVER'){
    document.getElementById('display').innerHTML = '<br> You may have VIRAL Infection';
  }if(upper === 'THROAT IRRITATION'){
    document.getElementById('display').innerHTML = '<br> You may have TONSILLITIS';
  }else{
    document.getElementById('display').innerHTML = 'Wrong input'
  }
};
