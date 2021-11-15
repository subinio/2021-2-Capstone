/*=========================================
=====전화번호 포맷 자동 생성
=====================================*/

var autoHypenPhone = function(str){
  str = str.replace(/[^0-9]/g, '');
  var tmp = '';
  if( str.length < 4){
      return str;
  }else if(str.length < 7){
      tmp += str.substr(0, 3);
      tmp += '-';
      tmp += str.substr(3);
      return tmp;
  }else if(str.length < 11){
      tmp += str.substr(0, 3);
      tmp += '-';
      tmp += str.substr(3, 3);
      tmp += '-';
      tmp += str.substr(6);
      return tmp;
  }else{              
      tmp += str.substr(0, 3);
      tmp += '-';
      tmp += str.substr(3, 4);
      tmp += '-';
      tmp += str.substr(7);
      return tmp;
  }

  return str;
}


var phoneNum = document.getElementById('phoneNum');

phoneNum.onkeyup = function(){
console.log(this.value); 
this.value = autoHypenPhone( this.value ) ;  
}


/*=========================================
===== 의료진, 격리자 선택
=====================================*/

$("input:radio[name=who]").click(function(){      
  if($("input:radio[name=who]:checked").val()=='doctor'){
      $("#forPatient").css({'display': 'none'})  
      $("#forDoctor").css({'display': ''})       //show
      $("input").val(function() {
        return this.defaultValue;
      });
  }
  else if($("input:radio[name=who]:checked").val()=='patient'){
      $("#forPatient").css({'display': ''})     //show
      $("#forDoctor").css({'display': 'none'}) 
      $("input").val(function() {
        return this.defaultValue;
      });
  }
});



/*=========================================
===== 기관 선택
=====================================*/

function cityCategory() {
  var js_dict = inst_dict.replace(/\'/gi, "\"");
  js_dict = JSON.parse(js_dict);

  if(document.querySelector('input[name="who"]:checked').value == "patient"){
    var target = document.getElementById("inst_city1");
  }
  else{
    var target = document.getElementById("inst_city2");
  }

  // target.options.length = 1;

  var cities = Object.keys(js_dict)
  for (i in cities) {
		var opt = document.createElement("option");
		opt.value = cities[i];
		opt.innerHTML = cities[i];
		target.appendChild(opt);
	}	
  
}


function centerCategory(e) {
  var js_dict = inst_dict.replace(/\'/gi, "\"");
  js_dict = JSON.parse(js_dict);

  if(document.querySelector('input[name="who"]:checked').value == "patient"){
    var target = document.getElementById("inst_center1");
  }
  else{
    var target = document.getElementById("inst_center2");
  }

  target.options.length = 1;
  
  var centers = js_dict[e.value];

  console.log(centers);

	for (i in centers) {
		var opt = document.createElement("option");
		opt.value = centers[i];
		opt.innerHTML = centers[i];
		target.appendChild(opt);
	}	
}


