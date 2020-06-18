
document.addEventListener("DOMContentLoaded", function(){
	function myFunction1(e){
		console.log(2)
		console.log(e.target)
		e.setAttribute("value", e.value);
	}
    var rightcard = false;
    var tempblock;
    var tempblock2;
    document.getElementById("blocklist").innerHTML = '<div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="python"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/eye.svg"></div><div class="blocktext">                        <p class="blocktitle">Python</p><p class="blockdesc">Select Python Component</p> </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="matillion"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/action.svg"></div><div class="blocktext">                        <p class="blocktitle">Matillion</p><p class="blockdesc">Select Matillion Component</p></div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="talend"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/time.svg"></div><div class="blocktext">                        <p class="blocktitle">Talend</p><p class="blockdesc">Select Talend Component</p>          </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="4"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/error.svg"></div><div class="blocktext">                        <p class="blocktitle">Error prompt</p><p class="blockdesc">Triggers when a specified error happens</p>              </div></div></div>';
    flowy(document.getElementById("canvas"), drag, release, snapping);
    function addEventListenerMulti(type, listener, capture, selector) {
        var nodes = document.querySelectorAll(selector);
        for (var i = 0; i < nodes.length; i++) {
            nodes[i].addEventListener(type, listener, capture);
        }
    }
    function snapping(drag, first) {
        var grab = drag.querySelector(".grabme");
        grab.parentNode.removeChild(grab);
        var blockin = drag.querySelector(".blockin");
        blockin.parentNode.removeChild(blockin);
        if (drag.querySelector(".blockelemtype").value == "python") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/eyeblue.svg'><p class='blockyname'>Python</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><label for='pythonfile'>Python File:</label><input class='' onblur='myFunction1(this)' type='pythonfile' value='e' placeholder='' name='pythonfile'>";
        } else if (drag.querySelector(".blockelemtype").value == "talend") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/actionblue.svg'><p class='blockyname'>Talend</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div></div><label for='TalendEndpoint'>Endpoint:</label><input onblur='myFunction1(this)' type='TalendEndpoint' id='TalendEndpoint' placeholder='' name='TalendEndpoint'>";
			
        } else if (drag.querySelector(".blockelemtype").value == "matillion") {
		drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/timeblue.svg'><p class='blockyname'>Matillion</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div> <div  id='matillion_detail'><label  style='display: none;width:32%;float:left;padding:1px' for='Server'>Server IP:</label><input onblur='myFunction1(this)' value='ip' class='test'  style='display: none;width:65%;float:right' type='ServerIP' id='ServerIP' placeholder='' name='Server'><label style='display: none;width:32%;float:left;padding:1px' for='GroupName'>GroupName:</label> <input onblur='myFunction1(this)' style='display: none;width:65%;float:right' type='GroupName' id='GroupName' placeholder='' name='GroupName'><label style='display: none;width:32%;float:left;padding:1px' for='ProjectName'>ProjectName:</label><input onblur='myFunction1(this)' style='display: none;width:65%;float:right' type='ProjectName' id='ProjectName' placeholder='' name='ProjectName'><label style='display: none;width:32%;float:left; padding: 2px;'  for='Version'>Version:</label><input onblur='myFunction1(this)' style='display: none;width:65%;float:right'  type='Version' id='Version' placeholder='' name='Version'><label style='width:32%;float:left;padding:1px' for='JobName'>JobName:</label><input onblur='myFunction1(this)' style='width:65%;float:right' type='JobName' id='JobName' placeholder='' name='JobName'><label style='display: none;width:32%;float:left;padding:1px' for='Environment'>Environment:</label><input onblur='myFunction1(this)' style='display: none;width:65%;float:right' type='Environment' id='Environment' placeholder='' name='Environment'></div>";
        } else if (drag.querySelector(".blockelemtype").value == "4") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/errorblue.svg'><p class='blockyname'>Error prompt</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>When <span>Error 1</span> is triggered</div>";
        } else if (drag.querySelector(".blockelemtype").value == "5") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/databaseorange.svg'><p class='blockyname'>New database entry</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Add <span>Data object</span> to <span>Database 1</span></div>";
        } else if (drag.querySelector(".blockelemtype").value == "6") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/databaseorange.svg'><p class='blockyname'>Update database</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Update <span>Database 1</span></div>";
        } else if (drag.querySelector(".blockelemtype").value == "7") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/actionorange.svg'><p class='blockyname'>Perform an action</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Perform <span>Action 1</span></div>";
        } else if (drag.querySelector(".blockelemtype").value == "8") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/twitterorange.svg'><p class='blockyname'>Make a tweet</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Tweet <span>Query 1</span> with the account <span>@alyssaxuu</span></div>";
        } else if (drag.querySelector(".blockelemtype").value == "9") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/logred.svg'><p class='blockyname'>Add new log entry</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Add new <span>success</span> log entry</div>";
        } else if (drag.querySelector(".blockelemtype").value == "10") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/logred.svg'><p class='blockyname'>Update logs</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Edit <span>Log Entry 1</span></div>";
        } else if (drag.querySelector(".blockelemtype").value == "11") {
            drag.innerHTML += "<div class='blockyleft'><img src='/static/assets/errorred.svg'><p class='blockyname'>Prompt an error</p></div><div class='blockyright'><img src='/static/assets/more.svg'></div><div class='blockydiv'></div><div class='blockyinfo'>Trigger <span>Error 1</span></div>";
        }
        return true;
    }
    function drag(block) {
        block.classList.add("blockdisabled");
        tempblock2 = block;
    }
    function release() {
        if (tempblock2) {
            tempblock2.classList.remove("blockdisabled");
        }
    }
    var disabledClick = function(){
        document.querySelector(".navactive").classList.add("navdisabled");
        document.querySelector(".navactive").classList.remove("navactive");
        this.classList.add("navactive");
        this.classList.remove("navdisabled");
        if (this.getAttribute("id") == "triggers") {
            document.getElementById("blocklist").innerHTML = '<div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="python"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/eye.svg"></div><div class="blocktext">                        <p class="blocktitle">Python</p><p class="blockdesc">Select Python Component</p>       </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="matillion"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/action.svg"></div><div class="blocktext">                        <p class="blocktitle">Matillion</p><p class="blockdesc">SelectSelect Matillion Component</p></div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="talend"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/time.svg"></div><div class="blocktext">                        <p class="blocktitle">Talend</p><p class="blockdesc">Select Talend Component</p>          </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="4"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                    <div class="blockico"><span></span><img src="/static/assets/error.svg"></div><div class="blocktext">                        <p class="blocktitle">Error prompt</p><p class="blockdesc">Triggers when a specified error happens</p>              </div></div></div>';
        } else if (this.getAttribute("id") == "actions") {
            document.getElementById("blocklist").innerHTML = '<div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="5"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/database.svg"></div><div class="blocktext">                        <p class="blocktitle">New database entry</p><p class="blockdesc">Adds a new entry to a specified database</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="6"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/database.svg"></div><div class="blocktext">                        <p class="blocktitle">Update database</p><p class="blockdesc">Edits and deletes database entries and properties</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="7"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/action.svg"></div><div class="blocktext">                        <p class="blocktitle">Perform an action</p><p class="blockdesc">Performs or edits a specified action</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="8"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/twitter.svg"></div><div class="blocktext">                        <p class="blocktitle">Make a tweet</p><p class="blockdesc">Makes a tweet with a specified query</p>        </div></div></div>';
        } else if (this.getAttribute("id") == "loggers") {
            document.getElementById("blocklist").innerHTML = '<div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="9"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/log.svg"></div><div class="blocktext">                        <p class="blocktitle">Add new log entry</p><p class="blockdesc">Adds a new log entry to this project</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="10"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/log.svg"></div><div class="blocktext">                        <p class="blocktitle">Update logs</p><p class="blockdesc">Edits and deletes log entries in this project</p>        </div></div></div><div class="blockelem create-flowy noselect"><input type="hidden" name="blockelemtype" class="blockelemtype" value="11"><div class="grabme"><img src="/static/assets/grabme.svg"></div><div class="blockin">                  <div class="blockico"><span></span><img src="/static/assets/error.svg"></div><div class="blocktext">                        <p class="blocktitle">Prompt an error</p><p class="blockdesc">Triggers a specified error</p>        </div></div></div>';
        }
    }
    addEventListenerMulti("click", disabledClick, false, ".side");
    document.getElementById("close").addEventListener("click", function(){
       if (rightcard) {
           rightcard = false;
           document.getElementById("properties").classList.remove("expanded");
           setTimeout(function(){
                document.getElementById("propwrap").classList.remove("itson"); 
           }, 300);
            tempblock.classList.remove("selectedblock");
       } 
    });
    
document.getElementById("removeblock").addEventListener("click", function(){
 flowy.deleteBlocks();
});
var aclick = false;
var noinfo = false;
var beginTouch = function (event) {
    aclick = true;
    noinfo = false;
    if (event.target.closest(".create-flowy")) {
        noinfo = true;
    }
}
var checkTouch = function (event) {
    aclick = false;
}
var doneTouch = function (event) {
    if (event.type === "mouseup" && aclick && !noinfo) {
      if (!rightcard && event.target.closest(".block") && !event.target.closest(".block").classList.contains("dragging")) {
            tempblock = event.target.closest(".block");
            rightcard = true;
            document.getElementById("properties").classList.add("expanded");
            document.getElementById("propwrap").classList.add("itson");
            tempblock.classList.add("selectedblock");
       } 
    }
}
addEventListener("mousedown", beginTouch, false);
addEventListener("mousemove", checkTouch, false);
addEventListener("mouseup", doneTouch, false);
addEventListenerMulti("touchstart", beginTouch, false, ".block");
});
