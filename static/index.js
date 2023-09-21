document.addEventListener("keypress", function (e) {
  if (e.keyCode === 13 || e.which === 13) {
    e.preventDefault();
    return false;
  }
});

function formValidate() {
  cansubmit = true;
  var f = document.forms["form_data"].elements;

  for (var i = 0; i < f.length; i++) {
    if (f[i].value.length == 0) {
      cansubmit = false;
    }
  };
  if (cansubmit) {
    document.getElementById("save").disabled = !cansubmit;
  } else {
    document.getElementById("save").disabled = true;
    document.getElementById("start").disabled = true;
  };

  std = document.getElementById('start_delay');
  etd = document.getElementById('end_delay');

  if (parseInt(std.value) >= parseInt(etd.value)) {
    document.getElementById("save").disabled = true;
    document.getElementById('stdetd').innerHTML = 'Start Delay value cannot be equal or more than End Delay value';
  }
  else {
    document.getElementById('stdetd').innerHTML = ''
  };

};

function formF() {  //load config values to its respective inputs
  var f = document.forms["form_data"].elements;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", '/receive', true)
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("type", "config")
  var cap_key = document.getElementById("cap_key");
  var owners = document.getElementById("owners");
  var server_id = document.getElementById("server_id");
  var server_role_id = document.getElementById("server_role_id");
  var log_channel_id = document.getElementById("log_channel_id");
  var unci = document.getElementById("unci");
  var mcsci = document.getElementById("mcsci");
  var start_delay = document.getElementById("start_delay");
  var end_delay = document.getElementById("end_delay");
  var startoxyminers = document.getElementById("startoxyminers");
  var stopoxyminers = document.getElementById("stopoxyminers");
  var start_each = document.getElementById("start_each");
  var stop_each = document.getElementById("stop_each");
  var dm_uwu = document.getElementById("dm_uwu");
  var invoke_cmd = document.getElementById("invoke_cmd");
  var miner_no = document.getElementById('minernos')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var data = JSON.parse(xhr.responseText)['data'];
      cap_key.value = data['captcha_key']
      owners.value = data['owners']
      server_id.value = data['server_id']
      server_role_id.value = data['server_role_id']
      log_channel_id.value = data['log_channel_id']
      unci.value = data['unci']
      mcsci.value = data['mcsci']
      start_delay.value = data['start_delay']
      end_delay.value = data['end_delay']
      startoxyminers.value = data['startoxyminers']
      stopoxyminers.value = data['stopoxyminers']
      start_each.value = data['start_each']
      stop_each.value = data['stop_each']
      dm_uwu.value = data['dm_uwu']
      invoke_cmd.value = data['invoke_cmd']
      miner_no.value = data['miner_no']
    }
  }
  xhr.send(null);
}

function postValue() { //save config
  document.getElementById('start').disabled = false; //post value when save button clicked, start btn active
  var cap_key = document.getElementById("cap_key");
  var owners = document.getElementById("owners");
  var server_id = document.getElementById("server_id");
  var server_role_id = document.getElementById("server_role_id");
  var log_channel_id = document.getElementById("log_channel_id");
  var unci = document.getElementById("unci");
  var mcsci = document.getElementById("mcsci");
  var start_delay = document.getElementById("start_delay");
  var end_delay = document.getElementById("end_delay");
  var startoxyminers = document.getElementById("startoxyminers");
  var stopoxyminers = document.getElementById("stopoxyminers");
  var start_each = document.getElementById("start_each");
  var stop_each = document.getElementById("stop_each");
  var dm_uwu = document.getElementById("dm_uwu");
  var invoke_cmd = document.getElementById("invoke_cmd");
  var miner_no = document.getElementById('minernos')
  jsonm = {
    data: {
      miner_no: miner_no.value,
      captcha_key: cap_key.value,
      owners: owners.value,
      server_id: server_id.value,
      server_role_id: server_role_id.value,
      log_channel_id: log_channel_id.value,
      unci: unci.value,
      mcsci: mcsci.value,
      start_delay: start_delay.value,
      end_delay: end_delay.value,
      startoxyminers: startoxyminers.value,
      stopoxyminers: stopoxyminers.value,
      start_each: start_each.value,
      stop_each: stop_each.value,
      dm_uwu: dm_uwu.value,
      invoke_cmd: invoke_cmd.value,
    },
  };
  var xhr = new XMLHttpRequest();
  var url = "/receive";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("type", "json")
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var json = JSON.parse(xhr.responseText);
    };
  };
  xhr.send(JSON.stringify(jsonm))
};

function submitV() { //start miners
  var xhr = new XMLHttpRequest();
  var url = "/signal";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ "number": parseInt(document.getElementById('minernos').value), "type": 2 }));
  document.getElementById('start').style.display = 'none';
  document.getElementById('save').style.display = 'none';
  document.getElementById('stop').style.display = 'block';
}

function stopV() { //stop miners
  document.getElementById('terminal_hello').innerHTML = 'KILLED - Please restart the application';
  document.getElementById('terminal_hello').disabled = true;
  document.getElementById('stop').innerHTML = 'KILLED'
  var xhr = new XMLHttpRequest();
  var url = '/signal'
  xhr.open('POST', url, true)
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({ "type": 1 }))
}


function UploadToken(event) {
  const reader = new FileReader()
  reader.onload = function handleFileLoad(event) {
    text = event.target.result
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_file', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("type", "token");
    text = (event.target.result);
    lines = text.split('\n')
    obj = {}
    for (line = 0; line < lines.length; line++) {
      tk = (lines[line].replace(/(\r\n|\n|\r)/gm, ""));
      Object.assign(obj, { [line.toString()]: tk })
    }

    xhr.send(JSON.stringify(obj));
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        if (myArr['status']) {
          document.getElementById('s_t').innerHTML = "Success";
          document.getElementById('s_t').style.color = 'green';
          document.getElementById('terminal_hello').innerHTML = "Tokens Uploaded: " + event.target.result + "\n";
        }
        else {
          document.getElementById('s_t').innerHTML = "Failed";
        }
      }
    };
  }
  reader.readAsText(event.target.files[0])
}

function UploadChannel(event) {
  const reader = new FileReader()
  reader.onload = function handleFileLoad(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_file', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("type", "channel");
    text = (event.target.result);
    lines = text.split('\n');
    obj = {}
    for (line = 0; line < lines.length; line++) {
      tk = (lines[line].replace(/(\r\n|\n|\r)/gm, ""));
      Object.assign(obj, { [line.toString()]: tk })
    }
    xhr.send(JSON.stringify(obj))
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        if (myArr['status']) {
          document.getElementById('s_c').innerHTML = "Success";
          document.getElementById('s_c').style.color = 'green'
          document.getElementById('terminal_hello').innerHTML = "Channel list Uploaded: " + "\n" + event.target.result + "\n";
        }
        else {
          document.getElementById('s_c').innerHTML = "Failed";
        }
      }
    };
  }
  reader.readAsText(event.target.files[0])

}

function UploadCommands(event) {
  const reader = new FileReader()
  reader.onload = function handleFileLoad(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_file', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("type", "commands");
    text = (event.target.result);
    lines = text.split('\n')
    objj = { "commands": [] }
    for (l = 0; l < lines.length; l++) {
      remove_r = (lines[l].replace(/(\r\n|\n|\r)/gm, ""));
      objj['commands'].push(remove_r);
    };
    xhr.send(JSON.stringify(objj));
    xhr.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        if (myArr['status']) {
          document.getElementById('s_f').innerHTML = "Success";
          document.getElementById('s_f').style.color = 'green'
          document.getElementById('terminal_hello').innerHTML = "Commands List Uploaded: " + "\n" + event.target.result + "\n";
        }
        else {
          document.getElementById('s_f').innerHTML = "Failed";
        }
      }
    };

  }
  reader.readAsText(event.target.files[0])

}

function x() {
  document.getElementById('UploadToken').addEventListener('change', UploadToken, false);
  document.getElementById('UploadChannel').addEventListener('change', UploadChannel, false);
  document.getElementById('UploadCommands').addEventListener('change', UploadCommands, false);
}


function running() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/status", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      statust = JSON.parse(xhr.responseText);
      if (statust['status'] == false) {
        document.getElementById('save').style.display = 'block';
        document.getElementById('start').style.display = 'block';
      }
      else {
        document.getElementById('stop').style.display = 'block';
        document.getElementById('save').style.display = 'none';
        document.getElementById('start').style.display = 'none';
      }
    };
  };
  xhr.send(null);
};


function receiveLog() {
  var xhr = new XMLHttpRequest();
  url = '/logs'
  xhr.open('GET', url, true)
  xhr.setRequestHeader("Content-Type", "multipart/form-data");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      text = xhr.responseText;
      document.getElementById('terminal_hello').innerHTML = text
    };
  };
  xhr.send(null)
};

setInterval(receiveLog, 5000);