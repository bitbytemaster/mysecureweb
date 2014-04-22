<SCRIPT LANGUAGE="JavaScript">
<!--
var delay=50;
var currentChar=1;

function type(dest_id, text)
{
    var dest=document.getElementById(dest_id);
    if (dest)
    {
      dest.innerHTML=text.substr(0, currentChar);
      currentChar++
      if (currentChar>text.length)
      {
        currentChar=1;
        setTimeout("type()", 5000);
      }
      else
      {
        setTimeout("type()", delay);
      }
    }
}

function startTyping(textParam, delayParam, destinationParam)
{
  text=textParam;
  delay=delayParam;
  currentChar=1;
  destination=destinationParam;
  type();
}

//-->
//</SCRIPT>
