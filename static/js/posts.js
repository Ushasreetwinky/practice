var tweets;
var i;

function submit()
{
    var text = document.getElementById("tweet").value
	$("#tweet").val("");
    alert(text);
	incidentList(text); 
}

function intialize(){
	tweets = [];
	i = 0;
}
function submitTweet() {
    var text = document.getElementById("tweet").submit()
	tweets[i++] = text
	incidentList();
}
function incidentList(text){		
    var div = document.getElementById('container');
	div.innerHTML = div.innerHTML +"<hr>"+ text;
}
