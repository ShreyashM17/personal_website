function menu(){
	var active = document.getElementById('nav-btn');
	active.style.display = 'none';
	var clicked = document.getElementById('navigate');
	clicked.classList.add('mnavigation');
	var click = document.getElementById('navbar');
	clicked.classList.add('active');
	var active = document.getElementById('close-btn');
	active.style.display = 'block';
}
function cross(){
	var active = document.getElementById('nav-btn');
	active.style.display = 'block';
	var clicked = document.getElementById('navigate');
	clicked.classList.remove('mnavigation');
	var click = document.getElementById('navbar');
	clicked.classList.remove('active');
	var active = document.getElementById('close-btn');
	active.style.display = 'none';

}
