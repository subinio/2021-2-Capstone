
const msgerChat = get(".msger-chat");

const BOT_IMG = "../static/images/chatbot.png";
const PERSON_IMG = "../static/images/maskperson.png";
const BOT_NAME = "BOT";
const PERSON_NAME = "{{user.first_name}}님";


function myRecord() {
  document.getElementById("record").style.display = "none";
  document.getElementById("stop").style.display = "";

  $.ajax({ // ajax로 서버와 통신
      type: "GET", // 데이터를 전송하는 방법
      url: "/chat", // 통신할 url을 지정
      data: {'what': "record"},
      dataType: "json",
      success: function (data) { // 성공
          console.log("recording...");
      },
      error: function (request, status, error) { // 실패

      },
  });
}

function myStop() {
  document.getElementById("record").style.display = "";
  document.getElementById("stop").style.display = "none";

  $.ajax({ // ajax로 서버와 통신
      type: "GET", // 데이터를 전송하는 방법
      url: "/chat", // 통신할 url을 지정
      data: {'what': "stop"},
      dataType: "json",
      success: function (data) { // 성공
        console.log("stop recording");
        
        const msgText = data['text'];
        appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
        botResponse();
      },
      error: function (request, status, error) { // 실패

      },
  });


}

function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function botResponse() {
  const msgText = "그랬구나 어쩌구 저쩌구";
  const delay = msgText.split(" ").length * 100;
  
  var audio = new Audio("../static/happy.wav");
  audio.play();

  setTimeout(() => {
    appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
  }, delay);
}


// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}


