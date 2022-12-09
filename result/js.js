let searchIcon = document.querySelector("#s");
let searchBar = document.querySelector("#term");
let questions = document.getElementsByClassName("main-title")
let previous;
function findQuestion(prompt){
	if (previous){previous.parentElement.style.backgroundColor="#e0e0e0";}
	for (let q of questions){
		if (q.textContent.toLowerCase().search(prompt.toLowerCase()) != -1){
				q.scrollIntoView();
				q.parentElement.style.backgroundColor="aquamarine"
				previous=q;
				return;
			}
	}
}

searchBar.onblur = () => {
	findQuestion(searchBar.value)
}

searchBar.onkeydown = (event) => {
	if (event.keyCode === 13)
		{
			findQuestion(searchBar.value);
	}
}